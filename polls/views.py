from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# from django.http import Http404


# def index(request):
#     """Polls Page"""
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template_path = "polls/index.html"
#     context = {"latest_question_list": latest_question_list}
#     return render(request, template_path, context)


# def detail(request, question_id):
#     """View Details"""
#     # try:
#     #     get_question = Question.objects.get(pk=question_id)
#     #     template_path = 'polls/detail.html'
#     #     context = {"question": get_question}
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     get_question_detail = get_object_or_404(Question, pk=question_id)
#     template_path = 'polls/detail.html'
#     context = {"question": get_question_detail}
#     return render(request, template_path, context)


# def results(request, question_id):
#     """View Results"""
#     question = get_object_or_404(Question, pk = question_id)
#     template = 'polls/results.html'
#     context = {"question": question}
#     return render(request,template,context)

class IndexView(generic.ListView):
    """Get Index View"""
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    """Get Details View"""
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Get Questions in the present o past time
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    """"Get Results View"""
    model = Question
    template_name = "polls/results.html"


def votes(request, question_id):
    """"View votes"""
    question = get_object_or_404(Question, pk=question_id)
    template_path = 'polls/detail.html'
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, template_path, {
               "question": question, "error_message": "You didn't select a choice."})
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
