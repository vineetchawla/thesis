from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
            'latest_question_list' : latest_question_list
            }
    return render(request, "polls/views.html", context)
    #return HttpResponse("Hello World!, this will come for url /view")

def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist :
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {'question' : question})
    #return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)

