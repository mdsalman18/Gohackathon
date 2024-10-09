from rest_framework import generics
from .models import InternshipRegistration
from .serializers import InternshipRegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class InternshipRegistrationList(generics.ListCreateAPIView):
    queryset = InternshipRegistration.objects.all()
    serializer_class = InternshipRegistrationSerializer


class InternshipRegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = InternshipRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registration successful!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
