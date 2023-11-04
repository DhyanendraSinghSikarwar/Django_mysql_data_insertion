from django.db import models

# Create your models here.
# class Tf_20230920(models.Model):
#     type = models.CharField(max_length=20)
#     ESP = models.CharField(max_length=255)
#     ENG = models.CharField(max_length=255)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()


#     def __str__(self):
#         return self.name

class Tf_20230920(models.Model):
    id = models.AutoField(primary_key=True)
    ApplicationId = models.IntegerField(null=True)
    ApplicationDate = models.DateTimeField(blank=True, null=True)
    IdRow = models.IntegerField()
    AccountId = models.CharField(max_length=255)
    Balance = models.FloatField()
    Bank = models.CharField(max_length=255)
    transactionDate = models.DateTimeField(blank=True, null=True)
    transactionAmount = models.FloatField()
    transactionClass = models.CharField(max_length=100)
    transactionDescription = models.TextField()
    predictedCategoryDescription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name