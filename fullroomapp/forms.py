from django import forms

from .models import RoomData

class RoomDataForm(forms.ModelForm):
    class Meta:
        model = RoomData

        fields = [
            'width',
            'length',
            'healthy',
            'sick'
        ]

        widgets = {
            'width' : forms.TextInput (
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Lebar'
                }
            ),
            'length' : forms.TextInput (
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Panjang'
                }
            ),
            'healthy' : forms.TextInput (
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Sehat'
                }
            ),
            'sick' : forms.TextInput (
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Sakit'
                }
            ),
        }