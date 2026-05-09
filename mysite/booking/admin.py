from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *


class HotelImageInLines(admin.TabularInline):
    model = HotelImage
    extra = 1


@admin.register(Hotel)
class HotelAdmin(TranslationAdmin):
    inlines = [HotelImageInLines]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class RoomImagesInLines(admin.TabularInline):
    model = RoomImages
    extra = 1


@admin.register(Room)
class RoomAdmin(TranslationAdmin):
    inlines = [RoomImagesInLines]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(User)
admin.site.register(Review)
admin.site.register(Booking)

