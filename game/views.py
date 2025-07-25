from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'landing.html')

def game(request):
    if 'state' not in request.session:
        # Initialize game state
        request.session['state'] = {
            'left': ['farmer', 'goat', 'wolf', 'cabbage'],
            'right': [],
            'boat_side': 'left',
            'game_over': False,
            'message': None
        }
    
    state = request.session['state']
    
    if request.method == 'POST':
        choice = request.POST.get('choice')
        process_move(state, choice)
        check_game_over(state)
        request.session['state'] = state
        request.session.modified = True  # Ensure session changes are saved
    
    return render(request, 'game_board.html', {'state': state})

def process_move(state, choice):
    current_side = state['boat_side']
    other_side = 'right' if current_side == 'left' else 'left'
    
    if choice == 'alone':
        if 'farmer' not in state[current_side]:
            state['message'] = "Farmer is not on this side."
            return
        state[current_side].remove('farmer')
        state[other_side].append('farmer')
    elif choice in ['goat', 'wolf', 'cabbage']:
        if choice not in state[current_side]:
            state['message'] = f"{choice.capitalize()} is not on this side."
            return
        if 'farmer' not in state[current_side]:
            state['message'] = "Farmer is not on this side."
            return
        state[current_side].remove('farmer')
        state[current_side].remove(choice)
        state[other_side].append('farmer')
        state[other_side].append(choice)
    else:
        state['message'] = "Invalid choice."
        return
    
    state['boat_side'] = other_side
    state['message'] = None  # Clear message after successful move

def check_game_over(state):
    def is_safe(side_list):
        if 'farmer' in side_list:
            return True
        if 'goat' in side_list and 'cabbage' in side_list:
            return False
        if 'wolf' in side_list and 'goat' in side_list:
            return False
        return True
    
    if not is_safe(state['left']):
        state['game_over'] = True
        if 'goat' in state['left'] and 'cabbage' in state['left']:
            state['message'] = "Goat ate cabbage on left!"
        elif 'wolf' in state['left'] and 'goat' in state['left']:
            state['message'] = "Wolf ate goat on left!"
    elif not is_safe(state['right']):
        state['game_over'] = True
        if 'goat' in state['right'] and 'cabbage' in state['right']:
            state['message'] = "Goat ate cabbage on right!"
        elif 'wolf' in state['right'] and 'goat' in state['right']:
            state['message'] = "Wolf ate goat on right!"
    else:
        if len(state['left']) == 0 and len(state['right']) == 4:
            state['game_over'] = True
            state['message'] = "You win!"

def restart(request):
    # Reset the game state
    request.session['state'] = {
        'left': ['farmer', 'goat', 'wolf', 'cabbage'],
        'right': [],
        'boat_side': 'left',
        'game_over': False,
        'message': None
    }
    request.session.modified = True  # Ensure session changes are saved
    return redirect('game')