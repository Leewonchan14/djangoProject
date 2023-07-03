from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question


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