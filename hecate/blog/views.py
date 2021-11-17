from django.shortcuts import render,redirect
from .forms import AnswerForm
from .models import Answer, Question

# Create your views here.
def allquestions(request):
    questions =Question.objects.all()
    return render(request,'blog/ques.html',{'questions':questions})

def askaquestion(request):
    if request.method == 'POST':
        question=request.POST.get('question')
        new_question = Question(question=question)
        new_question.save()
        return redirect('/blog/')
    
    return redirect('/blog/')

def answeraquestion(request,pk):
    form=AnswerForm()
    if request.method == 'POST':
        answer=request.POST.get('answer')
        new_answer = Answer(answer=answer,question=Question.objects.get(id=pk))
        new_answer.save()
        return redirect(f'/blog/allanswers/{pk}')
    return render(request,'blog/answeraquestion.html',{'form':form, 'pk':pk,'question':Question.objects.get(id=pk)})

def allanswers(request,pk):
    answers=Answer.objects.filter(question=Question.objects.get(id=pk))
    return render(request,'blog/allanswerspage.html',{'answers':answers,'question':Question.objects.get(id=pk)})
