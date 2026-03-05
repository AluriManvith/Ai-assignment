import random

while True:
    a = random.randint(1,20)
    b = random.randint(1,20)

    op = random.choice(["+","-"])

    if op == "+":
        answer = a + b
    else:
        answer = a - b

    print("Captcha:", a, op, b)

    user = int(input("Answer: "))

    if user == answer:
        print("Captcha Verified")
        break
    else:
        print("Wrong answer. Try again")