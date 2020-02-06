
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, HttpResponseRedirect
from .forms import *
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.views.generic import ListView 
from . models import (AboutMe,
                      Info,
                     CompetenceFor, 
                     SloganOrange, 
                     Expertise,
                     Contact,
                     Compteur,
                     Skills, 
                     Beforeskills,
                     Education, 
                     Work, 
                     Liens,
                     ProjectList,
                     CopyRight,
                     Header
                     )
                    

def index(request):
    Contact_Form = ContactForm
    context = {
        'mois': AboutMe.objects.all(),
        'competence': CompetenceFor.objects.all(),
        'slogan': SloganOrange.objects.all(),
        'expert': Expertise.objects.all(),
        'compte': Compteur.objects.all(),
        'pourcent': Skills.objects.all(),
        'bf': Beforeskills.objects.all(),
        'education': Education.objects.all(),
        'work': Work.objects.all(),
        'liens': Liens.objects.all(),
        'contact': Contact.objects.all(),
        'projets': ProjectList.objects.all(),
        'user': Info.objects.all(),
        'right': CopyRight.objects.all(),
        'header': Header.objects.all(),
        'form': Contact_Form,
    }
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            nom = request.POST.get('nom')
            email = request.POST.get('email')
            sujet = request.POST.get('sujet')
            message = request.POST.get('message')
            
            template = get_template('porto/contact_form.txt')
            context = {
                'nom' : nom,
                'email' : email,
                'sujet' : sujet,
                'message' : message,
            }
            content = template.render(context)

            email = EmailMessage(
                "Nouveau Message depuis mon Cv en ligne Django",
                content,
                "Mon CV " + '', 
                ['Danielguedegbe10027@gmail.com'],
                headers = { 'Reply To': email }
            )

            email.send()
            messages.success(request, f'Votre Message a bien été envoyé, je  vous contacterons dans un bref delai .Merci ')
            return redirect('/')
    return render(request, 'porto/index.html',context)




