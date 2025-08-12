from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Blogpost
from .serializers import BlogpostSerializer
# Create your views here.
class BlogpostListCreate(generics.ListCreateAPIView):
    queryset=Blogpost.objects.all()
    serializer_class= BlogpostSerializer

    def delete(self, request, *args, **kwargs):
        Blogpost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogpostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blogpost.objects.all()
    serializer_class= BlogpostSerializer
    lookup_field="pk"