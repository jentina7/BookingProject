from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"hotels", HotelViewSet, basename="hotel-list"),
router.register(r"hotel-detail", HotelDetailViewSet, basename="hotel-detail"),
router.register(r"users", UserViewSet, basename="users-list"),
router.register(r"users-detail", UserViewSet, basename="users-detail"),
router.register(r"rooms", RoomViewSet, basename="room-list"),
router.register(r"room-detail", RoomDetailViewSet, basename="room-detail"),
router.register(r"room_images", RoomImagesViewSet, basename="room-images-list"),
router.register(r"hotel-images", HotelImageViewSet, basename="hotel-images-list"),
router.register(r"review", ReviewViewSet, basename="review-list"),
router.register(r"review-detail", ReviewViewSet, basename="review-detail"),
router.register(r"booking", BookingViewSet, basename="booking-list")


urlpatterns = [
    path("", include(router.urls))
]

