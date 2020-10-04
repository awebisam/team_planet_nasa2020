from django.urls import path

from . import views
app_name = "core"
urlpatterns = [
    path('', views.index, name="index"),
    path('newsletter', views.newsletter, name='newsletter'),
    path("accounts/profile/", views.profileview, name="profile"),
    path('team/', views.team, name="team"),
    path('contact/', views.contact, name="contact"),
    path('portal/', views.portal, name="portal"),
]
