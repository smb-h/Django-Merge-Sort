from django.forms import ModelForm
from django import forms
from .models import Tree


class InputForm(ModelForm):
    class Meta:
        model = Tree
        fields = ['root',]
        # InputLabel = forms.CharField(label='Input', max_length=100)
        # InData = forms.CharField(widget=forms.Textarea)


class OutputForm(forms.Form):

    # OutputLabel = forms.CharField(label='Output', max_length=1000)
    # OutData = forms.Textarea()
    Result = forms.CharField(widget=forms.Textarea)


    # class Meta:
    #     model = Author
    #     fields = ('name', 'title', 'birth_date')
    #     labels = {
    #         'name': _('Writer'),
    #     }
    #     help_texts = {
    #         'name': _('Some useful help text.'),
    #     }
    #     error_messages = {
    #         'name': {
    #             'max_length': _("This writer's name is too long."),
    #         },
    #     }
