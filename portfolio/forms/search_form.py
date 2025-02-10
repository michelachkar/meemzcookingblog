from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(max_length=150,
                             widget=forms.TextInput(
                                 attrs={'class': 'search__input', 'placeholder': 'Type Words Then Enter'}),
                             label=''
                             )
