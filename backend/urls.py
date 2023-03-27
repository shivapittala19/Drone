from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import register, home,add_location, delete_location,drone,add_drone,book_drone,view_bookings,delete_booking

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add_location/', add_location, name='add_location'),
    path('delete_location/<int:location_id>/', delete_location, name='delete_location'),
    path('locations/<int:location_id>/add_drone/', book_drone, name='add_drone'),
    path('add_drone/', add_drone, name='add_drone'),
    path('view_bookings/',view_bookings,name='view_bookings'),
    path('booking/<int:booking_id>/delete/', delete_booking, name='delete_booking'),
    # path('book_drone/',book_drone,name="book_drone"),
]
