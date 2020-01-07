from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import mark_safe
from markdown import markdown


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_total_posts(self):
        tt = Post.objects.filter(category = self.pk).count()
        return tt


# Custom Manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='approved')


# Our Post Model
class Post(models.Model):
    STATUS_CHOICES = (
        ('inreview', 'Inreview'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='my_posts')
    category = models.ForeignKey(Category, on_delete = models.PROTECT, related_name = 'entries', default = '1')
    description = models.TextField()
    keywords = models.CharField(max_length = 400)
    body = RichTextUploadingField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

        # The default manager
    objects = models.Manager()

    # Custom made manager
    approved = PublishedManager()



    def get_absolute_url(self):
        return reverse('post_detail_view', args=[self.slug])


# Our Opportunity Model
class Opportunity(models.Model):
    STATUS_CHOICES = (
        ('inreview', 'Inreview'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    TYPE_CHOICES = (
        ('free', 'Free'),
        ('paid', 'Paid'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='my_opps')
    least_amount= models.CharField(max_length = 40)
    description = models.TextField()
    keywords = models.CharField(max_length = 400)
    body = RichTextUploadingField()
    direct_link = models.CharField(max_length = 200, default = 'https://omborisymons.com')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    types = models.CharField(max_length=10, choices=TYPE_CHOICES, default='free')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

        # The default manager
    objects = models.Manager()

    # Custom made manager
    published = PublishedManager()



    def get_absolute_url(self):
        return reverse('opportunity_detail_view', args=[self.slug])