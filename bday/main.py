import datetime, bdaymessages

today = datetime.date.today()
nextBday = datetime.date(2025, 8, 17)

timeDifference = nextBday - today

if today == nextBday:
    print(bdaymessages.randomMsg)
else:
    print(f"My next birthday is {timeDifference} days away!")