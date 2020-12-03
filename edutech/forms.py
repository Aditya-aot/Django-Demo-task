from django import forms
from django.forms import ModelForm
from .models import Question_Asked  , Answer_model

class Question_Form(ModelForm):
    content =  forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Write your topic "}))
    message  =   forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Write your Message"}))
    # images = forms.ImageField()
    # null = True, blank = True

    class Meta:
        model = Question_Asked
        fields = [
            'content' ,
            'message' ,
 ]

class Answer_Form(ModelForm) :
    answer  =  forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Write your topic "}))
    # message  =   forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Write your Message"}))
    # images = forms.ImageField()
    # null = True, blank = True

    class Meta:
        model = Answer_model
        fields = [
            'answer' ,
         
 ]

