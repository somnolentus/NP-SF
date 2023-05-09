from django import forms
from django.contrib.auth.models import Group
from allauth.account.forms import SignupForm
from .models import Post, Author, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['type', 'category', 'title', 'text']
        labels = {
            'type': 'Post type',
            'category': 'Categories',
            'title': 'Title',
            'text': 'Text'
        }

        widgets = {
            'type': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Enter title...'}),
            'text': forms.Textarea(attrs={'class': 'form-control',
                                          'placeholder': 'Enter text...'}),
            'category': forms.SelectMultiple(attrs={'class': 'form-control', 'size': 3}),
        }

class CustomSignupForm(SignupForm):
    become_author = forms.BooleanField(label='Become author', required=False,
                            widget=forms.CheckboxInput(attrs={'class': 'form-check-input',
                                                              'type': 'checkbox'}))

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        if self.cleaned_data['become_author']:
            authors_group = Group.objects.get(name='authors')
            authors_group.user_set.add(user)
            Author.objects.create(author_user=user)
        return user


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class ContactForm(forms.Form):
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Enter subject', 'required': True}))
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10,
                                                        'placeholder': 'Enter text...',
                                                        'required': True}))