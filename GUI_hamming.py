from tkinter import *
from Hamming_code import *

root = Tk()
root.title("Hamming")
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
w = 400
h = 120
x = (screenWidth - w) / 2
y = (screenHeight - h) / 2
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

label1 = Label(root, text="Enter     bit     sequence：", bg ="grey",fg="white",font="Cursive")
entry1 = Entry(root)
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1, sticky=W + E)

label2 = Label(root, text="Enter test hamming code: ", bg ='grey',fg="white",font="Cursive")
entry2 = Entry(root)
#entry2.insert(0, "例：x^4+x^1+1")
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1, sticky=W + E)

def generate():

    bit_sequence = entry1.get()
    code_raw = list(bit_sequence)
    try:
        code_raw = list(map(int, code_raw))
    except:
        label3.config(text='not valid input')
    if code_raw.count(1)+code_raw.count(0) == len(code_raw) & len(code_raw)!=0:
        code_ham = generate_hamming_code(code_raw)
        code_ham = map(str, code_ham)
        code_ham = ''.join(code_ham)
        label3.config(text=code_ham)
    else:
        label3.config(text='not valid input')
def check():
    code_input = entry2.get()
    code_input = list(code_input)
    try:
        code_input = list(map(int, code_input))
    except:
        label4.config(text='not valid input')
    if code_input.count(1) + code_input.count(0) == len(code_input) & len(code_input) != 0:
        flag = check_hamming_code(code_input)
        if type(flag) == int:
            label4.config(text='correct hamming code')
        else:
            code_ham_correct = flag
            code_ham_correct = map(str, code_ham_correct)
            code_ham_correct = ''.join(code_ham_correct)
            label4.config(text=code_ham_correct)
    else:
        label4.config(text='not valid input')


label3 = Label(root, text="                                     ", bg="white")
label4 = Label(root, text="                                     ", bg="white")
button1 = Button(root, text="Generate hamming code", relief="groove", command=generate)
button2 = Button(root, text="Check code", relief="groove", command=check)
label3.grid(row=2, column=1)
label4.grid(row=3, column=1)
button1.grid(row=2, column=0)
button2.grid(row=3, column=0)
root.mainloop()