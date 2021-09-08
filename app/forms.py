from django.forms import ModelForm
from app.models import Pacientes

class PacientesForm(ModelForm):
     class Meta:
         model = Pacientes
         fields = ['Nome', 'CPF', 'Cirurgia']
