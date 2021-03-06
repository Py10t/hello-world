from django.urls import path

from . import views

app_name = 'bestellung'
urlpatterns = [
    # ex: bestellung/
    path('', views.index, name='bestellung_index'),
    path('updated/<int:record_id>', views.update_order, name='update_bestellung'),
    path('new_order/', views.create_order, name='add_bestellung'),
    path('new_collective_order/', views.create_collective_order, name='add_sammelbestellung'),
]
