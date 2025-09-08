from django.db import models # type: ignore

class books(models.Model):
    GENRE_CHOICES = [
        ("Fiction", "Fiction"),
        ("Non-fiction", "Non-fiction"),
        ("Science", "Science"),
        ("History", "History"),
    ]

    name = models.CharField(max_length=200, verbose_name="Book Title")
    description = models.TextField(help_text="Write a short description")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, default="Fiction")
    image = models.ImageField(upload_to="books/", blank=True, null=True)
    published_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.name



