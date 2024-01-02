import os

for number in range (0, 501, 5):
    percentage = round(number*2/10)
    print(f"LOADING {percentage}%")
    os.system("cls" if os.name == "nt" else "clear")