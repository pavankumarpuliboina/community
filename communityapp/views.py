from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect,reverse
from . models import Category,Question,Answer
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.db.models import Q
from django.contrib import messages
from . forms import AnswerForm,QuestionForm
from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.

def index(request):
	category = Category.objects.all()
	question = Question.objects.all()[::-1]
	#filtercategory = Category.objects.get(slug=slug)
	#separatecategory = Category.objects.filter(slug = slug)

	# question_list = categorys.question_set.all()
	paginator = Paginator(question, 1)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	# form = QuestionForm()
	# if request.method == 'POST':
	# 	form = QuestionForm(request.POST)
	# 	if form.is_valid():
	# 		question = request.POST['question']
	# 		description = request.POST['description']
	# 		form.instance.category = category
	# 		form = form.save()
	# 		return HttpResponseRedirect(reverse('communityapp:detail', kwargs={'slug': slug}))
	# 	else:
	# 		form = QuestionForm()

	return render(request, 'community-main.html', { 'category':category, 'question':question, 'page_obj':page_obj })


def categorydetail(request,slug):
	category = Category.objects.all()
	filtercategory = Category.objects.get(slug = slug)
	question_list = filtercategory.question_set.all()[::-1]
	return render(request, 'category-filter.html',{'question_list':question_list, 'filtercategory':filtercategory, 'category':category})


def questiondetail(request,slug):
	question = Question.objects.get(slug = slug)
	answers = Answer.objects.filter(question = question)
	recent = [i.question for i in Category.objects.get(category = question.category).question_set.all()][::-1][:5]
	q = get_object_or_404(Question,slug = slug)
	related_questions = Question.objects.all()[::-1]

	# answerform = AnswerForm(request.POST)
	# if request.method == 'POST':
	# 	if answerform.is_valid():
	# 		answer = answerform.save(commit = False)
	# 		answer.question = q
	# 		answer.user = request.user
	# 		answer.save()
	# 		return redirect('communityapp:question-detail',slug = q.slug)
	# 	else:
	# 		answerform = AnswerForm()
	return render(request, 'community.html', {'question':question, 'answers':answers, 'recent':recent, 'related_questions':related_questions})



# def search(request):
# 	if request.method == 'POST':
# 		findingquestion = request.POST['findquestion']

# 		if findingquestion:
# 			match = Question.objects.filter(Q(question__icontains=findingquestion))
# 			if match:
# 				return render(request, 'search.html', {'smatch':match})
# 			else:
# 				messages.error(request, 'Result Not Found')
# 		else:
# 			return HttpResponseRedirect('/search/')

# 	return render(request, 'search.html')


def upvote(request):
	if request.method == "GET":
		uv = request.GET.get('uo',None)
		uo = Question.objects.get(id=uv)
		uo.upvote = uo.upvote+1
		uo.save()
		data = {'uo': uo.upvote}
	return JsonResponse(data)

def downvote(request):
	if request.method == "GET":
		dv = request.GET.get('dov',None)
		dov = Question.objects.get(id=dv)
		dov.downvote = dov.downvote-1
		dov.save()
		data = {'dov': dov.downvote}
		print(data)
	return JsonResponse(data)