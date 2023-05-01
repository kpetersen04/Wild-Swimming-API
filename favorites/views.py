from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated

from .models import Favorite
from .serializers.common import FavoriteSerializer
# from .serializers.populated import PopulatedFavoriteSerializer

class FavoriteListView(APIView):
    permission_classes = (IsAuthenticated, )
    def post(self, request): 
        fav_already_exists = Favorite.objects.filter(
        site = request.data['site'],
        ).first()

        if fav_already_exists:
            return Response({'detail': 'You have already saved this swim site as a favorite.'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        request.data["created_by"] = request.user.id
        favorite_to_create = FavoriteSerializer(data=request.data)

        try: 
            favorite_to_create.is_valid()
            favorite_to_create.save()
            return Response(favorite_to_create.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e: 
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except: 
            return Response('Unprocessible Entity', status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class FavoriteDetailView(APIView):
    def delete(self, request, pk):
        try:
            favorite_to_delete = Favorite.objects.get(pk=pk)
            if favorite_to_delete.created_by !=request.user:
                raise PermissionDenied()
            favorite_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Favorite.DoesNotExist:
            raise NotFound