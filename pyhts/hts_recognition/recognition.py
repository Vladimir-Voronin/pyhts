import re

import pyaudio
from vosk import Model, KaldiRecognizer


class HTSRecognizerVosk:
    def __init__(self, language="en-us"):
        self.__current_recognized = bytearray()  # recognized words after last getting
        self.__model = Model(lang=language)
        self.__recognizer = KaldiRecognizer(self.__model, 16000)
        cap = pyaudio.PyAudio()
        self.__stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        self.__stop_stream_flag = False  # to turn off recognize

    # This method may not be necessary
    def __del__(self):
        self.__stream.stop_stream()
        self.__stream.close()

    def is_working(self):
        if self.__stream.is_active():
            return True
        return False

    def get_last_recognized(self):
        result = self.__current_recognized.copy()
        self.__current_recognized.clear()  # ?? Is it possible to lose some data, coz of multithreading?
        return result

    def turn_on(self):
        self.__stream.start_stream()
        while not self.__stop_stream_flag:
            data = self.__stream.read(4096)
            pattern = r'\"text\" : \"(.+)\"'
            if self.__recognizer.AcceptWaveform(data):
                result = re.search(pattern, self.__recognizer.Result())
                if result:
                    str_b = " ".join(result.group(1).split(' '))
                    byte_arr = bytearray(str_b, 'utf-8')
                    self.__current_recognized.extend(byte_arr)
            if self.__stop_stream_flag:
                self.__stream.stop_stream()
        self.__stop_stream_flag = False

    def turn_off(self):
        self.__stop_stream_flag = True
