from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ('simpleUser', 'SimpleUser'),
        ('ownerUser', 'OwnerUser'),
    )
    status = models.CharField(max_length=18, choices=ROLE_CHOICES, default='simpleUser')
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(70)],
                                           null=True, blank=True)
    date_registered = models.DateField(auto_now_add=True, null=True, blank=True)


class Hotel(models.Model):
    name_hotel = models.CharField(max_length=32)
    description = models.TextField()
    hotel_stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 5)], verbose_name="Рейтинг", null=True,
                                blank=True)
    country = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name_hotel} - {self.country}'

    def get_average_reviews(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum(reviews.stars for reviews in reviews) / reviews.count(), 1)
        return 0


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="hotel_image")
    hotel_image = models.ImageField(upload_to='hotel_images/')


class Room(models.Model):
    hotel_room = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.PositiveSmallIntegerField(default=0)
    TYPE_CHOICES =(
        ("люкс", "люкс"),
        ("семейный", "семейный"),
        ("одноместный", "одноместный"),
        ("двухместный", "двухместный")
    )
    room_type = models.CharField(max_length=16, choices=TYPE_CHOICES, default='одноместный')
    STATUS_CHOICES = (
        ('забронирован', 'Забронирован'),
        ('свободен', 'Свободен'),
        ('занят', 'Занят')
    )
    room_status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='свободен')
    price = models.PositiveIntegerField()
    all_inclusive = models.BooleanField(default=False)
    room_description = models.TextField()

    def __str__(self):
        return f'{self.hotel_room} - {self.room_number} - {self.room_type}'


class RoomImages(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="room_image")
    room_image = models.ImageField(upload_to='room_image')


class Review(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, related_name='reviews', on_delete=models.CASCADE)
    text = models.TextField()
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 5)], verbose_name="Рейтинг", null=True,
                                blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_name} - {self.hotel} - {self.stars}'


class Booking(models.Model):
    hotel_book = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_book = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_book = models.ForeignKey(User, max_length=32, on_delete=models.CASCADE)
    checkin_date = models.DateTimeField()
    checkout_date = models.DateTimeField()
    total_price = models.PositiveIntegerField(default=0)
    STATUS_BOOK_CHOICES = (
        ('отменено', 'Отменено'),
        ('подтверждено', 'Подтверждено')
    )
    status = models.CharField(max_length=16, choices=STATUS_BOOK_CHOICES)

    def __str__(self):
        return f"{self.room_book}, {self.hotel_book}, {self.room_book}, {self.status}"
