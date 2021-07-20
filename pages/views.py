from django.shortcuts import render
from .models import Works,Categorey
from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, request
# Create your views here.


def index(request):
    most_recent = Works.objects.order_by('-timestamp')[:4]
    

    context={
        
        'most_recent':most_recent,
    }
    return render(request, 'pages/index.html', context)
# def categorey(request):
#     queryset = Works.objects.order_by('categories')
#     query = request.GET.get('q')
#     if query:
#         queryset = queryset.filter(
#             Q(title__icontains = query)
# 		).distinct()
        
#     context = {
#         'queryset': queryset,
       
# 	}
#     return render(request, 'pages/categorey.html', context)


def projects(request):
    
    categorey = request.GET.get('categorey')
   
    if categorey == None:
        works_list = Works.objects.all()
    else:
        works_list = Works.objects.filter(categories__title = categorey)
    categories = Categorey.objects.all()
    context={
      
        'categories':categories,
        'works_list': works_list,
        
    }
    return render(request, 'portfolio/projects.html', context)




def projectOverview(request):
    return render(request, 'pages/details.html')