from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# from django.template.defaultfilters import slugify # new
from django.urls import reverse

class Animal(models.Model):
    # ANIMALS = (
    #     ('X', 'Choose animalfamily')
    #     (REPTILES(), 'Reptiles'),
    # )
    REPTILES = (
        ('X', 'Choose type of reptile'),
        ('C', 'Crocodile'),
        ('L', 'Lizard'),
        ('S', 'Snake'),
        ('T', 'Turtle'),
    )

    CITES_SPECIES = (
        ('X', 'Cites of animal'),
        ('A', 'Cites A or I'),
        ('B', 'Cites B or II'),
        ('C', 'Cites C or III'),
        ('D', 'Cites D or none'),
    )

    title = models.CharField(blank=True, null=True, max_length=120)
    latinName = models.CharField(blank=True, null=True, max_length=120)
    # TypeofAnimal = models.CharField(blank=True, null=True, default='X', choises=ANIMALS)
    reptiletype = models.CharField(blank=True, null=True, max_length=1, default='X', choices=REPTILES)
    image = models.ImageField(blank=True, null=True, upload_to="animal_images")
    cites = models.CharField(blank=True, null=True, max_length=1, default='X', choices=CITES_SPECIES)
    habitat = models.CharField(blank=True, null=True, max_length=120)
    feeding = models.TextField(blank=True, null=True, max_length= 500)
    enclosure = models.TextField(blank=True, null=True, max_length= 500)
    temperature = models.TextField(blank=True, null=True, max_length=300)
    sex= models.TextField(blank=True, null=True, max_length= 500)
    male = models.ImageField(blank=True, null=True, upload_to="images")
    female = models.ImageField(blank=True, null=True, upload_to="images")
    breeding = models.TextField(blank=True, null=True, max_length= 500)
    incubation = models.TextField(blank=True, null=True, max_length= 500)
    author = models.ForeignKey(User, related_name='posts', null=False, default=1, on_delete=models.SET_DEFAULT)
    slug = models.SlugField(default="post_detail", null=False, unique=True)
    # created_date = models.DateTimeField(auto_now_add=True, null=True)
    # published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    # views = models.IntegerField(default=0)


    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post_detail', kwargs={'slug': self.slug})
    #
    # def save(self, *args, **kwargs): # new
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)

class AnimalImages(models.Model):
    animalpictures = models.ForeignKey(Animal, related_name="images", on_delete=models.CASCADE)
    images = models.ImageField()
