from django import forms

from users.models import Client, Restaurant
from foods.models import Product


class EditClientForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(EditClientForm, self).__init__(*args, **kwargs)
        self.fields['endereco'].label = "Endereço"
        self.fields['data_nascimento'].label = "Data de Nascimento"

    class Meta:
        model = Client
        fields = ('endereco', 'data_nascimento', 'celular')


class AddProductRestaurantForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddProductRestaurantForm, self).__init__(*args, **kwargs)
        self.fields['nome'].label = "Produto"
        self.fields['descricao'].label = "Descrição do Produto"
        self.fields['category'].label = "Categoria"
        self.fields['preco'].label = "Preço"

    class Meta:
        model = Product
        fields = (
            'nome', 'descricao', 'category',
            'preco', 'imagem' 
        )

class EditRestaurantForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditRestaurantForm, self).__init__(*args, **kwargs)
        self.fields['nome'].label = "Nome do Restaurante"
        self.fields['descricao'].label = "Descrição"
        self.fields['endereco'].label = "Endereço do Restaurante"
        self.fields['cnpj'].label = "CNPJ"
        self.fields['imagem'].label = "Logotipo"

    class Meta:
        model = Restaurant
        fields = (
            'nome', 'descricao', 'endereco',
            'cnpj', 'imagem'
        )
