from django.db import models

# Create your models here.
class Profile(models.Model):
    user = pass
    id_user = pass
    bio = pass
    profileImg = pass
    loc = pass

    def __str__(self):
        return self.id_user
