from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=False,null=False)
    description = models.TextField(blank=False,null=False)
    content = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    time_to_read=models.CharField(max_length=100,blank=False,null=False)
    slug=models.SlugField(unique=True,blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Posts'
        verbose_name = 'Post'


    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)


class Comments(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name_plural = 'Comments'
        verbose_name = 'Comment'

