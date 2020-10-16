from django import forms
from django.forms import ModelForm 
from communityapp.models import Question,Answer

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['question','description']

class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['answer']

# class CommentForm(forms.ModelForm):
# 	class Meta:
# 		model = Answer
# 		fields = ['comment']

