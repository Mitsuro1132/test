import random

numbers = random.randint(1,100)

print("Вгадай число від 1 до 100")

while True:
    print_number = int(input("Введіть число: "))
    if print_number == numbers:
        print("Ви вгадали число!")
        break
    elif print_number > numbers:
        print(f"Ви не вгадали число, але воно менше за {print_number}")
    elif print_number < numbers:
        print(f"Ви не вгадали число, але воно більше за {print_number}")