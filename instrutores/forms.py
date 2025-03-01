from django import forms

class InstrutoresForm(forms.Form):
    rg = forms.CharField(max_length=15, required=False, help_text="Informe o RG do Instrutor")
    nome = forms.CharField(max_length= 70, required=False, help_text="Informe o nome do Instrutor")
    data_Nascimento = forms.DateField(required=True, help_text="Informe a data de nascimento do Instrutor")
    telefone = forms.CharField(max_length=9, required=False, help_text="Informe o Número de telefone do Intrutor")
    ddd = forms.CharField(max_length=3, required=False, help_text="Informe o Número de ddd do Intrutor")
    codigo_titulo = forms.IntegerField(required=True, help_text="Informe o Título do Instrutor")
    