from tkinter import *

currentRow = 0

## As we are loading data we do not know how many rows we will need so we 
## maintain a global currentRow variable to get the nex available row
def getNewRow():
    global currentRow
    temp = currentRow
    currentRow += 1
    return temp

## Our main function which sets up the window
def showWindow():
    window = Tk()
    window.title = "Person List"
    window.geometry('500x400')
    printLines("user_school.csv", window)
    window.mainloop()

def printLines(fileName, window):
    lines = getFileLines(fileName)
    schools = getFileLines("school.csv")
    users = getFileLines("user.csv")
    # Display column titles
    displayLine("User\t\tInstitution\t\tTelephone", window, getNewRow(), True)
    for line in lines:
        # Split the current line into a list based on the comma
        split = line.split(',')
        
        # go and find the user and school based on 
        userCSV = getEntity(users, split[1].rstrip())
        # userCSV = "2,Josh,Student\n"
        schoolCSV = getEntity(schools, split[2].rstrip())
        # schoolCSV = "1,Ysgol Emrys Ap Iwan,01492 222333\n"
        user = userCSV.split(',')
        # user = [2, "Josh", "Student\n"]
        user = user[1]
        # user = "Josh"
        school = schoolCSV.split(',')
        # school = [1, "Ysgol Emrys Ap Iwan", "01492 222333\n"]
        schoolName = school[1]
        # schoolName = "Ysgol Emrys Ap Iwan"
        telephone = school[2].rstrip()
        displayLine(user + "\t\t" + schoolName + "\t" + telephone , window, getNewRow())

## Reads a file and returns a list with the lines from the file
def getFileLines(fileName):
    with open(fileName, "r") as f:
        return f.readlines()

## Takes a list of file lines and searches for an entity with a 
## given id, if nothing is found an empty string is returned
def getEntity(entities, id):
    for entity in entities:
        split = entity.split(',')
        if(split[0] == id):
            return entity
    return ""


## Displays a new label on a window the title flag will decide
## whether the label needs to be bold or not  
def displayLine(text, window, row, title=False):
    if title:
        font = "Helvetica 13 bold"
    else:
        font = "Helvetica 13"
    lbl = Label(window, text=text, width="60", anchor="w", font=font)
    lbl.grid(column=0, row=row)


showWindow()