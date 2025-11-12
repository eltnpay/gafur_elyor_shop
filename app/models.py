from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100, 
        unique=True, 
        verbose_name='Название категории'
        )
    description = models.TextField(
        blank=True, 
        null=True, 
        verbose_name='Описание'
        )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(
        max_length=100, 
        unique=True, 
        verbose_name='Название бренда'
        )
    country = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        verbose_name='Страна производителя'
        )
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(
        max_length=200, 
        verbose_name='Название товара'
        )
    description = models.TextField(
        verbose_name='Описание'
        )
    price = models.PositiveBigIntegerField(
        verbose_name='Цена'
        )
    image = models.ImageField(
        upload_to='products/', 
        verbose_name='Изображение товара')
    in_stock = models.PositiveIntegerField(
        default=0, 
        verbose_name='Количество на складе')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products', verbose_name="Бренд")

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title
