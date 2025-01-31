import speech_recognition as sr
import pyttsx3 

r = sr.Recognizer() 

def record_text():
    try:
        with sr.Microphone() as source2:
            
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.energy_threshold=250
            r.pause_threshold = 2.5
            r.adjust_for_ambient_noise(source2, duration=0.2)

            #listens for the user's input 
            audio2 = r.listen(source2, phrase_time_limit=15)
            
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.capitalize()

            print(MyText)
            # SpeakText(MyText)
            
    except sr.RequestError as e:
        print("error : ",str(e))
        
    except sr.UnknownValueError as e:
        print("error : ",str(e))


# def output_text():
#     f = open("output.txt","a")
#     f.write(text)
#     f.write('\n')
#     f.close()
#     return

    
# Loop infinitely for user to
# speak

while(1):    
    text = record_text()
    # output_text(text)
    print("Done")

    