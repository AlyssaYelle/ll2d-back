from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postcards/', views.PostcardListView.as_view(), name='postcards'),
    path('postcards/approved', views.ApprovedPostcardListView.as_view(), name='approved'),
    path('postcards/submit', views.form, name='submit'),
    path('postcards/create_letter', views.create_letter, name='create_letter')
]