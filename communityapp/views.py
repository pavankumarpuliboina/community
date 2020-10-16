from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect,reverse
from . models import Category,Question,Answer
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.db.models import Q
from django.contrib import messages
from . forms import AnswerForm,QuestionForm
from django.core.paginator import Paginator

# Create your views here.
def home(request):
	category = Category.objects.all()
	return render(request, 'index.html', {'category':category})

def index(request,slug):
	categorys = Category.objects.all()
	category = Category.objects.get(slug=slug)
	separatecategory = Category.objects.filter(slug = slug)

	question_list = category.question_set.all()
	paginator = Paginator(question_list, 5)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	form = QuestionForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			question = request.POST['question']
			description = request.POST['description']
			form.instance.category = category
			form = form.save()
			return HttpResponseRedirect(reverse('communityapp:detail', kwargs={'slug': slug}))
		else:
			form = QuestionForm()

	return render(request, 'community-main.html', {'category':category, 'categorys':categorys, 'separatecategory':separatecategory, 'page_obj':page_obj, 'form':form})




def search(request):
	if request.method == 'POST':
		findingquestion = request.POST['findquestion']

		if findingquestion:
			match = Question.objects.filter(Q(question__icontains=findingquestion))
			if match:
				return render(request, 'search.html', {'smatch':match})
			else:
				messages.error(request, 'Result Not Found')
		else:
			return HttpResponseRedirect('/search/')

	return render(request, 'search.html')


def questiondetail(request,slug):
	question = Question.objects.get(slug = slug)
	answers = Answer.objects.filter(question = question)
	q = get_object_or_404(Question,slug = slug)
	answerform = AnswerForm(request.POST)
	if request.method == 'POST':
		if answerform.is_valid():
			answer = answerform.save(commit = False)
			answer.question = q
			answer.user = request.user
			answer.save()
			return redirect('communityapp:question-detail',slug = q.slug)
		else:
			answerform = AnswerForm()
	return render(request, 'community.html', {'question':question, 'answers':answers, 'answerform':answerform})





# def questiondetail(request,slug):
# 	question = Question.objects.get(slug = slug)
# 	answers = Answer.objects.filter(question = question)
# 	q = get_object_or_404(Question,slug = slug)



# 	form = AnswerForm(request.POST)
# 	if request.method == 'POST':
# 		#answerdata = AnswerForm(request.POST)
# 		if form.is_valid():
# 			answer = form.cleaned_data['answer']
# 			answer = form.save(commit = False)
# 			answer.question = q
# 			answer.user = request.user
# 			answer.save()
# 			return redirect('communityapp:question-detail',slug = q.slug)
# 		else:
# 			form = AnswerForm()


# 	commented_answer = Answer.objects.get(slug = slug)
# 	comments = Answer.objects.filter(comment = comment)
# 	s = get_object_or_404(Answer,slug = slug)

# 	commentform = CommentForm(request.POST)
# 	if request.method == 'POST':
# 		if commentform.is_valid():
# 			comment = form.cleaned_data['comment']
# 			comment =commentform.save(commit = False)
# 			comments.answer = s
# 			comment.user = request.user
# 			comment.save()
# 			return redirect('communityapp:question-detail',slug = s.slug)
# 		else:
# 			commentform = CommentForm



# 	return render(request, 'community.html', {'question':question,'form':form, 'answers':answers, 'commentform':commentform})

