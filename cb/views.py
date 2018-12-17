from django.shortcuts import render,redirect
from django.views import generic
from .models import BookMeta, Usr, Rps
from .forms import RpsForm


# Create your views here.

class BookMetaList(generic.ListView):
    template_name = 'cb/booklist.html'
    context_object_name = 'booklist'

    def get_queryset(self):
        return BookMeta.objects.all()

class UsrList(generic.ListView):
    template_name = 'cb/usr.html'
    context_object_name = 'usrlist'

    def get_queryset(self):
        return Usr.objects.all()

class RpsList(generic.ListView):
    template_name = 'cb/rps.html'
    context_object_name = 'rpslist'

    def get_queryset(self):
        return Rps.objects.all()


def rps_new(request):
    if request.method == "POST":
        form = RpsForm(request.POST)
        if form.is_valid():

            return redirect('rpslist')
    else:
        form = RpsForm
        return render(request, 'cb/rpsform.html', {'form': form})
