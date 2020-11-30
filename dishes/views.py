from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Menu, kyakhayega
from django.urls import reverse
from django.template import loader
# Create your views here.

def index(request):
    latest_item = Menu.objects.order_by('-kab_banaya')[:3]
    context = {
        'latest':latest_item,
    }    
    return render(request, 'dishes/index.html', context)
    

def detail(request, itemid):
    try:
        dish = Menu.objects.get(pk=itemid)
    except Menu.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, "dishes/detail.html",{'dish':dish})

def ingredients(request, itemid):
    item = get_object_or_404(kyakhayega, pk=itemid)
    try:
        kitne_thali = item.set_choice.get(pk=request.POST['kitne_thali'])
    except(KeyError, kyakhayega.DoesNotExist):
        return render(request, 'dishes/detail.html', {"item":item, 'error_msg:':"You didnt select any item"})
    else:
        kitne_thali += 1
        kitne_thali.save()

    return HttpResponseRedirect(reverse('dishes:ingredients', args=(item.id,)))