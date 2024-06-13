import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        # Здесь мы получаем данные из фикстурв с категориями
        with open("category.json", "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def json_read_products():
        # Здесь мы получаем данные из фикстурв с продуктами
        with open("product.json", "r", encoding="utf-8") as file:
            return json.load(file)

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_list = []
        category_list = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_list.append(
                {
                    "id": category["pk"],
                    "name": category["fields"]["name"],
                    "description": category["fields"]["description"],
                }
            )
        create_for_category = []
        for category_item in category_list:
            create_for_category.append(Category(**category_item))

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(create_for_category)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_list.append(
                {
                    "id": product["pk"],
                    "name": product["fields"]["name"],
                    "description": product["fields"]["description"],
                    "price": product["fields"]["price"],
                    "category": Category.objects.get(pk=product["fields"]["category"]),
                    "preview": product["fields"]["preview"],
                    "created_at": product["fields"]["created_at"],
                    "updated_at": product["fields"]["updated_at"],
                }
            )
        product_for_create = []
        for product_item in product_list:
            product_for_create.append(Product(**product_item))

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
