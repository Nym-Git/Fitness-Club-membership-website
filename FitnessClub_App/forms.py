from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Category
from django.utils import timezone


choices = Category.objects.all().values_list('Category_Field','Category_Field')

# made a empty strings for collect the choises....
choice_list = []
# using loop we fetch data in choise_list to sow-up on html POST-creation page.
for i in choices:
  choice_list.append(i)


# main card...
class cardFORMS(forms.Form):
  HeadingF = forms.CharField(max_length=500,
    widget=forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
    }))


  CategoryF = forms.ChoiceField(choices=choices, 
    widget= forms.Select(attrs={
      'class':'form-control',     
    }))


  Training_periodF= forms.CharField(max_length=50000,
    widget= forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
    }))

  Images= forms.FileField(
    widget=forms.ClearableFileInput(attrs={
      'placeholder': 'Thumbnail',
      'type':'file',  
      'multiple': True
    }))



class cardDetailsFORMS(forms.Form):

  Video = forms.FileField(
    widget=forms.ClearableFileInput(attrs={
      'placeholder': 'Thumbnail',
      'type':'file',  
      'multiple': True
    }))


  SevenF= forms.IntegerField(
    widget= forms.NumberInput(attrs={
      'type' :'number',
      'class':'form-control',
    }))

  OneF= forms.IntegerField(
      widget= forms.NumberInput(attrs={
        'type' :'number',
        'class':'form-control',
      }))

  ThreeMF= forms.IntegerField(
      widget= forms.NumberInput(attrs={
        'type' :'number',
        'class':'form-control',
      }))

  OneYF= forms.IntegerField(
      widget= forms.NumberInput(attrs={
        'type' :'number',
        'class':'form-control',
      }),required=False)

  TwoYF= forms.IntegerField(
      widget= forms.NumberInput(attrs={
        'type' :'number',
        'class':'form-control',
      }),required=False)
  


# sign-up form based class based view 
class SignupFORMS(UserCreationForm):
  email = forms.EmailField(
    widget=forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  first_name= forms.CharField(
    widget= forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  last_name= forms.CharField(
    widget= forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  #For Attribute ordering
  class Meta:
    model = User
    fields = ('username','email','first_name','last_name','password1','password2')

  #For user-name and password designing
  def __init__(self, *args, **kwargs):
    super(SignupFORMS,self).__init__(*args, **kwargs)

    self.fields['username'].widget.attrs['class'] = 'form-control' 
    self.fields['password1'].widget.attrs['class'] = 'form-control' 
    self.fields['password2'].widget.attrs['class'] = 'form-control' 