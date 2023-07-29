from django.shortcuts import render,redirect
from .models import Expense
from .forms import ExpenseFrom
from django.db.models import Sum
import datetime
# Create your views here.
def index(request):
    if request.method == "POST":
        expense = ExpenseFrom(request.POST)
        if expense.is_valid():
            expense.save()
    expenses = Expense.objects.all()
    total_expense = expenses.aggregate(Sum('amount'))
    categorical_sum = Expense.objects.filter().values('category').order_by('category').annotate(sum=Sum('amount'))
    print(categorical_sum)
    expense_form = ExpenseFrom()
    return render(request,'myapp/index.html',{'expense_form':expense_form,'expenses':expenses,'total_expense':total_expense,'categorical_sum':categorical_sum})
def edit(request,id):
    expense = Expense.objects.get(id=id)
    expense_form = ExpenseFrom(instance=expense)
    if request.method == "POST":
        expense = Expense.objects.get(id=id)
        form = ExpenseFrom(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'myapp/edit.html',{'expense_form':expense_form})

def delete(request,id):
    expense = Expense.objects.get(id=id)
    if request.method == "POST":
        expense.delete()
        return redirect('index')
    return render(request,'myapp/delete.html',{'expense':expense})