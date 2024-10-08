from django.urls import path
from . import views

app_name = "venues"

urlpatterns = [

    path('login/', views.create_session, name="login"),
    path('logout/', views.destroy_session, name="logout"),
    path('register/', views.register_user, name="register"),

    path('', views.index, name='index'),
    path('venues/', views.venues, name='venues'),
    path('venues/<str:pk>/', views.detail, name='detail'),

    path('create-venue/', views.create_venue, name='create-venue'),
    path('update-venue/<str:pk>/', views.update_venue, name='update-venue'),
    path('delete-venue/<str:pk>/', views.delete_venue, name='delete-venue'),

    path('delete-comment/<str:pk>/', views.delete_comment, name='delete-comment'),
    
    path('venues/<str:pk>/review/', views.create_review, name='create-review'),
    
    path('profile/<str:pk>/', views.profile, name='profile'),
    
    path('venues/<int:pk>/menu', views.menu_list, name='menu'),
    path('delete-menu/<str:pk>/', views.delete_menu, name='delete-menu'),
    path('venues/<int:pk>/menu/<int:menu>', views.menu_items, name="menu-add-items")
    
]
