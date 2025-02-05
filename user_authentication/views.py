import logging
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Get the logger for the 'user_authentication' app (as configured in settings.py)
logger = logging.getLogger('user_authentication')


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Create the user and hash the password automatically
            user = serializer.save()
            # Log user creation event
            logger.info(f"User created: {user.username} (ID: {user.id})")
            return Response({"Message": "User Created successfully", "User": serializer.data},
                            status=status.HTTP_201_CREATED)
        # Log invalid data error
        logger.error(f"User creation failed: Invalid data - {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def get_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        logger.warning(f"User with ID {pk} does not exist")
        return Response({"message": "User Not Found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    logger.info(f"User details fetched: {user.username} (ID: {user.id})")
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])  # Ensure the user is authenticated
def get_all_user(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        logger.info(f"Fetched {len(users)} users from the database")
        return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def update_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        logger.warning(f"User with ID {pk} does not exist")
        return Response({"message": "User Not Found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user, request.data)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"User updated: {user.username} (ID: {user.id})")
        return Response({"message": "User Updated Succesfully", "user": serializer.data})
    logger.error(f"User update failed: Invalid data - {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])  # Ensure the user is authenticated
def delete_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        logger.warning(f"User with ID {pk} does not exist")
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    user.delete()
    logger.info(f"User deleted: {user.username} (ID: {user.id})")
    return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
