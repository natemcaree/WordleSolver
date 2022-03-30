import all5letters
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://www.nytimes.com/games/wordle/index.html")
driver.maximize_window()

driver.implicitly_wait(2)

ActionChains(driver).move_by_offset(10 , 10).click().perform()

driver.implicitly_wait(2)


def wordlist (self, word, letter_status):
    
    correct = []
    wrongspot = []
    incorrect = []
    
    
    for i in range(len(word)): 
            if letter_status[i] == "correct":
                correct.append[i]
            if letter_status[i] == "absent":
                #remove letter from pool
            if letter_status[i] == "present"
                #save letter and force letter to be used, refuse to use that letter

def play_game(self):
    # goes within for loop to push words?
    button2 = 'button[data-key="%s"]' % letter

    success = False
    
    placeholder = 'wordlist choice goes here'

    button = 'button[data-key="↵"]'

    keyboard_base = "game-app::shadow game-keyboard::shadow "

    row = 'game-app::shadow game-row[letters="%s"]::shadow ' % placeholder

    tile = row + "game-tile:nth-of-type(%s)"




    #need to add a start loop and end loop (break) when all 5 are correct. 
    #need to add a sleep to let animation play out
    

    self.save_screenshot_to_logs()
    print('\nWord: "%s"\nAttempts: %s' % (word.upper(), total_attempts))
    if not success:
         self.fail("Unable to solve for the correct word in 6 attempts!")
    