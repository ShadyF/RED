from django.shortcuts import render
from django.views.generic import View

from pages.models import Member


class HomePage(View):
    template_name = 'pages/home.html'

    def get(self, request):
        # Maybe add another field to the database indicating whether a person is
        # a CEO or not? Changing the position name requires changing the following
        # line aswell
        ceo = Member.objects.get(position="CEO/Batman")
        rest = Member.objects.exclude(pk=ceo.pk)
        context = {'CEO': ceo, 'Members': rest, 'Count': rest.count()}
        return render(request, self.template_name, context)

