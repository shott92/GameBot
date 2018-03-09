import tkinter
from tkinter import ttk
from tkinter import tix
import os

##start GUI
root = tkinter.Tk()
##Window name
root.title('GameBot')

#create container frame 
frameStyle = ttk.Style()
frameStyle.configure("frame.TFrame", padx="20", pady="20", relief="flat", background="#0a0082")

###
##would like the window to be resizable and for the two text frames to auto adjust size.
###

frame = ttk.Frame(root, style="frame.TFrame")
frame.pack()

##add a text box - bg white - ideal solution to convert the text box to a frame and have individual text boxes generated per chat,
##or alternate the colout of the text highlight 
chatWindow = tkinter.Text(frame, state="disabled", relief="raised", wrap="word")
chatWindow.pack(fill="x", padx="10", pady="5")
scrollbar = ttk.Scrollbar(chatWindow)
scrollbar.pack(side = "right", fill="y" )  
scrollbar.config(command = chatWindow.yview )


def writeToLog(msg):
    numlines = chatWindow.index('end - 1 line').split('.')[0]
    chatWindow['state'] = 'normal'
    if chatWindow.index('end-1c')!='1.0':
        chatWindow.insert('end', '\n')
    chatWindow.insert('end', msg)
    chatWindow['state'] = 'disabled'
    

def userTextInput():
   userInput = input.userTextBox.get("1.0", "END-1c")
   userTextBox.delete(0,END)
   
userTextBox = tkinter.Text(frame,  bg="#87ceeb", relief="sunken", wrap="word")
userTextBox.pack(fill="x", padx="10")

enter_btn = ttk.Button(frame, text="enter", command=userTextInput)
enter_btn.pack(side="right", padx="10")

exit_btn = ttk.Button(frame, text="exit", command=root.quit)
exit_btn.pack(side="right", padx="10")

#end GUI code
root.mainloop()
##End GUI

userName = input('what is your name? \n')
print('Hello ', userName)

gameType = input('Are we going to play \'eye spy\' or \'odd one out\' ? \n')
if gameType == 'eye spy':
    print('great let\'s play eye spy')

    eyeSpyItem = input('Eye spy with my little eye, something Beginning with M \n')

    if eyeSpyItem == 'Mouse' or eyeSpyItem == 'mouse':
        print('A ', eyeSpyItem, ' how did you guess! ')
        
    elif eyeSpyItem == 'Mirror' or eyeSpyItem == 'mirror':
        print(eyeSpyItem, '! that\'s the right answer. Well done', userName)
               
    else:
        print('Sorry that\'s not the right answer, better luck next time!')
        
elif gameType == 'odd one out':
    print('Great, this will be fun,')
    print('choose the odd one out! \n Dog \n Cat \n Spoon')
    answer = 'blank'
    while answer.strip() != 'Spoon' or 'spoon':
        answer = input()
        if answer == 'Spoon' or answer =='spoon': print('Well done ', userName, '! \n You got it right.')
        elif answer == 'Dog' or answer == 'dog' or answer == 'Cat' or answer == 'cat': print('Sorry ', userName, '\n', answer, ' is not the right answer, try again')
        else: print('I dont understand, please select from Dog, Cat, or Spoon')
        
        
else:
    print('I am unable to help with that, Goodbye', userName)
print('Thanks for playing ', userName, ' until next time!')
