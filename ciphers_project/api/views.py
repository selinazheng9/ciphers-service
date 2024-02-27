from django.http import JsonResponse
from .ciphers import caesar_encode

def greetings(request):
    result = {"message": "Welcome to ciphers service!"}
    return JsonResponse(result)

def encode(request, plainText, shift):
    parameters = dict(request.GET)
    print(parameters)
    cipher = caesar_encode(plainText,shift)
    return JsonResponse({"cipher":cipher})