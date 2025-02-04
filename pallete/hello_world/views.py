from django.shortcuts import render, HttpResponse
import os



def login(request):
    filepath=os.path.join(os.path.dirname(__file__),'index.html')

    with open( filepath,'r') as html_file:
        html_content = html_file.read()
    return  HttpResponse(html_content,content_type="text/html")

def home(request):
    filepath=os.path.join(os.path.dirname(__file__),'home.html')

    with open( filepath,'r') as html_file:
        html_content = html_file.read()
    return  HttpResponse(html_content,content_type="text/html")


    

