from django import forms
from .models import Tienda, Ciudad, Region

class TiendaForm(forms.ModelForm):
    class Meta:
        model = Tienda
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ciudad'].queryset = Ciudad.objects.none()

        if 'region' in self.data:
            try:
                country_id = int(self.data.get('region'))
                self.fields['ciudad'].queryset = Ciudad.objects.filter(idCiudad=country_id).order_by('descripcion')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['ciudad'].queryset = self.instance.region.ciudad_set.order_by('descipcion')

        