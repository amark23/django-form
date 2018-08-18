from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template import Context

from django.template.loader import get_template

def index(request):
    return render(request, 'form/home.html')
    #return HttpResponse('This page shows a list of most recent posts.')


def user_form(request):
    form_class = UserForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name', '')
            date_of_birth = request.POST.get('date_of_birth', '')
            email_id = request.POST.get('email_id', '')
            phone_number = request.POST.get('phone_number', '')

            # Email the profile with the
            # contact information
            template = get_template('form/contact_template.txt')
            context ={
                'name': name,
                'date_of_birth':date_of_birth,
                'email_id': email_id,
                'phone_number': phone_number,
            }
            content = template.render(context)

            email = EmailMessage(
                "Aglofocus",
                content,
                "Aglofocus Response" + '',
                ['chromaticmusic1@gmail.com'],
                ['chromaticmusic1@gmail.com', 'guymisguided@gmail.com', email_id],
                headers={'Reply-To': email_id}
            )
            email.send()
            return render(request, 'form/contact.html')

    return render(request, 'form/contact.html', {'form': form_class, })