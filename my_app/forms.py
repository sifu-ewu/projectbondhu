from django.forms import ModelForm
from .models import Project
from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['doctor','user','title', 'featured_image', 'description',
                  'demo_link', 'source_link']
        labels = {
			'featured_image' : 'Prescript Image',
            'demo_link' : 'Issues',
            'source_link' : 'other Notes'

		
        }    
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})