from django import forms
from django.core.exceptions import ValidationError

from .models import Category, Product


class ProductForm(forms.ModelForm):
    forbidden_words = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    class Meta:
        model = Product
        fields = ["name", "price", "description", "image", "category"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название"}
        )
        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите цену"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание"}
        )
        # self.fields["image"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название'})
        self.fields["category"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Выберите категорию"}
        )

    def clean_name(self):
        name = self.cleaned_data["name"]
        if any(word in name.lower() for word in self.forbidden_words):
            raise ValidationError("Нельзя использовать запрещенные слова в имени")
        return name

    def clean_description(self):
        description = self.cleaned_data["description"]
        if any(word in description.lower() for word in self.forbidden_words):
            raise ValidationError("Нельзя использовать запрещенные слова в описании")
        return description

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price <= 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]
