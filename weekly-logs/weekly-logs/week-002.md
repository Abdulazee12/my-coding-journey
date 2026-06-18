## Day 12 — June 17, 2026
- Topic: Hangman game - while loops, lists, strings
- Built the guess-checking and display-update logic for Hangman
- Learned the difference between looping through values vs 
  positions/indexes in a list
- Learned strings are immutable, lists are mutable - and why 
  that matters for updating display
- Used ''.join(display) to convert a list back into a string
- Set up lives variable (6) and 7-stage ASCII art list, ready 
  to wire together next session
- Still pending: reduce lives on wrong guess, show correct 
  stage art, handle "You lose" condition



  ## Day 13 — June 18, 2026
- Topic: Hangman game - completed (lives, break, ASCII stages)
- Wired up lives to decrease on wrong guesses and trigger 
  "You lost" / "You won" correctly
- Learned and implemented two approaches to stopping a while 
  loop early: combined condition vs break statement
- Used lives as a dynamic list index to display the correct 
  hangman stage automatically
- Fixed SyntaxWarnings from unescaped backslashes in ASCII art
- Hangman game challenge fully complete 🎉