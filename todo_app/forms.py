from django import forms
from .models import TodoList
from django.utils.translation import gettext_lazy as _

class TodoListForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        label='期限日',
        widget=forms.TextInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = TodoList
        fields = ['title', 'due_date', 'category', 'priority', 'comment',]
        labels = {
            'title': _('タイトル'),
            'due_date': _('期限日'),
            'category': _('カテゴリー'),
            'priority': _('優先度'),
            'comment': _('コメント'),
        }
