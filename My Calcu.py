import operator
import webbrowser as web
import speech_recognition as sr

from tkinter import *

print("Your speech_recognition version is: " + sr.__version__)

window = Tk()
window.title("Calculator and Search Box")
window.geometry("500x500")

def evaluate():
    r = sr.Recognizer()
    m = sr.Microphone(device_index=1)
    with m as source:
        print("Say what you want to calculate, example: 3 plus 3")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    string = r.recognize_google(audio)
    print(string)

    var = StringVar(window, string)

    var.set("label")
    label = Label(window, text=string, font=("helvetica", "20"))
    label.pack()
    label.place(x=100, y=200)

    def get_operator_fn(op):
        return {
            '+': operator.add,
            '-': operator.sub,
            'x': operator.mul,
            'divided': operator.__truediv__,
            'Mod': operator.mod,
            'mod': operator.mod,
            '^': operator.xor,
        }[op]

    def eval_binary_expr(op1, oper, op2):
        op1, op2 = int(op1), int(op2)
        return get_operator_fn(oper)(op1, op2)

    answer = eval_binary_expr(*(string.split()))
    print(answer)

    var1 = IntVar(window, answer)

    var1.set("label")
    label1 = Label(window, text=answer, font=("helvetica", "20"))
    label1.pack()

def search():

    def main():
        path = "C:/Program Files (x86)/Google/Update/Download/{8A69D345-D564-463C-AFF1-A69D9E530F96}/96.0.4664.45/96.0.4664.45_chrome_installer.exe %s"

        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)

            print("Please say something ")

            audio = r.listen(source)

            print("Recognizing Now ... ")

            try:
                dest = r.recognize_google(audio)
                print("You have said : " + dest)

                web.get(path).open(dest)

            except Exception as e:
                print("Error : " + str(e))

    if __name__ == "__main__":
        main()


btn = Button(window, text='Tap and Speak', command=evaluate)
btn.pack()

btn2 = Button(window, text='Tap and Search', command=search)
btn2.pack()

button = Button(window, text='Stop', width=25, command=window.destroy)
button.place(x=900, y=100)
button.pack()

window.mainloop()
