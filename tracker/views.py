from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .models import Counter
from .forms import CountForm

def all_counters(request):
    if request.user.is_anonymous == True:
        return render(request, 'registration/login.html', {'user': 'anonymous'})
    else:
        counters = Counter.objects.filter(author=request.user)
        return render(request, 'tracker/all_counters.html', {'counters': counters, 'user': request.user.username})

@login_required
def counter_edit(request, pk):
    count = get_object_or_404(Counter, pk=pk)
    if request.method == "POST":
        form = CountForm(request.POST, instance=count)
        if form.is_valid():
            count = form.save(commit=False)
            count.author = request.user
            count.save()
            return redirect('/', pk=count.pk)
    else:
        form = CountForm(instance=count)
    return render(request, 'tracker/counter.html', {'form': form, 'count': count})

@login_required
def new_counter(request):
    if request.method == "POST":
        form = CountForm(request.POST)
        if form.is_valid():
            count = form.save(commit=False)
            count.author = request.user
            count.save()
            return redirect('/')
    else:
        form = CountForm()
    return render(request, 'tracker/new_counter.html', {'form': form})

@login_required
def counter_remove(request, pk):
    count = get_object_or_404(Counter, pk=pk)
    count.delete()
    return redirect('all_counters')

def register(request):
    args={}
    args.update(csrf(request))
    args['form']=UserCreationForm()
    if request.POST:
        newuser_form=UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()

            return redirect('/')
        else:
            args['form']=newuser_form
    return render(request, 'registration/register.html', args)