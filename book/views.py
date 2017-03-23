from django.shortcuts import render
from django.utils import timezone
from .models import Leaf

def book_list(request):
    leafs = Leaf.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'book/book_list.html', {'leafs': leafs})