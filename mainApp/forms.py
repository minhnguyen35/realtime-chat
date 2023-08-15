from django import forms


class NameForm(forms.Form):
    user_name = forms.CharField(label="User Name", max_length=30)
    room_name = forms.CharField(label="Room Name", max_length=40)