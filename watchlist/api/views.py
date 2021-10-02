from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from watchlist.models import WatchList, StreamPlatform
from watchlist.api.serializers import (
    WatchlistSerializer, StreamPlatformSerializer
)


class WatchlistAPIView(APIView):
    """Response with watch list data"""

    def get(self, request):
        try:
            watchlist = WatchList.objects.all()
        except WatchList.DoesNotExist:
            return Response({
                "Error": "List Does not exist",
            }, status=status.HTTP_404_NOT_FOUND)

        # serealize data if found
        serialized_data = WatchlistSerializer(watchlist, many=True)

        return Response(serialized_data.data)

    def post(self, request):
        serialized_data = WatchlistSerializer(data=request.data)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response(
            serialized_data.errors, status=status.HTTP_400_BAD_REQUEST
        )


class WatchDetailAPIView(APIView):
    """Returns Movie Detail from wathlist"""

    def get(self, request, pk):
        """Returns Movie detail"""

        try:
            watch_item = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({
                "Error": "Does not exist",
            }, status=status.HTTP_404_NOT_FOUND)

        serialized_data = WatchlistSerializer(watch_item)

        return Response(serialized_data.data)

    def put(self, request, pk):
        try:
            watch_item = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({
                "Error": "Does not exist",
            }, status=status.HTTP_404_NOT_FOUND)

        serialized_data = WatchlistSerializer(watch_item, data=request.data)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response(
            serialized_data.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        try:
            watch_item = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({
                "Error": "Does not exist",
            }, status=status.HTTP_404_NOT_FOUND)

        WatchList.delete(watch_item)
        return Response(status=status.HTTP_204_NO_CONTENT)


# StreamPlatform APIViews

class StreamPlatformAPIView(APIView):
    """Manages Strea platform api views responses"""

    def get(self, request):
        try:
            platforms = StreamPlatform.objects.all()
        except StreamPlatform.DoesNotExist:
            return Response({
                "Error": "No Platform found"
            }, status=status.HTTP_404_NOT_FOUND)

        # if found
        serialized_data = StreamPlatformSerializer(platforms, many=True)
        return Response(serialized_data.data)

    def post(self, request):
        serialized_data = StreamPlatformSerializer(data=request.data)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response(
            serialized_data.errors, status=status.HTTP_400_BAD_REQUEST
        )
