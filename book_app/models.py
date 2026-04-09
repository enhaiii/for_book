from django.db import models

class Authors(models.Model):
    name = models.CharField('Name', max_length=30)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return f"{self.name}"

class Books(models.Model):
    title = models.CharField('Title', max_length=80)
    description = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField('Relase')
    author = models.ForeignKey(Authors, verbose_name='Authors', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return f"{self.title}"
    