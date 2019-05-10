from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from generateletter.models import Visaletters

# Create your views here.

# Our original index view function
# Corresponds to original_index.html (rename it to index.html to use it!)

# def index(request):
#     my_dict = {'insert_me':"Now I am coming from first_app/index.html!"}
#     # Make sure this is pointing to the correct index
#     return render(request,'first_app/index.html',context=my_dict)

@method_decorator(login_required, name='dispatch')
class list_view(ListView):
    model = Visaletters
    context_object_name = "list_view"
    template_name = "generateletter/list.html"


class gen_eng_visa(DetailView):
    model = Visaletters
    context_object_name = "detail_visa"
    template_name = "generateletter/gen_eng_visa.html"

class gen_rus_visa(DetailView):
    model = Visaletters
    context_object_name = "russian_visa"
    template_name = "generateletter/gen_rus_visa.html"

class gen_eng_voucher(DetailView):
    model = Visaletters
    context_object_name = "english_voucher"
    template_name = "generateletter/gen_eng_voucher.html"

class gen_rus_voucher(DetailView):
    model = Visaletters
    context_object_name = "russian_voucher"
    template_name = "generateletter/gen_rus_voucher.html"


def error_404(request):
        data = {}
        return render(request,'generateletter/error_404.html', data)

def error_500(request):
        data = {}
        return render(request,'generateletter/error_500.html', data)
