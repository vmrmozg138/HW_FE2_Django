from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from catalog.models import Category, Product
from .forms import CategoryForm, ProductForm
from .mixins import OwnerRequiredMixin


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class HomeView(TemplateView):
    template_name = "catalog/home.html"


class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "catalog/contacts.html")

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


"""делаем недостающие формы для CRUD"""


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:products")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:products")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        raise PermissionDenied


class ProductDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, OwnerRequiredMixin, DeleteView
):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:products")

    def test_func(self):
        return self.request.user.has_perm("catalog.delete_product")

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return HttpResponseForbidden("Вы не можете удалять товары")
        return super().handle_no_permission()


class ProductTogglePublishView(LoginRequiredMixin, View):
    """новый контроллер для публикации"""

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if not request.user.has_perm("catalog.can_unpublish_product"):
            return HttpResponseForbidden("Вы не можете управлять публикацией")

        product.is_published = not product.is_published
        product.save(update_fields=["is_published"])
        return redirect("catalog:product_detail", pk=pk)


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "catalog/category_form.html"


"""ниже все старое"""

"""def home(request):
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
    return render(request, "product_detail.html", context)"""
