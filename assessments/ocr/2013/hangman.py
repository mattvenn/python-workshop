import random

#allow end user to put in new words
ask = raw_input("input new words? (y/n): ")
if ask == 'y':
    new_words = raw_input("type comma separated words: ")
    words = new_words.split(',')
    print("new words: " + ','.join(words))
else:
    # set of related words in an array
    words = [ 'python', 'rattlesnake', 'adder', 'cobra' ]

# select a random word
word = random.choice(words)

# show number of characters
display_word = ['*'] * len(word)
print("guess the word")

# 6 lives
lives = 6

# allow guesses
guessed = []
while lives > 0:
    print(''.join(display_word))
    guess = raw_input("guess a letter")

    #already guessed?
    if guess in guessed:
        print("already guessed")
        next

    #if guess in word, show it in correct position
    if guess in word:
        print("correct guess!")
        guessed.append(guess)
        for char in range(len(word)):
            if word[char] == guess:
                display_word[char] = guess

    if ''.join(display_word) == word:
        print(''.join(display_word))
        # show lives left as score
        print("well done you got it with %d lives left!" % lives)
        break
    else:
    #otherwise lose life
        lives -= 1
        print("bad guess - you have %d lives left" % lives)

else:
    print("you're out of lives") 
