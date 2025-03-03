from django.db import models

class UniversityCampus(models.Model) :
    campus_name = models.CharField(max_length=80, default="", blank=True, null=False)
    campus_state = models.CharField(max_length=2,default="", blank=True, null=False)
    campus_id = models.IntegerField (default="", blank=True, null=False)


    object = models.Manager ()

    def __str__(self):
        display_name = '{0.campus_name}: {0.campus_state}'
        return display_name.format(self)

    class Meta:
        verbose_name_plural = "University Campus"