from django.db import models

class HealthCondition(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='health_conditions/images/')
    facts = models.TextField()
    symptoms = models.TextField()
    causes = models.TextField()
    diagnosis = models.TextField()
    treatments = models.TextField()
    complications = models.TextField()
    prevention = models.TextField()
    nutrition = models.TextField()
    alphabet = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title