from django import forms
from .models import Bug, BugScreenshot

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['title', 'description', 'project', 'priority', 'status']


class BugScreenshotForm(forms.ModelForm):
    class Meta:
        model = BugScreenshot
        fields = ['image']

        def clean_image(self):
            image = self.cleaned_data.get('image')
            if image:
                if not image.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                    raise forms.ValidationError("Only .jpg, .jpeg, and .png files are allowed.")
            return image
