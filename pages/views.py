from django.db.models.fields import FilePathField, files
from django.http.response import FileResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from .models import Testimonial, Works,Categorey
from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, request
from django.core.files.storage import FileSystemStorage
from .forms import ContactForm,ContactFormDb
from django.core.mail import EmailMessage    
from portfolio.settings import EMAIL_HOST, EMAIL_HOST_USER   
from django.contrib import messages
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




def details(request, slug):
    details = Works.objects.filter(slug=slug)
    
    if details.exists():
        details = get_object_or_404(Works, slug = slug)

        return render(request, "pages/details.html", {"details": details})
        
    else:
        return HttpResponse("<h3>page not found</h3>")
        
         
''' def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            name   = form.cleaned_data['name']
            email_from =  form.cleaned_data['email_from']   
            email_to = EMAIL_HOST_USER   
            message= form.cleaned_data['message']
            #send_mail(subject, message, email_from, [email_to,], fail_silently=False)
            email = EmailMessage(subject=subject,body=message,from_email=email_from,to=[email_to,],reply_to=[email_from],)
            email.send()
            return render(request, 'pages/contact.html', {'form': form})
    form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form}) '''
    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            name   = form.cleaned_data['name']
            email_from =  form.cleaned_data['email_from']   
            email_to = EMAIL_HOST_USER   
            message= form.cleaned_data['message']
            #save data into DB code    
            
            email = EmailMessage(subject=subject,body=message,from_email=email_from,to=[email_to,],reply_to=[email_from],)
            email.send()
            #save data into DB code 
            form = ContactFormDb(request.POST)
            cemetery=form.save(commit=False)
            cemetery.name=request.POST.get('name')
            cemetery.email_from=request.POST.get('email_from')
            cemetery.subject=request.POST.get('subject')
            cemetery.message=request.POST.get('message')
            cemetery.save() 
            messages.success(request, 'Great! Your messages submitted')
            return render(request, 'pages/contact.html', {'form': form})
        else:
            messages.warning(request, 'please fill the form!')
            return render(request, 'pages/contact.html')
    form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})



def testimonial(request):
    testimonial_list = Testimonial.objects.all()
   
    context ={
        'testimonial_list': testimonial_list
    }
    return render(request, 'pages/testimonial.html',context)