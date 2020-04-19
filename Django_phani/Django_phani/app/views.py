from django.shortcuts import render
from django.http import HttpRequest
from app.forms import NewUser

# Create your views here.

def index(request):
    return render(request,'app/index.html')

def User(request):

    return render(request,'app/other.html')


def Transfer(request):
    form = NewUser()

    if request.method == 'POST':
        form = NewUser(request.POST)

        if form.is_valid:
            form.save(commit=True)
            return index(request)
        else:

            print("form error")


    return render(request,'app/transfer.html',{'form': form})
