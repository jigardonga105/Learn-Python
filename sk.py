# views.py
# I have created this file - sanket
from django.http import HttpResponse
from django.shortcuts import render


# Code for video: 6
# def index(request):
#     return HttpResponse('''<h1> chose your favorite youtube channale</h1>
#
# <a href="https://www.youtube.com/watch?v=zs2Ux1jfDD0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=6 "> code with harry </a><br><br><hr>
# <a href=" "> Telusco  </a><br><br><hr>
# <a href=" ">thapa technical  </a><br><br><hr>
# <a href=" "> technical guruji </a><br><br><hr>
# <a href=" "> carry minati </a><br><br><hr>''')


# def about(request):
#     return HttpResponse("About Harry Bhai")

# def home(request):
#     return HttpResponse("home")
#
# def storedata(request):
#     x=request.GET.get('text','default')
#     print(x)
#     return HttpResponse("your data")

def index(request):
    # param={ 'name':'sanket','city':'surat'}
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")