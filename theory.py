
# In theory, we should be able to create a main arg and pass the location of your web browser
# to run the browser shortcutted directly to wordle, then use selenium to inspect element view game boxes.
# Game tile reads as game-tile and will put in the letter of what you guessed. Once you guess, it will show
# if the game tile gets revealed or stays hidden. It reads correct if it's green. So we do NOT need to 
# use a bot to read screen colors. Find list of already used words and push priority to back end. 



# Use selenium to read inspected element for game rows and elements, use if statements to go through "ok, 
# we have the letter P in square 3. Waht are the msot common words with P that a) have not been used and 
# b) do not have the letter p in that spot"