from django import forms
from .models import Student
class StudentCreateForm(forms.ModelForm):
  class Meta:
     model=Student
     fields=['name','roll_no','marks','email','course','contact','address']
     widgets={
        'name':forms.TextInput(
    attrs={
      'placeholder':'Enter Student Name'
    }
  ),
  'roll_no':forms.NumberInput(
    attrs={
      'placeholder':'Enter Student roll_no'
    }
  ),
  'marks':forms.NumberInput(
    attrs={
      'placeholder':'Enter Student Marks'
    }
  ),
  'email':forms.EmailInput(
    attrs={
      'placeholder':'Enter Student Email'
    }
  ),
  'course':forms.TextInput(
    attrs={
      'placeholder':'Enter Student Course'
    }
  ),
  'contact':forms.TextInput(                                                                                                                                  
    attrs={
      'placeholder':'Enter Student Contact'
    }
  ),
  'address':forms.Textarea(
    attrs={
      'placeholder':'Enter Student Adddress',
      'rows':10,
      'cols':50                                                                                                                                         
    }
  )
        
     }
 
  
  
  
                                                                                                                                                                                                                         
  def clean_roll_no(self):
    roll_no=self.cleaned_data['roll_no']
    print("VALIDATING ROLL NUMBER:", roll_no)
    if roll_no < 0:
      raise forms.ValidationError("Roll No Can't Be Negative")
    return roll_no
  def clean_marks(self):
      marks=self.cleaned_data['marks']
      if marks < 0 or marks > 100:
        raise forms.ValidationError("Marks must be in the range of 0 to 100")
      return marks
  def clean_contact(self):
        contact=self.cleaned_data['contact']                                                                                                            
        if len(contact)!=10:
          raise forms.ValidationError("Marks must contain exactly 10 digits")
        return contact
 
                                                                                                                                                                                                            
  def create(self,user):
     student=Student.objects.create(trainer=user,**self.cleaned_data)
     return student
  def update(self,instance):
     instance.name=self.cleaned_data.get('name',instance.name)
     instance.roll_no=self.cleaned_data.get('roll_no',instance.roll_no)
     instance.marks=self.cleaned_data.get('marks',instance.marks)
     instance.email=self.cleaned_data.get('email',instance.email)
     instance.course=self.cleaned_data.get('course',instance.course)
     instance.contact=self.cleaned_data.get('contact',instance.contact)
     instance.address=self.cleaned_data.get('address',instance.address)
     instance.save()
     return instance