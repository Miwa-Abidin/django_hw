from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from .models import Item, Purchase

def greetings(request):
    return HttpResponse('welcome to greetings')

def list_item(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'list_item.html', context)

def detail_item(request, id):
    item = get_object_or_404(Item, id=id)
    context = {
        'item': item,
    }
    return render(request, 'detail.html', context)
