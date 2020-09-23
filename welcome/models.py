from django.db import models

class Element(model.Model):
  element_nom = models.CharField(max_length=50)
