import pyttsx3
import requests
import time
import pyperclip  

engine = pyttsx3.init()



def get_definition(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if response.status_code == 200:
        data = response.json()
        if data:
            meanings = data[0]['meanings']
            definitions = []
            for meaning in meanings:
                definition = f"• Meaning: {meaning['partOfSpeech']}\nDefinition: {meaning['definitions'][0]['definition']}\n"
                definitions.append(definition)
                # Speak out the definition
                engine.say(definition)
            engine.runAndWait()  # Wait for the speech to finish
            return '\n'.join(definitions)
        return "No definition found."
    return "No definition found."

def find_definition():
    # Get the word under the mouse cursor
    # word = pyautogui.prompt("Please select a word to find its definition:")
    word_copy=""
    while True :
        word = pyperclip.paste()
        print("word_copy is "+word)
        if word != word_copy:
            print("New word copied: "+ word)
            word_copy = word
            engine.say("your word is "+word)
            if word:
                print(get_definition(word)) #this is definotion
        time.sleep(1)              
      
    
def main():
     engine.say("welcome to word defintion reader")
     find_definition()

if __name__ == "__main__":
    main()