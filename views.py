from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@csrf_exempt
def home(request):
    answer = ''

    if request.method == 'POST':
        question = request.POST.get('question')

        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'user', 'content': question}
            ]
        )

        answer = response.choices[0].message.content

    return render(request, 'analytics/home.html', {'answer': answer})

