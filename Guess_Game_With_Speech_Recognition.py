import speech_recognition as sr
import random

Words = (
    "kivy",
    "banana",
    "apple",
    "grape",
    "google"
)
print(f"You must guess from these words:\n{Words}")
Word = random.choice(Words)


chances = 3
Wining = False
while chances != 0:
    if Wining:
        break
    Detection = False
    while not Detection:
        try:
            print("Say: ")
            Recognizer = sr.Recognizer()

            Microphone = sr.Microphone()
            with Microphone as source:
                Audio = Recognizer.listen(source)
            Result = str(Recognizer.recognize_google(Audio)).lower()
            Detection = True
            chances -= 1
            print(f"You said: {Result}")
            if Result == Word:
                Wining = True
                break
        except:
            print("not understood say again: ")
            continue


if Wining:
    print("You guess the word in " + str(3 - chances) + " try.")
else:
    print(f"You lose!\nThe correct word is {Word}")
