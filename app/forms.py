from django import forms
from django.forms import ModelForm, inlineformset_factory
from app.utils import generate_bootstrap_widgets_for_all_fields

from . import (
    models
)


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # field.widget.attrs['class'] = 'form-control'
            if field_name == 'phone' or field_name == 'telefone':
                field.widget.attrs['class'] = 'form-control telefone phone'
            if field_name == 'cep' or field_name == 'postalcode':
                field.widget.attrs['class'] = 'form-control cep'


class MensagemForm(BaseForm, ModelForm):
    class Meta:
        model = models.Mensagem
        fields = ("id", "nome", "email", "nome_empresa", "telefone", "assunto", "mensagem")
        widgets = generate_bootstrap_widgets_for_all_fields(models.Mensagem)

    def __init__(self, *args, **kwargs):
        super(MensagemForm, self).__init__(*args, **kwargs)
