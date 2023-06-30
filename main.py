import random
import words
import art

end_of_game = False
chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)

lives = len(art.stages) - 1
display = []
for i in range(word_length):
    display.append("_")
print(art.logo)
while '_' in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess not in chosen_word:
        lives -= 1
    else:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess

    print(f"{' '.join(display)}")
    print(art.stages[lives])

if (lives < 0 or "_" in display):
    print(f'The word was {chosen_word}.\nYou lost.')
else:
    print('You won!')
