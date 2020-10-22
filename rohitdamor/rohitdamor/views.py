# i have a created Page views navbar - Rohit

from django.http import HttpResponse

# navbar urls short name

def index(request):
    return HttpResponse('Home Page Rohit Wow,Wow,Wow,Wow,Wow,Wow, Congratulation Rohit Bhai')

def viedos(request):
    return HttpResponse('Videos Page Rohit Wow,Wow,Wow,Wow,Wow,Wow, Congratulation Rohit Bhai')

def about(request):
    return HttpResponse('about Page Rohit Wow,Wow,Wow,Wow,Wow,Wow, Congratulation Rohit Bhai')

def contact(request):
    return HttpResponse('Contact Page Rohit Wow,Wow,Wow,Wow,Wow,Wow, Congratulation Rohit Bhai')

