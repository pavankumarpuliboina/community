from communityapp.models import Category,Question,Answer
from communityapp.forms import QuestionForm

def basefile(request):
	category = Category.objects.all()
	form = QuestionForm(request.POST)
	return {'category':category, 'form':form}