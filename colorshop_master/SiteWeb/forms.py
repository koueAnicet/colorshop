from django import forms


class FormEmail(forms.Form):
    class Meta:
        fields = "__all__"