from django.utils import timezone
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.http import Http404, HttpResponse, HttpResponseForbidden, JsonResponse
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from calendar import monthrange
import calendar
from datetime import datetime, time, timedelta
from .forms import *
from .models import Item
import os

User = get_user_model()

"""
def get_color_for_value(value, max_value, colormap_name='viridis'):
    #Generate a color from a colormap given a value and a maximum.
    norm = value / max_value if max_value > 0 else 0
    cmap = cm.get_cmap(colormap_name)
    rgba = cmap(norm)  # Returns an RGBA tuple
    # Convert RGBA to hex
    return '#{:02x}{:02x}{:02x}'.format(int(rgba[0] * 255), int(rgba[1] * 255), int(rgba[2] * 255))
"""

def get_color_for_value(value, max_value, color_map='viridis'):
    if max_value == 0:
        return '#f0f0f0'
    normalized_value = min(value /max_value, 1.0)
    cmap = cm.get_cmap(color_map)
    color = cmap(normalized_value)
    #color = cm.Oranges(normalized_value) #viridis, Purples, plasma, magma, YlGnBu, Greens, Blues, Oranges, inferno, Reds, 
    return '#' + ''.join(f'{int(c * 255):02x}' for c in color[:3])


def generate_colorbar(colormap_name):
    colorbar_filename = f'colorbar_{colormap_name}.png'
    colorbar_path = os.path.join(settings.MEDIA_ROOT, colorbar_filename)

    # Check if the image already exists
    if not os.path.exists(colorbar_path):
        # Create a figure for the colorbar if it doesn't exist
        fig, ax = plt.subplots(figsize=(6, 1))
        fig.subplots_adjust(bottom=0.5)

        # Create a gradient for the colorbar with values ranging from 0 to 10
        gradient = np.linspace(0, 10, 256)
        gradient = np.vstack((gradient, gradient))

        # Get the colormap by name (e.g., 'viridis', 'plasma', etc.)
        colormap = cm.get_cmap(colormap_name)

        # Display the colorbar using the specified colormap
        ax.imshow(gradient, aspect='auto', cmap=colormap, extent=[0, 10, 0, 1])
        ax.set_axis_off()

        # Save the figure to the defined path
        fig.savefig(colorbar_path, bbox_inches='tight', pad_inches=0)
        plt.close(fig)

    # Construct the URL for the colorbar image
    image_url = os.path.join(settings.MEDIA_URL, colorbar_filename)

    return image_url

def index_view(request):
    context = {}
    return render(request, 'index.html', context)


def change_color_view(request):
    user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = ColorForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ColorForm(instance=user)
    return form

@login_required
def month_view(request, year=None, month=None):
    # If year or month is not provided, use the current date
    if year is None or month is None:
        today = timezone.now()
        year = today.year
        month = today.month
    else:
        year = int(year)
        month = int(month)

    # Get the number of days in the given month and year
    num_days = monthrange(year, month)[1]
    days = [timezone.datetime(year, month, day) for day in range(1, num_days + 1)]

    days_with_weekdays = []
    for day in days:
        weekday_index = day.weekday()
        weekday_name = calendar.day_name[weekday_index]
        days_with_weekdays.append({'date': day, 'weekday':weekday_name})

    # Get items for the current month, filtered by the logged-in user
    items = Item.objects.filter(date__year=year, date__month=month, user=request.user)

    """
    # Organize items by day and get the maximum number of items for a single day
    items_by_day = {}
    max_items = 0
    for item in items:
        day_items = items_by_day.setdefault(item.date.day, [])
        day_items.append(item)
        if len(day_items) > max_items:
            max_items = len(day_items)

    # Generate colors based on the number of items using the Viridis color map
    day_colors = {}
    for day, items in items_by_day.items():
        num_items = len(items)
        day_colors[day] = get_color_for_value(num_items, max_items)
    """

    items_by_day = {day: [] for day in range(1, num_days + 1)}
    print(items_by_day)
    for item in items:
        if item.date.day not in items_by_day:
            items_by_day[item.date.day] = []
        items_by_day[item.date.day].append(item)


    max_items =  max(len(items_by_day[day]) for day in range(1, num_days + 1))
    
    # Generate colors based on the number of items using the Viridis color map
    day_colors = {}
    for day in range (1, num_days + 1):
        num_items = len(items_by_day.get(day, []))
        if request.user.colors == '':
           day_colors[day] = get_color_for_value(num_items, max_items)
        else:
            day_colors[day] = get_color_for_value(num_items, max_items, request.user.colors)

    # Calculate the previous and next month
    prev_month_date = (timezone.datetime(year, month, 1) - timedelta(days=1)).replace(day=1)
    next_month_date = (timezone.datetime(year, month, num_days) + timedelta(days=1)).replace(day=1)

    current_date = timezone.now().date()

    print(items_by_day)
    print(type(items_by_day))
    print(items_by_day.get(2))
    print(day_colors)
    print(request.user.colors)

    color_form = change_color_view(request)
    print(color_form)
    colorbar_url = generate_colorbar(request.user.colors)

    cal = calendar.Calendar(firstweekday=6)
    days_of_week = list(calendar.day_name)

    days_of_week = days_of_week[-1:] + days_of_week[:-1]
    month_days = cal.monthdayscalendar(year, month)
    print(month_days)
    print(num_days)
    
    
    context = {
        'form': color_form,
        'days': days,
        'items_by_day': items_by_day,
        'day_colors': day_colors,
        'current_year': year,
        'current_month': month,
        'prev_month': prev_month_date,
        'next_month': next_month_date,
        'today': current_date,
        'current_date': current_date,
        'days_with_weekdays': days_with_weekdays,
        'colorbar_url': colorbar_url,
        'days_of_week': days_of_week,
        'month_days': month_days,
    }

    return render(request, 'timetable/month.html', context)

# Function to generate all time slots from 12 AM to 11 PM in one-hour intervals
def generate_time_slots():
    start_time = time(0, 0)  # Start at 12:00 AM
    slots = []
    for hour in range(24):  # 24 hours
        slots.append((datetime.combine(datetime.today(), start_time) + timedelta(hours=hour)).time())
    return slots


def day_view(request, day):
    selected_date = datetime.strptime(day, '%Y-%m-%d').date()
    items = Item.objects.filter(date=selected_date)
    
    # Generate time slots and match available items
    time_slots = generate_time_slots()
    schedule = {slot: None for slot in time_slots}
    
    for item in items:
        schedule[item.time] = item.description
    
    return render(request, 'timetable/day.html', {'schedule': schedule, 'date': selected_date})


@login_required
def upcoming_items_view(request):
    # Get the latest 5 upcoming items for the logged-in user
    upcoming_items = Item.objects.filter(user=request.user, date__gte=timezone.now().date()).order_by('date', 'time')[:10]
    
    context = {
        'upcoming_items': upcoming_items,
    }

    return render(request, 'timetable/upcoming_items.html', context)

def create_item_form(request):
    item_form = ItemForm()
    context = {'form':item_form}
    if request.method == 'POST':
        form  = ItemForm(request.POST)
        if form.is_valid():
            
            now = timezone.now()
            
            item_data = form.save(commit=False)
            item_data.user = request.user
            item_data.date = now.date()
            item_data.time = now.time()
            item_data.save()

            print("Done")

            return redirect('/')
        else:
            message = f"{form.errors}"
            messages.success(request, message)
            return render(request, 'timetable/create_item_form.html', context)
    return render(request, 'timetable/create_item_form.html', context)
