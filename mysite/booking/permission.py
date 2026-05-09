from rest_framework import permissions
from rest_framework.permissions import BasePermission


class CheckOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user.status == "ownerUser":
            return False
        return True


class CheckCRUD(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.status == "ownerUser"


class CheckOwnerHotel(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class CheckStatus(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.status == "simpleUser":
            return obj.room_status == "свободен"
        return False


class CheckRoleStatus(BasePermission):
    def has_permission(self, request, view):
        if request.user.status == "simpleUser":
            return True
        return False


class CheckReview(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_name == request.user


class CheckHotelOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.hotel_room.owner == request.user


class CheckBookingUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user_book:
            return True
        return False


class CheckImages(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True