from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.response import Response
from .models import *
from .serilazer import *
from rest_framework import status
from rest_framework.permissions import AllowAny  


@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serailizer = Bookseralizer(books,many=-True)
    return Response({'data':serailizer.data},status=status.HTTP_200_OK)

@api_view(['GET'])
def get_book(request,id):
    try:
        book = Book.objects.get(id=id)
        serailzer = Bookseralizer(book)
        return Response({'data':serailzer.data},status=status.HTTP_200_OK)
    except:
        return Response({'error':'Book not found'},status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes(['AllowAny'])
def create_book(request):
    serailzer = Bookseralizer(data=request.data)
    if serailzer.is_valid():
        serailzer.save()
        return Response({'data':serailzer.data},status=status.HTTP_201_CREATED)
    return Response({'error':serailzer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','PATCH'])
@permission_classes(['AllowAny'])
def update_book(request,id):
    try:
        book = Book.objects.get(id=id)
    except:
         return Response({'error':'Book not found'},status=status.HTTP_404_NOT_FOUND)
    serailzer = Bookseralizer(book,request.data)
    if serailzer.is_valid():
        serailzer.save()
        return Response('data:serailzer.data',status=status.HTTP_200_OK)
    return Response({'error':serailzer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes(['AllowAny'])
def delete_book(request,id):
    try:
        book = Book.objects.get(id=id)  
    except:
        return Response({'error':'Book not found'},status=status.HTTP_404_NOT_FOUND)
    book.delete()
    return Response({'message':'Book deleted successfully'},status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_books_by_author(request, author):
    books = Book.objects.filter(author=author)
    serailizer = Bookseralizer(books,many=True)
    return Response({'data':serailizer.data},status=status.HTTP_200_OK)