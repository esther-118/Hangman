def wordToGuess():
       return "satoru"

def getInput():
       guessedLetters = ""
       correctLetters = ""
       correctCount = 0
       
       while True:
              character = input("\nEnter the guess: ").lower()
              if (validate(character, guessedLetters)):
                     print("You guessed one letter correct! Character: " + character)
                     correctLetters = correctLetters + character
                     correctCount = correctCount + 1
                     printWord("satoru", correctLetters)
                     printBody(guessedLetters)
                     if (correctCount == len("satoru")):
                            print("You win")
                            break
              else:
                     print("You guessed one letter incorrect. Character: " + character)
                     guessedLetters = character + guessedLetters
                     print("Characters that were guessed: " + " ".join(sorted(guessedLetters)))
                     printWord("satoru", correctLetters)
                     printBody(guessedLetters)
                     if (len(guessedLetters) > 5):
                        print("Game over")
                        break

def printWord(word, correctLetters):
       result = ""
       for letter in word:
            if (letter in correctLetters):
                   result = result + letter
            else:
                   result = result + "_"
       print(result)
       
def printBody(guessedLetters):
       if (len(guessedLetters) == 6):
              print(" o")
              print("/|" + chr(92))
              print(" /" + chr(92))
       if (len(guessedLetters) == 5):
              print(" o")
              print("/|" + chr(92))
              print("/")
       if (len(guessedLetters) == 4):
              print(" o")
              print("/|" + chr(92))
       if (len(guessedLetters) == 3):
              print(" o")
              print("/|")
       if (len(guessedLetters) == 2):
              print(" o")
              print(" |")
       if (len(guessedLetters) == 1):
              print(" o")
       if (len(guessedLetters) == 0):
              print("")

def validate(playerInput, guessedLetters):
         return (len(playerInput) == 1 and playerInput in "satoru" and playerInput not in guessedLetters)

def main():
        print("H   A   N   G   M   A   N   !\n")
        getInput()

if __name__ == "__main__":
    main()