from .models import Hotel, Room
from modeltranslation.translator import TranslationOptions, register


@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('name_hotel', 'description', 'country', 'city', 'address')


@register(Room)
class RoomTranslationOptions(TranslationOptions):
    fields = ('room_description',)