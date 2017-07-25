from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'index.html'


class ConfirmationPage(TemplateView):
    template_name = 'confirmation.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'
