from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Todo
from .serializers import TodoSerializer


class TodoListApiView(APIView):
    # Get all todo items or by an user
    def get(self, request):
        if(request.user.id):
            todos = Todo.objects.filter(user=request.user.id)
        else:
            todos = Todo.objects
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create a Todo item
    def post(self, request):
        data = {
            'task': request.data.get('task'),
            'completed': request.data.get('completed'),
            'user': request.user.id
        }

        serializer = TodoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailApiView(APIView):
    # Get a todo item
    def get_object(self, todo_id, user_id):
        try:
            return Todo.objects.get(id=todo_id, user=user_id)
        except Todo.DoesNotExist:
            return None

    # Get detail about a todo item
    def get(self, request, todo_id, *args, **kwargs):
        todo_item = self.get_object(todo_id, request.user.id)

        if not todo_item:
            return Response({
                "res": "Object with todo ID doesn't exist"
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = TodoSerializer(todo_item)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a todo item
    def put(self, request, todo_id):
        todo_item = self.get_object(todo_id, request.user.id)

        if not todo_item:
            return Response({
                "res": "Object with todo ID doesn't exist"
            }, status=status.HTTP_400_BAD_REQUEST)

        data = {
            "task": request.data.get("task"),
            "completed": request.data.get("completed"),
            # "user": request.user.id
        }

        print(data)

        serializer = TodoSerializer(instance = todo_item, data=data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a todo item
    def delete(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id, request.user.id)

        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
