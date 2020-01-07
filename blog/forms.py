from django import forms


class EmailPostForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(EmailPostForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'input-field col s6'})
        self.fields['email'].widget.attrs.update({'class': 'input-field col s6'})
        self.fields['to'].widget.attrs.update({'class': 'input-field col s6'})
        self.fields['comments'].widget.attrs.update({'class': 'input-field col s6'})

    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)
