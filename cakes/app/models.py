from django.db import models

# Create your models here.
# class CategoryChoices(models.TextChoices):

#     BIRTHDAY_CAKE= 'Birthday Cakes','Birthday Cakes'

#     WEDDING_CAKE= 'Weddding Cakes','Wedding Cakes'

# class ShapeChoices(models.TextChoices):

#     RECTANGLE='Rectangle','Reactangle'

#     ROUND='Round','Round'

# class WeightChoices(models.TextChoices):

#     HALF_KG='1/2 kg','1/2 kg'

#     ONE_KG= '1 kg','1 kg'

#     TWO_KG= '2 kg','2 kg'

class Category(models.Model):   

    name = models.CharField(max_length=50)

    def __str__(self):

        return self.name

    class Meta:

        verbose_name='Category'

        verbose_name_plural='Categories'

class Shape(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):

        return self.name

    class Meta:

        verbose_name='Shape'

        verbose_name_plural='Shapes'

class Weight(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):

        return self.name

    class Meta:

        verbose_name='Weight'

        verbose_name_plural='Weights'

class Cake(models.Model):

    name=models.CharField(max_length=50)

    description=models.TextField()

    photo=models.ImageField(upload_to='cake-images')

    category=models.ForeignKey('Category',on_delete=models.PROTECT)

    shape=models.ForeignKey('Shape',on_delete=models.PROTECT)

    weight=models.ForeignKey('Weight',on_delete=models.PROTECT)

    price=models.FloatField()

    def __str__(self):

        return self.name

    class Meta:

        verbose_name='Cakes'

        verbose_name_plural='Cakes'