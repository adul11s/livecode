from django.shortcuts import render

# Create your views here.
def home(request):
    # produk =ProductRekomen.Objects.all()
    return render(request, 'index.html',{
      
    })

def produk(request):
    return render(request,'produk.html')

def detail(request):
    return render(request,'detail_produk.html')
