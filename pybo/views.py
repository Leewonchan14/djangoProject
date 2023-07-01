from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Question, Answer
from .forms import QuestionForm,AnswerForm


def index(request: WSGIRequest) -> render:
    page = request.GET.get('page', '1')  # 페이지
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)


def detail(request: WSGIRequest, question_id) -> render:
    question = get_object_or_404(Question, pk=question_id)
    anwser_list = question.answer_set.all()
    context = {'question': question, "anwser_list": anwser_list}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request: WSGIRequest, question_id):

    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            #commit = False로 create_date속성이 입력안돼도 Question객체를 반환함
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

