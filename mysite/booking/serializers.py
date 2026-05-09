from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]


class HotelImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ["hotel_image"]


class HotelSerializers(serializers.ModelSerializer):
    average_reviews = serializers.SerializerMethodField()
    hotel_image = HotelImageSerializers(read_only = True, many=True)
    class Meta:
        model = Hotel
        fields = ["name_hotel", "hotel_stars", "average_reviews", "country", "city", "hotel_image"]

    def get_average_reviews(self, obj):
        return obj.get_average_reviews()


class ReviewSerializers(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format="%d-%m-%Y" "%H:%M")
    user_name = UserSimpleSerializer()
    class Meta:
        model = Review
        fields = ["user_name", "text", "stars", "parent", "created_date"]


class HotelDetailSerializers(serializers.ModelSerializer):
    hotel_image = HotelImageSerializers(read_only = True, many=True)
    date = serializers.DateField(format="%d-%m-%Y")
    owner = UserSimpleSerializer()
    reviews = ReviewSerializers(many=True, read_only=True)
    average_reviews = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ["name_hotel", "country", "city", "address", "description", "hotel_stars", "average_reviews", "owner", "date", "hotel_image", "reviews"]

    def get_average_reviews(self, obj):
        return obj.get_average_reviews()


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["hotel_room", "room_number", "room_type", "room_status", "all_inclusive", "room_status"]


class RoomImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomImages
        fields = ["room_image"]


class RoomDetailSerializers(serializers.ModelSerializer):
    room_image = RoomImagesSerializers(read_only=True, many=True)
    class Meta:
        model = Room
        fields = ["hotel_room", "room_number", "room_status", "room_type", "all_inclusive", "room_description", "price", "room_image"]


class ReviewDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'