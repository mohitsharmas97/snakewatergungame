# app.py
from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def game():
    result = None
    user_choice = None
    computer_choice = None
    
    if request.method == 'POST':
        # Get user's choice from form
        user_choice_str = request.form.get('choice')
        
        # Dictionaries for conversion
        choice_dict = {"s": 1, "w": -1, "g": 0}
        reverse_dict = {1: "Snake", -1: "Water", 0: "Gun"}
        
        # Generate computer's choice
        computer = random.choice([-1, 0, 1])
        you = choice_dict[user_choice_str]
        
        # Store choices for display
        user_choice = reverse_dict[you]
        computer_choice = reverse_dict[computer]
        
        # Game logic
        if computer == you:
            result = "It's a Draw!"
        elif (computer == -1 and you == 1) or \
             (computer == 1 and you == 0) or \
             (computer == 0 and you == -1):
            result = "You Win! 🎉"
        else:
            result = "You Lose! 😢"
    
    return render_template('game.html', result=result, 
                         user_choice=user_choice, 
                         computer_choice=computer_choice)

if __name__ == '__main__':
    app.run(debug=True)