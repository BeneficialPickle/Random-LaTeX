from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter as tk
import random
import os
import re

root = Tk()
files = []
labels = []
initialdir = "C:/Users/poote/Desktop/" #TODO change to be dynamic

def OpenFile():
    global initialdir
    path = askopenfilename(initialdir=initialdir,
                           filetypes=(("LaTeX Files", "*.tex"), ("All Files", "*.*")),
                           title="Choose a file."
                           )
    try:
        initialdir = os.path.abspath(path)  #sets the opening directory to the previously used directory
        files.append(path)
        temp = Label(root, text=path + " added.")
        temp.pack()
        temp.place(relx=0.5, rely=0.65, anchor=CENTER)
        for label in labels:
            label.destroy()
        labels.append(temp)
    except:
        print("No file exists")

def CreatePdf():
    save = tk.tkFileDialog.askDirectory()
    questions = []
    latexCode = ""
    title = "Title"
    print(save)
    for f in files:
        try:
            file = open(f)
            temp = re.findall(r'\\begin{question}(.*?)\\end{question}', file.read(), re.S)
            rand = random.randint(0, len(temp) - 1)
            questions.append(temp[rand])
        except:
            print("There was an error in creating the PDF.")
            continue
    for q in questions:
        latexCode += "\\begin{question}\n" + q[5:None] + "\\end{question}\n\n"
    document = r'''\documentclass[12pt]{article}
    \usepackage{tasks}
    \usepackage{exsheets}
    \usepackage{graphicx}
    \usepackage{fullpage}
    \usepackage{multicol}
    \usepackage{amsmath,amsthm,amssymb}
    \SetupExSheets[question]{type=exam}

    \newtheorem{theorem}{Theorem}
    \newtheorem{corollary}{Corollary}[theorem]
    \newtheorem{lemma}[theorem]{Lemma}

    \begin{document}

    \begin{center}
    \textbf{\large ''' + title + '''}
    \end{center}
    ''' + latexCode + "\end{document}"

    with open(save + 'randomized_' + title + '.tex', 'w') as f:
        f.write(document)  # create a new file and shove the latex code in

    filename = save + "randomized_" + title + ".tex"

    os.system("pdflatex " + filename)  # compile the code with the command pdflatex

    # remove the non-pdf files that come with compiling
    try:
        os.unlink(save + "randomized_" + title + ".tex")
        os.unlink(save + "randomized_" + title + ".log")
    except:
        print("Encountered an error removing the .tex and .log files.")


Title = root.title("LaTeX Problem Set Generator")
Size = root.geometry('400x200')

# Button

chooseFile = Button(root, text="Choose Files", command=OpenFile)
chooseFile.pack()
chooseFile.place(relx=0.5, rely=0.4, anchor = CENTER)
stop = Button(root, text="Compile PDF", command=CreatePdf)
stop.pack()
stop.place(relx=0.5, rely=0.55, anchor = CENTER)

root.mainloop()
