from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    forbidden_words = ['казино',
                       'криптовалюта',
                       'крипта',
                       'биржа',
                       'дешево',
                       'бесплатно',
                       'обман',
                       'полиция',
                       'радар']

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for word in self.forbidden_words:
            if word in self.cleaned_data:
                raise forms.ValidationError('Недопустимое имя')
            else:
                return cleaned_data
