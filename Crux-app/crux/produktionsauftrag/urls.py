from django.urls import path

from . import views

app_name = 'produktionsauftrag'
urlpatterns = [
    # AUFTRAG URLS
    path('', views.index, name='produktionsauftrag_index'),
    path('updated/<int:record_id>', views.update_order, name='update_produktionsauftrag'),
]
