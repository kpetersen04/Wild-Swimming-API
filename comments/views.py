from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated

from .models import Comment
from .serializers.common import CommentSerializer

class CommentListView(APIView):
     permission_classes = (IsAuthenticated, )
     def post(self, request): 
          request.data["created_by"] = request.user.id
          comment_to_create = CommentSerializer(data=request.data)

          try: 
               comment_to_create.is_valid()
               comment_to_create.save()
               return Response(comment_to_create.data, status=status.HTTP_201_CREATED)
          except IntegrityError as e: 
               return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
          except AssertionError as e:
               return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
          except: 
               return Response('Unprocessible Entity', status=status.HTTP_422_UNPROCESSABLE_ENTITY)
          
class CommentDetailView(APIView):
     permission_classes = (IsAuthenticated, )

     def put(self, request, pk):
          print('You made it to the edit endpoint.')
          comment_to_edit = Comment.objects.get(pk=pk)
          updated_comment = CommentSerializer(comment_to_edit, data=request.data)
          try:
               updated_comment.is_valid()
               updated_comment.save()
               return Response(updated_comment.data, status=status.HTTP_202_ACCEPTED)
          except AssertionError as e: 
               return Response({'detail': str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
          except: 
               res = {"detail": "Unprocessable Entity"}
               return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

     def delete(self, request, pk):
          try:
               comment_to_delete = Comment.objects.get(pk=pk)
               if comment_to_delete.created_by !=request.user:
                    raise PermissionDenied()
               comment_to_delete.delete()
               return Response(status=status.HTTP_204_NO_CONTENT)
          except Comment.DoesNotExist:
               raise NotFound
          

    