from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import RoomFilter
from rest_framework.permissions import BasePermission
from .permission import (CheckOwner, CheckCRUD, CheckOwnerHotel, CheckStatus, CheckRoleStatus,
                         CheckReview, CheckHotelOwner, CheckBookingUser, CheckImages)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HotelDetailViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializers
    permission_classes = [CheckCRUD]


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["country", "city", "hotel_stars"]
    search_fields = ["name_hotel"]
    ordering_fields = ["hotel_stars"]
    permission_classes = [CheckCRUD]


class HotelImageViewSet(viewsets.ModelViewSet):
    queryset = HotelImage.objects.all()
    serializer_class = HotelImageSerializers
    permission_classes = [CheckImages]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = RoomFilter
    search_fields = ["room_number"]
    ordering_fields = ["price"]
    permission_classes = [CheckStatus, CheckHotelOwner]


class RoomDetailViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializers
    permission_classes = [CheckHotelOwner]


class RoomImagesViewSet(viewsets.ModelViewSet):
    queryset = RoomImages.objects.all()
    serializer_class = RoomImagesSerializers
    permission_classes = [CheckImages]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [permissions.IsAuthenticated, CheckOwner, CheckReview]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    permission_classes = [CheckRoleStatus, CheckBookingUser]
