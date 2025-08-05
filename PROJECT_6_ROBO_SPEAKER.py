import pyttsx3

class RoboSpeaker:
    def _init_(self):
        pass 

    def speak(self):
        print("Welcome to ROBO SPEAKER")
        print("Enter 'exit' to quit\n")

        while True:
            text = input("Please enter what you want to say: ").strip()
            if text.lower() == "exit":
                print("Goodbye!")
                self.speak_text("Goodbye")
                break
            elif text == "":
                print("Please type something.")
                continue
            self.speak_text(text)

    def speak_text(self, text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(text)
        engine.runAndWait()
        engine.stop()

speaker = RoboSpeaker()
speaker.speak()


