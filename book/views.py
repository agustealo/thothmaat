from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Leaf

def book_list(request):
    leafs = Leaf.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'book/book_list.html', {'leafs': leafs})



def book_detail(request, pk):
    leaf = get_object_or_404(Leaf, pk=pk)
    return render(request, 'book/book_detail.html', {'leaf': leaf})