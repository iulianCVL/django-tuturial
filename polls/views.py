from django.shortcuts import render
from polls.models import Question

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def content(request):
    return HttpResponse("Incercam sa construim un site")

def conclusion(request):
    return HttpResponse("Concluzii finale")



def detail(request, question_id):
    exists = Question.objects.filter(id=question_id).exists()
    if exists:
        return HttpResponse("You're looking at question %s." % question_id)
    else:
        return HttpResponse("Nu exista %s." % question_id)


def results(request, question_id):
    exists = Question.objects.filter(id=question_id).exists()
    if exists:
        response = "You're looking at the results of question %s."
    else:
        response = "nu exista &s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    exists = Question.objects.filter(id=question_id).exists()
    if exists:
        return HttpResponse("You're voting on question %s." % question_id)
    else:
        return HttpResponse("Nu exista %s." % question_id)
    

def top_five_questions(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
