from django.shortcuts import render,redirect  
from django.contrib import messages 
# Create your views here.
import db.dbclass
import db.dataclass
import os.path
from .forms import *
from .models import *
def admin_login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        request.session['uname']=uname
        pass1=request.POST['pass1']
        
        if uname=="admin" and pass1=="admin":  
            return redirect('/metta_add')
        else:
            messages.success(request,'Invalid user name/Password')
            return render(request,'login.html')
    else:
      #context={'form':form}
      return render(request,'login.html',{})
def metta_add(request):  
    form=MovieForm
    if request.method=='POST':
        frm = MovieForm(request.POST)  
        if frm.is_valid():
            frm.save()
            messages.success(request,'Metta Data Upload Success')
            return redirect('/metta_add')
    context={'form':form}
    return render(request,'metta_add.html',context)
def loadvideo(request,id):
    ob=db.dataclass
    ob.loadvideo(id)
    return redirect('/collection')
def metta_display(request):
    form=Movie.objects.all()
    context={'form':form}
    print(context)
    return render(request,'metta_display.html',context)
def collection(request):
    form=Movie.objects.all()
    context={'form':form}
    print(context)
    return render(request,'collection.html',context)
def movie_review(request):
    form=Movie.objects.all()
    context={'form':form}
    print(context)
    return render(request,'movie_review.html',context)
def movie_status(request,id):
    ob=db.dbclass.dbclass()
    mycursor = ob.mydb.cursor()
    
    s="SELECT * FROM appdata_movie where id="+str(id)
    print(s)
    mycursor.execute(s)
    myresult = mycursor.fetchall()
    if myresult:
        for k in   myresult:
            fname=k[1]
            amt=k[4]
            camt=k[5]
            happy=k[6]
            sad=k[7]
            tot=k[8]
        st=int(amt)-int(camt)
        print("COllection : ",st)
        st1=""
        if st<0:
            st1="Success"
        else:
            st1='Failure'
            
        context={'fname':fname,'amt':amt,'camt':camt,'happy':happy,'sad':sad,'tot':tot,'st':st1}
        return render(request,'movie_status.html',context)
def meta_edit(request,id):
   form=Movie.objects.get(id=id)
   context={'form':form}
   return render(request,'meta_update.html',context)  
def meta_update(request,id):
   form=Movie.objects.get(id=id)
   frm=MovieForm(request.POST,instance=form)
   if frm.is_valid():
         frm.save()
         messages.success(request,'Meta Data Update Successfully')
         return redirect('/metta_display')       
def meta_delete(request,id):
    form=Movie.objects.get(id=id)
    form.delete()  
    messages.success(request,'Meta Data Delete Successfully')  
    return redirect('/metta_display') 
            
