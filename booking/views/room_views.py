# Booking/booking/views/room_views.py
from django.db.models import Q
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from booking.models.hotel_models import Hotel
from booking.models.room_models import Room
from booking.serializers.room_serializers import RoomSerializer


class RoomListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

    def get(self, request, *args, **kwargs):
        rooms = self.get_queryset()
        serializer = self.serializer_class(rooms, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Room created successfully", "data": serializer.data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class RoomRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RoomSerializer

    def get_object(self):
        room_id = self.kwargs.get("pk")
        room = get_object_or_404(Room, id=room_id)
        return room

    def get(self, request, *args, **kwargs):
        room = self.get_object()
        serializer = self.serializer_class(room)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, *args, **kwargs):
        room = self.get_object()
        serializer = self.serializer_class(room, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK,
                            data={"message": "Room updated successfully", "data": serializer.data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def delete(self, request, *args, **kwargs):
        room = self.get_object()
        room.delete()
        return Response(status=status.HTTP_200_OK, data="Room deleted successfully")


class AvailableRoomsListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RoomSerializer

    def get_queryset(self):
        # Получаем список свободных номеров для каждого отеля
        hotel_rooms = []
        hotels = Hotel.objects.all()
        for hotel in hotels:
            free_rooms = Room.objects.filter(Q(hotel_id=hotel.id) & Q(available=True))
            hotel_rooms.extend(free_rooms)
        return hotel_rooms

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
