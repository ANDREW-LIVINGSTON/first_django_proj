from django.shortcuts import render, HttpResponse, redirect

def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse("placeholder to later display list of all blogs")

def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f'placeholder to replace blog number: {number}')


def edit(request, number):
    return HttpResponse(f'placeholder to edit blog {number}')

def destroy(request):
    return redirect('/blogs')