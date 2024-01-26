from os import path
from random import randint
from django.db import models
from django.utils.translation import gettext_lazy as _
# from ckeditor.fields import RichTextField

# Create your models here.
def get_filename_ext(filename):
    filepath = path.basename(filename)
    name, ext = path.splitext(filepath)
    return name, ext

def upload_name_path(instance, filename):
    folderName = randint(1, 40000000)
    filenam = randint(1, folderName)
    ext = get_filename_ext(filename)[1]
    return f'products/{folderName}/{filenam}.{ext}'


class ProductCategory(models.Model):

    category_name = models.CharField(_("Category name"), max_length=100) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product Category")
        verbose_name_plural = _("Product Categories")

    def __str__(self):
        return self.name


def get_default_product_category():
    return ProductCategory.objects.get_or_create(name="Others")[0]


class Product(models.Model):
    image=models.ImageField(upload_to=upload_name_path,null=True)
    product_name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        ProductCategory,
        related_name="product_list",
        on_delete=models.SET(get_default_product_category),
    )
    rating=models.FloatField(default=0.0)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
  
