from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=150)
    genre = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    image = models.URLField(max_length=500, blank=True)
    books_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='books')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.FloatField(default=4.5)
    reviews_count = models.IntegerField(default=10)
    description = models.TextField()
    image = models.URLField(max_length=500)
    is_featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Enquiry(models.Model):
    INQUIRY_CHOICES = [
        ('availability', 'Book Availability'),
        ('price', 'Price Inquiry'),
        ('shipping', 'Digital Download Info'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    book_title = models.CharField(max_length=200, blank=True)
    inquiry_type = models.CharField(max_length=50, choices=INQUIRY_CHOICES, default='availability')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enquiry from {self.name} - {self.book_title}"
