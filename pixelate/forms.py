# pixelate/forms.py
from django import forms


class URLForm(forms.Form):
    image_url = forms.URLField(label="Image URL", required=True)
