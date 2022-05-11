from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from pkg_resources import require
from .models import Choice, Question
from django.views import generic


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]

#     # template = loader.get_template('polls/index.html')

#     context = {
#         'latest_question_list':  latest_question_list
#     }

#     # return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context)


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)

#     context = {
#         'question': question
#     }

#     return render(request, 'polls/detail.html', context)

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {
#         question: question
#     })

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))

    return HttpResponse("You're voting on question %s" % question_id)
