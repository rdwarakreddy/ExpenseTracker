from .models import Expense
from django.forms import ModelForm
class ExpenseFrom(ModelForm):
    class Meta:
        model = Expense
        fields = ['name','amount','category']