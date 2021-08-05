from django.contrib import admin
from .models import Gallery ,Headerphoto,Aboutme,Events,Team,Category,Indexphoto,Contactform,Video
from embed_video.admin import AdminVideoMixin
class AdminCategory(admin.ModelAdmin):
    list_display=['name']
class AdminTeam(admin.ModelAdmin):
    list_display=['name']
class AdminEvent(admin.ModelAdmin):
    list_display=['name']
class AdminGallery(admin.ModelAdmin):
    list_display=['image']
class AdminAbout(admin.ModelAdmin):
    list_display=['image']
class AdminHeader(admin.ModelAdmin):
    list_display=['image']
class AdminIndexphoto(admin.ModelAdmin):
    list_display=['image']
class AdminContactform(admin.ModelAdmin):
    list_display=['name','email','contact','message']
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display=['video']
# Register your models here.
admin.site.register(Gallery,AdminGallery)
admin.site.register(Headerphoto,AdminHeader)
admin.site.register(Aboutme,AdminAbout)
admin.site.register(Events,AdminEvent)
admin.site.register(Team,AdminTeam)
admin.site.register(Category, AdminCategory)
admin.site.register(Indexphoto, AdminIndexphoto)
admin.site.register(Contactform, AdminContactform)
admin.site.register(Video, MyModelAdmin)
