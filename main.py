import random
from word_find import select_letters, display_letters, validate_word

print("Welcome to Word Find. \nCome up with as many words as possible from the letters below! \n")

def get_mode_instructions(code):
  if(code == "h"):
    return "Hard mode selected. Entering and invalid word will end the game!"
  elif(code == "e"):
    return "Easy mode selected."

def check_used_word(word, used_words):
  if any(string in word for string in used_words):
    return True  
  else:
    return False

def check_not_valid_characters(letters: list, word: str):
  if any(s not in letters for s in word.upper()):
    return True
  else:
    return False    

def calculate_score(word: str):
  score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

  return sum(map(score.get, word))

mode_prompt = "Do you wish to play [e]asy mode or [h]ard mode? "
mode_code = input(mode_prompt)
is_hard_mode = mode_code == "h"
hard_mode = is_hard_mode

while True:
  is_invalid_input = not (mode_code == "e" or mode_code == "h")

  if(is_invalid_input):
    print("Invalid input, please select a mode. \n")
    mode_code = input(mode_prompt)
  else:
    mode_str = get_mode_instructions(mode_code)
    print(mode_str)
    break


letters = select_letters()
used_words = []
total_score = 0
  
while True:
  print(f"\nScore: {total_score}. Your letters are: ")
  display_letters(letters)

  word = input("Enter a word, [s]huffle letters, [l]ist words, or [e]nd game: ")

  if(len(word) >= 3):
    is_valid_word = validate_word(word)
    is_used_word = check_used_word(word, used_words)
    is_not_valid_characters = check_not_valid_characters(letters, word)


    if(is_valid_word):
      if(is_not_valid_characters):
        print("You're using invalid characters!")
        if(hard_mode):
          print("Game Over!")
          break
      elif(is_used_word):
        print(f"Already used {word.upper()}")
        if(hard_mode):
          print("Game Over!")
          break
      else:
        score = calculate_score(word.lower())
        total_score += score
        used_words.append(word)
        print(f"\n{word.upper()} accepted - {score} points awarded. Your score is now {total_score}.")
    else:
      print(f"{word.upper()} is not a valid word!")
      if(hard_mode):
        print("Game Over!")
        break
        
  elif(word == "s"):
    print('\nShuffling letters...')
    random.shuffle(letters)
  elif(word == "l"):
    print("\nPreviously entered words:")
    used_words.sort()
    for w in used_words:
      print(f"- {w.upper()}")
  elif(word == "e"):
    break
  else:
    print("Word has a minimum length of 3 charactors!")
    if(hard_mode):
      print("Game Over!")
      break





