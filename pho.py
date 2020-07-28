from tkinter import  *
import random

canvas_width = 300
canvas_height = 300

root =Tk()
root.title("Dice Roller")
root.geometry("400x400")
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()



img1=  PhotoImage(file='sample1.png')
img2 = PhotoImage(file='sample2.png')
img3 = PhotoImage(file='sample3.png')
img4 = PhotoImage(file='sample4.png')
img5 = PhotoImage(file='sample5.png')
img6 = PhotoImage(file='sample6.png')
canvas.create_image(200, 200, image=img1 )






def dice_roller():
    numb = random.randint(1, 6)

    if numb == 1:
         canvas.create_image(200, 200, image=img1 )

    elif numb == 2:
        canvas.create_image(200, 200, image=img2 )

    elif numb == 3:
        canvas.create_image(200, 200, image=img3 )

    elif numb == 4:
        canvas.create_image(200, 200, image=img4 )

    elif numb == 5:
        canvas.create_image(200, 200, image=img5 )

    elif numb == 6:
        canvas.create_image(200, 200, image=img6 )

    root.update()




b = Button(root, text ="roll dice", command = dice_roller)
b.pack()



#root.update()
#root.after(100)





root.mainloop()

