from django.db import models


from embed_video.fields import EmbedVideoField
class Headerphoto(models.Model):
    image= models.ImageField(upload_to='headerpics')
    @staticmethod
    def get_all_header():
        return Headerphoto.objects.all()
class Aboutme(models.Model):
     image= models.ImageField(upload_to='aboutpic')
     @staticmethod
     def get_all_about():
        return Aboutme.objects.all()
    
class Events(models.Model):
    name=models.CharField(max_length=100)
    image= models.ImageField(upload_to='events')
    @staticmethod
    def get_all_events():
        return Events.objects.all()
class Team(models.Model):
    name=models.CharField(max_length=100)
    work =models.CharField(max_length=100)
    image= models.ImageField(upload_to='team')
    @staticmethod
    def get_all_team():
        return Team.objects.all()
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    @staticmethod
    def get_all_category():
        return Category.objects.all()
class Gallery(models.Model):
    image= models.ImageField(upload_to='pics')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    @staticmethod
    def get_all_photo():
        return Gallery.objects.all()
    @staticmethod
    def get_all_photo_by_id(category_id):
        if category_id:
             return Gallery.objects.filter(category=category_id)
        else :
             return Gallery.get_all_photo()
class Indexphoto(models.Model):
    image= models.ImageField(upload_to='indexpics')   
    @staticmethod
    def get_all_index():
        return Indexphoto.objects.all()
class Contactform (models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField()
    contact = models.CharField(max_length=15)
    message = models.CharField(max_length=300)
class Video(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
    @staticmethod
    def get_all_video():
        return Video.objects.all()
