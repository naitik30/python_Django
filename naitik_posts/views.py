from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def post_create(request):
    return HttpResponse("<h1>Create First Page<h1>")
def post_details(request):
    return HttpResponse("<h1>Details of All post<h1>")
def post_list(request):
    return HttpResponse("<h1>List view of all post<h1>")
def post_update(request):
    return HttpResponse("<h1>Update the selected post<h1>")
def post_delete(request):
    return HttpResponse("<h1>Delete the selected post<h1>")
