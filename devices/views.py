from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CreateAuthTokenView(ObtainAuthToken):
    """
    post:
        get or create a authtoken for authenticated user.
    """
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username
        })
