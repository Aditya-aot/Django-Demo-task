from django.shortcuts import render
from .models import Question_Asked , Answer_model
from .forms import Question_Form ,Answer_Form
from django.contrib.auth.models import  User, auth
from django.http import HttpResponseRedirect
# Create your views here.

def home(request) :
    return render(request, 'edutech/home.html')

def send_answer(request) :
    question = Question_Asked.objects.all()

    context = {'ques':question[::-1],
                }
    return render(request, 'edutech/answer.html', context)

def ask_question(request) :
    question = Question_Asked.objects.all()
    username = request.GET.get('username')
    form = Question_Form(request.POST, request.FILES)
    if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user or None
            obj.save()
            form=Question_Form()
            # form=form.cleaned_data
    user_question = question.filter(user__username__iexact = username)

    context = {'ques':user_question[::-1],
                'form':form ,
                }
    return render(request, 'edutech/question.html' , context)        


def answer_post(request, pk) :
    form = Answer_Form()
    question = Question_Asked.objects.get(id= pk)
    username = request.GET.get('username')
    ans = question.answers.all()

    form.instance.user = request.user

    if request.method == 'POST':
        form = Answer_Form(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user or None
        obj.chat = Question_Asked.objects.get(id= pk) or None
        obj.save()
        form=Answer_Form()    
    context = {'question': question ,
               'ans': ans[::-1] ,
               'form':form ,
               }

    return render(request, 'edutech/post_answer.html' ,context)