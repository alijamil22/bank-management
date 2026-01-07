from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponseForbidden,HttpResponseNotFound

from .forms import BankForm,BranchForm
from .models import Bank,Branch

# Create your views here.
@login_required
def add_bank(request):
    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            bank = form.save(commit=False)
            bank.owner = request.user
            bank.save()
            return redirect(f'banks/{bank.id}/details/')
        else:
            form = BankForm()
    return render(request,'banks/add_bank.html',{'form':form})

def all_banks(request):
    banks = Bank.objects.all().order_by('name')
    return render(request,'banks/all_banks.html',{'banks':banks})
def bank_details(request):
    try:
        bank = bank.objects.get(id=bank.id)
    except Bank.DoesNotExist:
        return HttpResponseNotFound()
    branches = branches.objects.all()
    return render(request,'banks/banks_details.html',{'bank':bank,'branches':branches})

@login_required    
def add_branch(request,bank_id):
    try:
        bank = bank.objects.get(id=bank_id)
    except Bank.DoesNotExist:
        return HttpResponseNotFound()
    if request.user != bank.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = BranchForm(request.Post)
        if form.is_valid():
            branch = form.save(commit=False)
            branch.bank = bank
            branch.save()
    else:
        form = BranchForm()
    return render(request,'banks/add_branch.html',{'form':form,'branch':branch})
def branch_details(request,branch_id):
    try:
        branch = Branch.objects.get(id = branch_id)
    except Branch.DoesNotExist:
        return HttpResponseNotFound()
    data = {
        'id':branch.id,
        'name':branch.name,
        'transit_number':branch.transit_number,
        'address':branch.address,
        'email':branch.email,
        'capacity':branch.capacity,
        'last_modified':branch.last_modified.isoformat(),
    }
    return JsonResponse(data)
@login_required
def edit_branch(request, branch_id):
    try:
        branch = Branch.objects.get(id=branch_id)
    except Branch.DoesNotExist:
        return HttpResponseNotFound()
    

    if request.user != branch.bank.owner:
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect(f'/banks/branch/{branch.id}/details/')
    else:
        form = BranchForm(instance=branch)
    
    return render(request, 'banks/edit_branch.html', {'form': form, 'branch': branch})