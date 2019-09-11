from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
# view baseada em função (FBV)
def function_based_view(request, *args, **kwargs):
    return HttpResponse("Olá mundo!")


# view baseada em classe (CBV)
class UrlCBView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("olá novamente!")
