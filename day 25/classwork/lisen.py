guess_number = int(input("guess number 1 to 100 :"))
num = 20
if guess_number > num:
    print("მაღალი")
elif guess_number < num:
    print("დაბალი")
elif guess_number == num:
    print("სწორია")