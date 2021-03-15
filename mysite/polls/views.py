from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.http import Http404

# from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list,
    }
    # return HttpResponse(output)
    # return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    # response = "you are looking at question %s."
    try:
        question = Question.objects.get(pk=question_id)
        context = {
            'question':question,
        }
    except Question.DoesNotExist:
        raise Http404("Question dose not exist")
    # return HttpResponse(response % question_id)
    return render(request,'polls/detail.html',context)

def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    response = "You are voting on question %s."
    return HttpResponse(response % question_id)