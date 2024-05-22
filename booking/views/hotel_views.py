# Booking/booking/views/hotel_views.py
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from booking.models.hotel_models import Hotel
from booking.serializers.hotel_serializers import HotelSerializer


class HotelListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()

    def get(self, request, *args, **kwargs):
        hotels = self.get_queryset()
        serializer = self.serializer_class(hotels, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Hotel created successfully", "data": serializer.data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class HotelRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HotelSerializer

    def get_object(self):
        hotel_id = self.kwargs.get("pk")
        hotel = get_object_or_404(Hotel, id=hotel_id)
        return hotel

    def get(self, request, *args, **kwargs):
        hotel = self.get_object()
        serializer = self.serializer_class(hotel)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, *args, **kwargs):
        hotel = self.get_object()
        serializer = self.serializer_class(hotel, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK,
                            data={"message": "Hotel updated successfully", "data": serializer.data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def delete(self, request, *args, **kwargs):
        hotel = self.get_object()
        hotel.delete()
        return Response(status=status.HTTP_200_OK, data="Hotel deleted successfully")
