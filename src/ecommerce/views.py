from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):

    title = 'home page'
    header = 'this is home page'
    text_data = 'hi, welcome to my home page'
    home_page_link = 'http://127.0.0.1:8000/'
    about_page_link = 'http://127.0.0.1:8000/about/'

    my_contex = {
        'title': title,
        'header': header,
        'text': text_data,
        'home_page_link': home_page_link,
        'about_page_link': about_page_link
    }

    return render(request, "index.html", my_contex)


def about_page(request):

    title = 'about us'
    header = 'this is about page'
    text_data = 'hi, my name is saman'
    home_page_link = 'http://127.0.0.1:8000/'
    about_page_link = 'http://127.0.0.1:8000/about/'

    my_contex = {
        'title': title,
        'header': header,
        'text': text_data,
        'home_page_link': home_page_link,
        'about_page_link': about_page_link
    }

    return render(request, "index.html", my_contex)
