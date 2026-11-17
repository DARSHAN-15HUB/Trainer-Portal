from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentCreateForm

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='signin')
def create_view(request):
  if request.method=='POST':
    form=StudentCreateForm(data=request.POST)

    if form.is_valid():
      student=form.save(commit=False)
      student.trainer=request.user
      student.save()
      return redirect('display')
  else:
    form=StudentCreateForm()
  context={
    'form':form,
    'operation':'+ Create'

  }
  return render(request,'create.html',context)

@login_required(login_url='signin')
def display_view(request):
 
  students=Student.objects.filter(trainer=request.user)
  context={
    'students':students
      
    }
  return render(request,'display.html', context)
@login_required(login_url='signin')

def update_view(request,student_id):
  context={}
  try:
 
   student=Student.objects.get(id=student_id, trainer=request.user)
   context['student']=student
  except Student.DoesNotExist:
    context['id']=student_id
    return render(request,'error.html', context)
  if request.method=='POST':
      form= StudentCreateForm(data=request.POST,instance=student)
      if form.is_valid():
        form.save()
        return redirect('display')
  else:
    existing_data={
      'name':student.name,
      'roll_no':student.roll_no,
      'marks':student.marks,
      'email':student.email,
      'course':student.course,
      'contact':student.contact,
      'address':student.address
    }
    form=StudentCreateForm(initial=existing_data)
  context={
     'form':form,
      'operation':'* Update'

  }

  


 
  return render(request,'update.html', context)

@login_required(login_url='signin')

def delete_view(request,student_id):
  context={}
  try:
 
   student=Student.objects.get(id=student_id, trainer=request.user)
   context['student']=student
  except Student.DoesNotExist:
    context['id']=student_id
    return render(request,'error.html', context)
  if request.method=='POST':
    student.delete()
    return redirect('display')
  
   
  


  return render(request,'delete.html',context)