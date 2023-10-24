
from django.shortcuts import render
from .models import Interaction

def index(request):
    interactions = Interaction.objects.all()
    return render(request, 'interaction_tracking/index.html', {'interactions': interactions})

def detail(request, interaction_id):
    interaction = Interaction.objects.get(id=interaction_id)
    return render(request, 'interaction_tracking/detail.html', {'interaction': interaction})

def create(request):
    if request.method == 'POST':
        new_interaction = Interaction(
            contact=request.POST['contact'],
            interaction_type=request.POST['interaction_type'],
            interaction_date=request.POST['interaction_date'],
            notes=request.POST['notes'],
        )
        new_interaction.save()
        return redirect('interaction_tracking:index')
    else:
        return render(request, 'interaction_tracking/create.html')

def update(request, interaction_id):
    interaction = Interaction.objects.get(id=interaction_id)
    if request.method == 'POST':
        interaction.contact = request.POST['contact']
        interaction.interaction_type = request.POST['interaction_type']
        interaction.interaction_date = request.POST['interaction_date']
        interaction.notes = request.POST['notes']
        interaction.save()
        return redirect('interaction_tracking:index')
    else:
        return render(request, 'interaction_tracking/update.html', {'interaction': interaction})

def delete(request, interaction_id):
    interaction = Interaction.objects.get(id=interaction_id)
    interaction.delete()
    return redirect('interaction_tracking:index')
