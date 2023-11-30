"""Forms of the project."""
from django import forms
from .models import Thing

# Create your forms here.
class ThingForm(forms.ModelForm):
    """Form for the Thing model."""
    name = forms.CharField(label='Name', max_length=35, widget=forms.TextInput())
    description = forms.CharField(label='Description', max_length=120, widget=forms.Textarea())
    quantity = forms.IntegerField(label='Quantity', min_value=0, max_value=50, widget=forms.NumberInput())

    class Meta:
        """Meta class."""
        model = Thing
        fields = ['name', 'description', 'quantity']

    def clean(self):
        """Clean."""
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        quantity = cleaned_data.get('quantity')
        if not name and not description and not quantity:
            raise forms.ValidationError('You have to write something!')
    
    def save(self, commit=True):
        """Save."""
        thing = Thing.objects.create(
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],
            quantity=self.cleaned_data['quantity']
        )
        return thing
    


