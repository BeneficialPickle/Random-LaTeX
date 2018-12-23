from tkinter import *
from tkinter.filedialog import askopenfilename
import random
import os
import re

root = Tk()
files = []
labels = []

def OpenFile():
    path = askopenfilename(initialdir="C:/Users/poote/Desktop/",
                           filetypes=(("LaTeX Files", "*.tex"), ("All Files", "*.*")),
                           title="Choose a file."
                           )
    try:
        files.append(path)
        temp = Label(root, text=path + " added.")
        temp.pack()
        temp.place(relx=0.5, rely=0.6, anchor=CENTER)
        for label in labels:
            label.destroy()
        labels.append(temp)
    except:
        print("No file exists")

def CreatePdf():
    questions = []
    latexCode = ""
    title = "Title"
    save = ""
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
    \textbf{\large ''' + title + '''}\\[1ex]
    \end{center}
    ''' + latexCode + "\end{document}"

    with open(save + 'randomized_' + title + '.tex', 'w') as f:
        f.write(document)  # create a new file and shove the latex code in

    filename = save + "randomized_" + title + ".tex"

    os.system("pdflatex", filename)  # compile the code with the command pdflatex

    # remove the non-pdf files that come with compiling
    try:
        os.unlink(save + "\\randomized_" + title + ".tex")
        os.unlink(save + "\\randomized_" + title + ".log")
    except:
        print("Encountered an error generating the pdf.")


Title = root.title("LaTeX Problem Set Generator")
Size = root.geometry('400x400')

# Button

chooseFile = Button(root, text="Choose Files", command=OpenFile)
stop = Button(root, text="Compile PDF", command=CreatePdf)
chooseFile.pack()
stop.pack()
chooseFile.place(relx=0.5, rely=0.4, anchor = CENTER)
stop.place(relx=0.5, rely=0.5, anchor = CENTER)

root.mainloop()
