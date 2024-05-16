from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .utils.groq_init import groq_client

# Create your views here.

@api_view(['POST'])
def chat_with_groq(request):
    query = request.data
    print('query', query)
    chat_completion = groq_client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "you are a Coding assistant."
            },
            {
                "role": "user",
                "content": query['prompt'],
            }
        ],
        model="llama3-8b-8192",
    )
    print()
    return Response({'response': chat_completion.choices[0].message.content}, status=status.HTTP_200_OK)
