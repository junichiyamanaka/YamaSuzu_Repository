from django import forms

class KeibaForm(forms.Form):
    date = forms.DateField(label='date')
    data = [
        ('one',    '第１Ｒ'),
        ('two',    '第２Ｒ'),
        ('three',  '第３Ｒ'),
        ('four',   '第４Ｒ'),
        ('five',   '第５Ｒ'),
        ('six',    '第６Ｒ'),
        ('seven',  '第７Ｒ'),
        ('eight',  '第８Ｒ'),
        ('nine',   '第９Ｒ'),
        ('ten',    '第１０Ｒ'),
        ('eleven', '第１１Ｒ'),
        ('twelve', '第１２Ｒ')
    ]
    choice = forms.ChoiceField(label='Choice', choices=data)
    #age = forms.IntegerField(label='age')

class KeibaCreateForm(forms.Form):
    horse = forms.CharField(label='Horse')
    f_horse = forms.CharField(label='F_horse')
    m_horse = forms.CharField(label='M_horse')
    ff_horse = forms.CharField(label='Ff_horse')
    fm_horse = forms.CharField(label='Fm_horse')
    mf_horse = forms.CharField(label='Mf_horse')
    mm_horse = forms.CharField(label='Mm_horse')
    age = forms.IntegerField(label='Age')
