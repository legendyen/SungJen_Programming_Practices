import pandas as pd

# import Google Text to Speech to convert text to speech
from gtts import gTTS
import os

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
# print(nato_data.to_dict())
# found out the dictionary format is not what we wanted, therefore use dictionary comprehension

while True:
    nato_dict = {row["letter"]: row["code"] for index, row in nato_data.iterrows()}
    # print(nato_dict)

    word = list(input("Enter a word: ").upper())
    print(word)

    nato = [nato_dict[character] for character in word]
    print(nato)

    text = ''.join(nato)
    print(text)

    speech = gTTS(text=text, lang='en', slow=True)
    speech.save("text.mp3")
    os.system("start text.mp3")

    flag = (input("Press 'Enter' to continue: \n"))
    if flag == "":
        continue
    else:
        break


