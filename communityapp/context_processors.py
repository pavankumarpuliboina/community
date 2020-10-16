from communityapp.models import Category,Question,Answer
from communityapp.forms import QuestionForm

def basefile(request):
	categorys = Category.objects.all()
	form = QuestionForm(request.POST)
	return {'categorys':categorys, 'form':form}