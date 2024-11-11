from django.core.exceptions import ObjectDoesNotExist
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from apps.users.models import User
from apps.users.serializers import UserAuthSerializer, UserSerializer


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    return Response(UserAuthSerializer(users, many=True).data)


@api_view(['GET'])
def get_user_by_id(request, pk):
    user = get_object_or_404(User, id=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def register(request):

    serialiser = UserAuthSerializer(data=request.data)

    if serialiser.is_valid():
        serialiser.save()
        user = User.objects.get(email=request.data.get('email'))
        user.set_password(request.data.get('password'))

        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serialiser.data}, status=HTTP_201_CREATED)

    return Response({'error': serialiser.errors})


@api_view(['POST'])
def login(request):

    user = User.objects.filter(email=request.data.get('email')).first()

    if not user or not user.check_password(request.data.get('password')):
        return Response({"error": "Invalid Credentials"})

    user.save()
    token, created = Token.objects.get_or_create(user=user)
    serialiser = UserAuthSerializer(instance=user)
    return Response({'token': token.key, 'user': serialiser.data})


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        request.user.auth_token.delete()
        return Response({"success": "Successfully logged out."},
                        status=HTTP_200_OK)
    except (AttributeError, ObjectDoesNotExist) as e:
        print(e)


# @api_view(['PUT'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def update(request, pk):
#     user = User.objects.get(id=pk)
#
#     if str(request.user) != str(user) or not request.user.is_admin :
#         return Response({"error": 'Unauthorized action'}, status=HTTP_403_FORBIDDEN)
#
#     serializer = UserSerializer(instance=user, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     else:
#         return Response(serializer.errors)
#     return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])     # permits superusers only
def delete(request, pk):
    user = User.objects.get(id=pk)

    serializer = UserSerializer(user)
    user.delete()
    return Response({"deleted": serializer.data})