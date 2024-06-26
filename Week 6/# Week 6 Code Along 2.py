# Week 6 Code Along 2

try:
    number_of_scores = int(input("Enter how many scores: "))
    scores = []

    for x in range(0, number_of_scores):
        while True:
            try:
                score = int(input(f"What is the score #: {x + 1}"))
                scores.append(score)
            except:
                print("Invalid score, enter again")
            else:
                break

except:
    print("Invalid input entered")



while True:
    try:
        email_address = input("Enter an email address bro")
        parts = email_address.split("@")
        name = parts[0]
        domain = parts[1].split(" , ")
        print("The email address is:", name, domain[0], domain[1])
        print("Thank You")
        break
    except:
        print("That was not a correct email address")
        pass
    break



