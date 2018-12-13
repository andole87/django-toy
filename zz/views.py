from django.shortcuts import render, redirect
from django.views import generic
from .models import Book, MyPDF
from PyPDF2 import PdfFileReader, PdfFileWriter
from .forms import RPSForm
import os
from django.conf import settings


# Create your views here.

class BookList(generic.ListView):
    template_name = 'zz/index.html'
    context_object_name = 'booklist'

    def get_queryset(self):
        return Book.objects.all()

class MyList(generic.ListView):
    template_name = 'zz/my.html'
    context_object_name = 'mylist'

    def get_queryset(self):
        return MyPDF.objects.all()


def rps_new(request):
    if request.method == "POST":
        form = RPSForm(request.POST)
        if form.is_valid():
            rps = form.save(commit=False)
            

            rps.save()
            return redirect('mylist')
    else:
        form = RPSForm
        return render(request, 'zz/form.html', {'form': form})

def make_rps(origin,start,end):
    pdfpath = os.path.join(settings.BASE_DIR, 'media', 'pdf', origin)
    inp = PdfFileReader(open(pdfpath,'rb'))
    out = PdfFileWriter()
    out.addPage(inp.getPage)
