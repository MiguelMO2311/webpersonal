from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link = models.URLField(verbose_name="Dirección Web", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title

class Diploma(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción", blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="diplomas")
    date = models.DateField(null=True, blank=True, verbose_name="Fecha de obtención")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "diploma"
        verbose_name_plural = "diplomas"
        ordering = ["-date", "-created"]

    def __str__(self):
        return self.title
