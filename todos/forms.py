from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=200,
                          widget=forms.TextInput(
                          attrs={'class': 'form-control', 'placeholder': 'Enter whatcha tryna do', 'aria-label': 'Todo', 'aria-describedby': 'add-btn'}))