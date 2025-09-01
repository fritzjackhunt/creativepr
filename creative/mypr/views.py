from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'creative/index.html')

def campaign(request):
    return render(request, 'creative/campaign.html')

def pricing(request):
    return render(request, 'creative/pricing.html')

def forbrands(request):
    return render(request, 'creative/forbrands.html')