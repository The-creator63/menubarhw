from tkinter import*

root = Tk()
root.title("Student Information Window")
root.geometry("450x300")
root.config(background = "#BCD8C1")

#creating the labels
user_name = Label(root,text = "Name").place(x = 40,y = 60)
grade = Label(root,text = "Grade").place(x = 40,y =100)
section= Label(root,text = "Section").place(x = 40,y =140)
age = Label(root,text = "Age").place(x = 40,y =180)

#creating the text boxes
user_input = Entry(root,width = 30).place(x = 120,y = 60)
grade_input = Entry(root,width = 30).place(x = 120,y = 100)
sect_input = Entry(root,width = 30).place(x = 120,y = 140)
age_input = Entry(root,width = 30).place(x = 120,y = 180)

#creating the menubar
menubar = Menu(root)

#adding menu and the commands
grade = Menu(menubar,tearoff = 0)
menubar.add_cascade(label = "Grade",menu = grade)
grade.add_command(label = "6",command = None)
grade.add_command(label = "7",command = None)
grade.add_command(label = "8",command = None)
grade.add_command(label = "9",command = None)
grade.add_separator()
grade.add_command(label = "Other...",command = None)

Class = Menu(menubar,tearoff = 0)
menubar.add_cascade(label = "Class",menu = Class)
Class.add_command(label = "a",command = None)
Class.add_command(label = "b",command = None)
Class.add_command(label = "c",command = None)
Class.add_command(label = "d",command = None)
Class.add_separator()
Class.add_command(label = "Other...",command = None)

#creating the submit button
submit_btn = Button(root,text ="Submit", command = root.destroy).place(x = 90, y = 230)
root.config(menu = menubar)
root.mainloop()