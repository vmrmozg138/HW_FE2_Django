from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class HomeView(TemplateView):
    template_name = "catalog/home.html"


class ContactView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'catalog/contacts.html')

    def post(self,request,*args,**kwargs):
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


'''ниже все старое'''

'''def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("name")
        message = request.POST.get("message")
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        print(name)
        print(message)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "contacts.html")

def products(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product_list.html", context)


def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {"product": product}
    return render(request, "product_detail.html", context)'''
