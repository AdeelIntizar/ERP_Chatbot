import speech_recognition as sr
def convert_text_to_speech(engine, response):
    modified_bot_str = response.replace("Bot ", "").strip()
    engine.say(modified_bot_str)
    engine.runAndWait()
    return 
def convert_to_text(engine):
    r = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                user_input = r.recognize_google(audio2)
                return user_input
        except sr.UnknownValueError:
            
            str="Sorry I did not get what you said, can you please repeat?"
            print(str)
            convert_text_to_speech(engine,str)
        except sr.RequestError:
            print("Sorry, there was an issue with the speech service. Please check your internet connection.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break