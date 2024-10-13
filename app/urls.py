from django.urls import path
from . import views


urlpatterns = [
    #path('', views.index_view, name='home'),
    path('', views.month_view, name='month_view'),
    path('month/<int:year>/<int:month>/', views.month_view, name='month_view'),
    path('day/<str:day>/', views.day_view, name='day_view'),
    path('upcoming-items/', views.upcoming_items_view, name='upcoming_items_view'),
    path('create-item-form/', views.create_item_form, name='create_item_form'),
]
