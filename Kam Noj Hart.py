import random

while True:

    Item = ["камък", "ножица", "хартия"]

    computer = random.choice(Item)

    player = None


    while player not in Item:
        player = input("Избери камък, ножица или хартия: ").lower()

        if player == computer:  # ок
            print("Computer има:" + computer)
            print("Ти имаш: "+player)
            print("Равни")
        elif player == "камък":     # ок
            if computer == "ножица":
                print("Computer има:" + computer)
                print("Ти имаш: " + player)
                print("Ти печелиш!")
            if computer == "хартия":
                print("Computer има:" + computer)
                print("Ти имаш: " + player)
                print("Ти губиш!")

        elif player == "ножица":    # ок
            if computer == "хартия":
                print("Computer има:" + computer)
                print("Ти имаш: " + player)
                print("Ти печелиш!")

            if computer == "камък":
                print("Computer има:" + computer)
                print("Ти имаш: " + player)
                print("Ти губиш!")
        elif player == "хартия":
            if computer == "камък":
                print("Computer има:" + computer)
                print("Ти имаш: " + player)
                print("Ти печелиш!")

            if computer == "ножица":
                print("Computer има:" + computer)
                print("Ти имаш: " + player)
                print("Ти губиш!")

        playAgain = input("Още една игра? да/не?: ").lower()
    if playAgain != "да":
        break
print("Bye")