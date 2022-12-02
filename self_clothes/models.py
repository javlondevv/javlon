from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.db.models import (
    Model,
    CharField,
    DecimalField,
    ForeignKey,
    SlugField,
    ImageField
)
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class self_clothes(models.Model):
    name = CharField(max_length=255)
    description = RichTextField()
    price = DecimalField(max_digits=5, decimal_places=2)
    image = ImageField(upload_to='self_clothes/%m')
    category = ForeignKey(Category, models.SET_DEFAULT, default='all')
    slug = SlugField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        while self_clothes.objects.filter(slug=self.slug).exists():
            slug = self_clothes.objects.filter(slug=self.slug).first().slug
            if '-' in slug:
                try:
                    if slug.split('-')[-1] in self.name:
                        self.slug += '-1'
                    else:
                        self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                except:
                    self.slug = slug + '-1'
            else:
                self.slug += '-1'

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Clothes'


class Review(models.Model):
    class Rate_Choices(models.IntegerChoices):
        Worse = 1
        Bad = 2
        Good = 3
        Excellent = 4
        Best = 5

    user = models.ForeignKey(User, models.SET_DEFAULT, default='Unknown')
    text = RichTextField(null=True)
    clothes = models.ForeignKey(self_clothes, models.CASCADE, null=True)
    rate = models.PositiveSmallIntegerField(choices=Rate_Choices.choices, null=True)
