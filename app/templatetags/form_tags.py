from django import template

from app.forms import ColorForm

register = template.Library()

@register.inclusion_tag("templatetags/color_form.html")
def render_form():
    form = ColorForm
    return {'form': form}

def change_color_view(request):
    if request.method == 'POST':
        form = ColorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) #Redirect to the same page
    else:
        form = ColorForm()
    return form
