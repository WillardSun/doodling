secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit :
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print(f"You won! {secret_number} was the answer!")
        break
else:
    print ("Sorry, you failed, try harder!")


