from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import CreateView
from bt import settings
from contact.forms import MessageForm
from contact.models import Message


class MessageCreate(CreateView):
    template_name = 'contact/contact4.html'
    model = Message
    form_class = MessageForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        context = {'form': MessageForm()}
        return render(request, 'contact/contact4.html', context)

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            if request.user.is_authenticated:
                contact.user = self.request.user
            contact.save()
            send_mail(contact.phone, contact.message, settings.DEFAULT_FROM_EMAIL, ['popescu.manuel.denis@gmail.com', ])
            return render(request, 'brand/index.html')
        return render(request, 'contact/contact4.html', {'form': form})


