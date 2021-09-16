from django.forms import ModelForm
from app.models import Paciente


class PacienteForm (ModelForm):
    class Meta:
        model = Paciente
        fields = ['Nome', 'CPF', 'Cirurgia']
