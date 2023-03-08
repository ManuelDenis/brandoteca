from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import CreateView

from bt import settings
from contact.forms import MessageForm, NewsletterForm
from contact.models import Message, Newsletter


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


class NewsletterCreate(CreateView):
    template_name = 'brand/index.html'
    model = Newsletter
    form_class = NewsletterForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        context = {'form': NewsletterForm()}
        return render(request, 'brand/index.html', context)

    def post(self, request, *args, **kwargs):
        form = NewsletterForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            if request.user.is_authenticated:
                news.user = self.request.user
                news.email = self.request.user.email
            news.save()
            return render(request, 'brand/index.html')
        return render(request, 'brand/index.html', {'form': form})
