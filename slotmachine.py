import random

symbols = ['🍒',' 🍇', '🍉', '7️⃣']

results = [] 

def play():
    game = input("Do you wish to keep playing? (y/n) ")
    if game.lower() == "y": 
        current_results = random.choices(symbols, k=3)
        print(" |".join(current_results))
        if current_results == ['7️⃣', '7️⃣', '7️⃣']:
            print("Jackpot!")
        else:
            pass 
        return current_results 
    else:
        print("See you next time.")
        return None 

while True:
    results = play()

    if results is None: 
        break
    
    if results == ['7️⃣', '7️⃣', '7️⃣']:
        break 

print("Thanks for playing!") 