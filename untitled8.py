from tkinter import *
import random

root=Tk()
root.title("amogus")
root.geometry("400x400")

array=[[["sus"],["0","1","2","3","4","5","6","7","8","9"],["!","@","#","$","%","^","&","*","-","+",":","'","<",">","?"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]]]
label=Label(root)
label.place(relx=0.5,rely=0.4,anchor=CENTER)
input1 = Entry(root)
input1.place(relx=0.5,rely=0.5,anchor=CENTER)
def generate():    
    print(enter)
    print(password)
    if enter==password:
        label["text"]="correct"
    else:
        label["text"]="wrong"
    label["text"]=""
    i=0
    code=""
    repeat = random.randint(5,10)
    while i<repeat:
        i=i+1
        mode = random.randint(0,3)
        type1 = 0
        type2 = random.randint(0,9)
        type3 = random.randint(0,14)
        type4 = random.randint(0,25)
        if 0 == mode:
            label["text"] +=  str(array[0][mode][type1])
            code += str(array[0][mode][type1])
            password=code
        if 1 == mode:
            label["text"] +=  str(array[0][mode][type2])
            code += str(array[0][mode][type2])
            password=code
        if 2 == mode:
            label["text"] +=  str(array[0][mode][type3])
            code += str(array[0][mode][type3])
            password=code
        if 3 == mode:
            label["text"] +=  str(array[0][mode][type4])
            code += str(array[0][mode][type4])
            password=code


button=Button(root,text="generate",command=generate)
button.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()