from django.http import Http404, HttpResponse # el import render, lo deja obsoleto.
from django.template import loader  # el import render, lo deja obsoleto.
from polls.models import Question
from django.shortcuts import get_object_or_404, render


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def pre_index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # Es un atajo, mas no necesita un mensaje pues irá al 404
    return render(request, 'polls/detail.html', {'question': question})

def pre_dos_detail(request, question_id):
    print('en details [request][question_id][%s][%s]' % (request, question_id))
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist (Error personalizado)")
    return render(request, 'polls/detail.html', {'question': question})

def pre_uno_detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
