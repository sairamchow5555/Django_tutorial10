from django.shortcuts import render

# Create your views here.
def imagae_info(request):
    return render(request,'testapp/results.html')
