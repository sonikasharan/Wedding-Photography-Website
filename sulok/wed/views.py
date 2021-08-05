from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from .models import Gallery ,Headerphoto,Aboutme,Events,Team,Category,Indexphoto,Contactform,Video


# Create your views here.
def home(request):
   events= Events.get_all_events()
   index=  Indexphoto.get_all_index()
   header= Headerphoto.get_all_header()
   about= Aboutme.get_all_about()
   obj= Video.get_all_video()
  
   return render(request,'index.html',{'image':index,'head':header,'ab':about,'vv':obj,'event':events})
def about(request):
    teams=Team.get_all_team()
    
    return render(request,'aboutus.html',{'team':teams})
def contact(request):
    if request.method=="POST":
        cont=Contactform()
        name= request.POST['name']
        email= request.POST['email']
        contact1= request.POST['contact']
        message= request.POST['message']
        cont.name= name
        cont.email=email
        cont.contact=contact1
        cont.message=message
        cont.save()
        return render(request,'contact.html')
    else:   
        return render(request,'contact.html')
def gallery(request):
    photo = None
    category=Category.get_all_category()
    categoryid = request.GET.get('i')
    if categoryid:
        photo=Gallery.get_all_photo_by_id(categoryid)
    else:
        photo = Gallery.get_all_photo()
    return render(request,'gallery.html',{'img':photo,'cat':category})
def FAQ(request):
      return render(request,'frequently.html')

