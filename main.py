import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5


def create_task():
    text = ""
    print("Что добавить в заметки?\n")
    with open("to_do_list.txt", 'a', encoding="utf-8") as file:
        while text != "":
            text = recognize_voice()
            if text != "":
                file.write(f'{recognize_voice()}')


def recognize_voice():
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        query = sr.recognize_google(audio_data=audio, language="ru-RU").lower()
    return query


def main():
    while True:
        text = recognize_voice()
        if text == 'добавить заметку':
            create_task()
        if text == 'выйти':
            exit()
        print(text)


if __name__ == '__main__':
    main()
