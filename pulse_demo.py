import random

def pulse_analysis():
    bpm = random.randint(60,110)
    print("Ölçülen Nabız:", bpm)

    if bpm < 50:
        print("Bradikardi Riski")
    elif 60 <= bpm <= 100:
        print("Normal")
    else:
        print("Taşikardi Riski")

pulse_analysis()
