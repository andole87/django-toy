from django.shortcuts import render, redirect
from django.views import generic
from .models import Book, MyPDF
from .forms import RPSForm
from . import pdf



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
            path = pdf.get_pdf_piece(form.cleaned_data['my_name'],rps.my_origin.book_pdf,form.cleaned_data['my_start']-1,form.cleaned_data['my_end']-1)
            rps.save(path)
            return redirect('mylist')
    else:
        form = RPSForm
        return render(request, 'zz/form.html', {'form': form})


