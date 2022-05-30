
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .services.utils import send_activate_code

from .models import CustomUser
from apps.account.models import CustomUser
from .serializers import CustomAuthTokenSerizlizer, RegisterSerializer


from .serializers import CustomAuthTokenSerizlizer



class LoginView(ObtainAuthToken):

    serializer_class = CustomAuthTokenSerizlizer



class RegisterView(APIView):

    def post(self, request):
        data = request.POST #(email='sadasd', password='#!@#!@')
        serializer = RegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # serializer.validated_data #dict(data)
        user: CustomUser = serializer.save()
        send_activate_code(user.activate_code, user.email)
        return Response(serializer.data)



class ActivateView(APIView):
    #http://localhost:8000/api/v1/account/activate/fsdfsdfsfsf/
    def get(self, request, activate_code):
        user = get_object_or_404(CustomUser, activate_code=activate_code)
        user.is_active = True
        user.save()
        return Response({"messsege": "all okey, your activate account"})


