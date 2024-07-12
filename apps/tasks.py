
from django.db.models import Model, TextField, ImageField, CharField, ForeignKey, CASCADE, BooleanField, FileField


class Product(Model):
    name = CharField(max_length=255)
    description = TextField()
    video = FileField(upload_to='product_video/')
    is_premium = BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductImages(Model):
    image = ImageField(upload_to='product_image/')
    product = ForeignKey('apps.Product', CASCADE, related_name='images')
