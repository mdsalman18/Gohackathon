from rest_framework import generics
from .models import InternshipRegistration
from .serializers import InternshipRegistrationSerializer

class InternshipRegistrationList(generics.ListCreateAPIView):
    queryset = InternshipRegistration.objects.all()
    serializer_class = InternshipRegistrationSerializer
    def perform_create(self, serializer):
        # Save the registration
        instance = serializer.save()



