def fortune():
    """
    Returns a random fortune cookie message.
    """
    import random

    fortunes = [
        "You will have a great day!",
        "Good things are coming your way.",
        "You will find success in your endeavors.",
        "A surprise is waiting for you.",
        "You will meet someone special soon.",
        "Your hard work will pay off.",
        "You will receive good news soon.",
        "A new opportunity is on the horizon.",
        "You will make a new friend.",
        "You will find joy in the little things."
    ]

    print(random.choice(fortunes))

fortune()