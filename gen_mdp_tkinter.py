from tkinter import *
from tkinter import messagebox
import random


fenetre = Tk()

   
label = Label(fenetre, text="Click to Generate And Close The Window")
label.pack()


    
mdp = ('A','B','C','D','E','F','G','H','I','J','K','L','M',
        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        '~','`','!','@','#','£','€','$','¢','¥','§','%','°','^','&','*',')','-','_','+','=','{','}','['	,']','|','/',':',';',		
        '<','>',',','.','?')
    

#def line():
    
for i in range(12):
    mdp_generate = random.choice(mdp)
    print(mdp_generate, end="")
    

generate_btn = Button(text='Generate', command=mdp_generate) 
generate_btn.pack()
    
    
fenetre.mainloop()
