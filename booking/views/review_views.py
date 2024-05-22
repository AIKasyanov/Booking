# Booking/booking/views/review_views.py
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from booking.models.review_models import Review
from booking.serializers.review_serializers import ReviewSerializer


class ReviewListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def get(self, request, *args, **kwargs):
        reviews = self.get_queryset()
        serializer = self.serializer_class(reviews, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Review created successfully", "data": serializer.data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class ReviewRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer

    def get_object(self):
        review_id = self.kwargs.get("pk")
        review = get_object_or_404(Review, id=review_id)
        return review

    def get(self, request, *args, **kwargs):
        review = self.get_object()
        serializer = self.serializer_class(review)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, *args, **kwargs):
        review = self.get_object()
        serializer = self.serializer_class(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK,
                            data={"message": "Review updated successfully", "data": serializer.data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def delete(self, request, *args, **kwargs):
        review = self.get_object()
        review.delete()
        return Response(status=status.HTTP_200_OK, data="Review deleted successfully")
