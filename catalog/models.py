from django.db import models

NULLABLE = {"null": True, "blank": True}


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование продукта")
    description = models.TextField(verbose_name="Описание продукта", **NULLABLE)
    preview = models.ImageField(
        upload_to="products/photo", blank=True, null=True, verbose_name="Превью"
    )
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, related_name="Категории"
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена за продукт"
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )

    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="наименование категории")
    description = models.TextField(verbose_name="Описание категории")

    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Version(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True
    )
    version_name = models.CharField(max_length=50, verbose_name="Наименование версии")
    version_number = models.IntegerField(verbose_name="Номер версии")
    is_active = models.BooleanField(default=True, verbose_name="Активная версия")

    def __str__(self):
        return f"{self.version_name} {self.version_number}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
