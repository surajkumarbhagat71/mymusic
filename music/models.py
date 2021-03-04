from django.db import models

# Create your models here.


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Music(models.Model):
    music_id = models.AutoField(primary_key=True)
    song_title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='image/' , blank=True, null=True)
    song = models.FileField(upload_to='song/' ,max_length=500)
    song_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    song_movie = models.CharField(max_length=300)
    song_singer = models.CharField(max_length=200)

    def __str__(self):
        return self.song_title



