from django.shortcuts import render
from .models import Bond


# Create your views here.
def home(request):
    return render(request, 'bonds/home.html')

from django.shortcuts import render
from .models import Bond

def search_bond(request):
    context = {}

    if request.method == 'POST':
        bond_number = request.POST.get('bond_number')
        denomination = request.POST.get('denomination')
        
        bond = Bond.objects.filter(bond_number=bond_number, denomination=denomination).first()
        
        if bond:
            context = {
                'message': 'Congratulations, you won!',
                'bond_number': bond.bond_number,
                'denomination': bond.denomination,
                'draw_date': bond.draw_date,
                'prize_won': bond.prize_won
            }
        else:
            context = {
                'message': 'Sorry, you do not win. Better luck next time!'
            }
    
    return render(request, 'bonds/search.html', context)
