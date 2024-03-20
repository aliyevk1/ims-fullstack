from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def getItem(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getItemById(request, pk):
    try:
        item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(item, many=False)

        return Response(serializer.data)
    except Item.DoesNotExist:
        raise Http404("Item does not exist")

@api_view(['POST'])
def addItem(request):

    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteItem(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def editItem(request, pk):
    item = get_object_or_404(Item, pk=pk)
    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
