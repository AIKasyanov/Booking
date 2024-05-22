# Booking/booking/views/booking_views.py
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from booking.models.booking_models import Booking
from booking.serializers.booking_serializers import BookingSerializer


class BookingListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def get(self, request, *args, **kwargs):
        bookings = self.get_queryset()

        if bookings:
            serializer = self.serializer_class(bookings, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT, data=[])

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Booking created successfully", "data": serializer.data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class BookingRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer

    def get_object(self):
        booking_id = self.kwargs.get("pk")
        booking = get_object_or_404(Booking, id=booking_id)
        return booking

    def get(self, request, *args, **kwargs):
        booking = self.get_object()
        serializer = self.serializer_class(booking)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, *args, **kwargs):
        booking = self.get_object()
        serializer = self.serializer_class(booking, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK,
                            data={"message": "Booking updated successfully", "data": serializer.data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def delete(self, request, *args, **kwargs):
        booking = self.get_object()
        booking.delete()
        return Response(status=status.HTTP_200_OK, data="Booking deleted successfully")
