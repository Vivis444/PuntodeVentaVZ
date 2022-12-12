from datetime import datetime

from django import forms
from django.forms import ModelForm

from core.model1.models import Category, Product, Client, Sale
import logging


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'desc': forms.Textarea(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }

    def save(self, commit=True):
        logging.basicConfig(filename='requirements/logs.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG,)
        logging.debug('Started')
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
            logging.warning('Datos Invalidos de la Categoria!')
        logging.info("Validando la Categoria")
        logging.debug('Finished')
        return data
    


class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'cat': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
        }

    def save(self, commit=True):
        logging.basicConfig(filename='requirements/logs.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG,)
        logging.debug('Started')
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
            logging.warning('Datos Invalidos del Producto!')
        logging.info("Validando el Producto")
        logging.debug('Finished')
        return data


class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'names': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
            'surnames': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'dni': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su dni',
                }
            ),
            'date_birthday': forms.DateInput(format='%Y-%m-%d',
                                       attrs={
                                           'value': datetime.now().strftime('%Y-%m-%d'),
                                       }
                                       ),
            'address': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su dirección',
                }
            ),
            'gender': forms.Select()
        }

    def save(self, commit=True):
        logging.basicConfig(filename='requirements/logs.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG,)
        logging.debug('Started')
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
            logging.warning('Datos Invalidos del cliente!')
        logging.info("Validando el cliente")
        logging.debug('Finished')
        return data

    # def clean(self):
    #     cleaned = super().clean()
    #     if len(cleaned['name']) <= 50:
    #         raise forms.ValidationError('Validacion xxx')
    #         # self.add_error('name', 'Le faltan caracteres')
    #     return cleaned


class TestForm(forms.Form):
    categories = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    products = forms.ModelChoiceField(queryset=Product.objects.none(), widget=forms.Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    # search = CharField(widget=TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Ingrese una descripción'
    # }))

    search = forms.ModelChoiceField(queryset=Product.objects.none(), widget=forms.Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))


class SaleForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cli'].queryset = Client.objects.none()

    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'cli': forms.Select(attrs={
                'class': 'custom-select select2',
                # 'style': 'width: 100%'
            }),
            'date_joined': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'date_joined',
                    'data-target': '#date_joined',
                    'data-toggle': 'datetimepicker'
                }
            ),
            'iva': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'subtotal': forms.TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            'total': forms.TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            })
        }
