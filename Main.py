import re
import random
import subprocess
import os

userInput = ""
questions = ""
array = []#array of one random question from each assignment

title = "title"
save = input("Enter the file path to where you want your pdf saved.")
#title = input("Enter the title of the pdf.")
while userInput != "stop":
    userInput = input("Please enter the file location of your tex file, or enter 'stop'.")
    try:
        file = open(userInput)
        #something that finds the section in the latex file - SO
        temp = re.findall(r'\\begin{question}(.*?)\\end{question}', file.read(), re.S)
        rand = random.randint(0, len(temp) - 1)
        array.append(temp[rand])
    except:
        if userInput != stop:
            print("An error occured, please try again\n")
        continue

for i in array:
    questions += "\\begin{question}\n" + i[5:None] + "\\end{question}\n\n"
    #wrap the contents in the question environment

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

''' + questions + "\end{document}"

with open('randomized_' + title + '.tex', 'w') as f:
    f.write(document)#create a new file and shove the latex code in

os.system(save + "pdflatex randomized_" + title + ".tex")#compile the code with the command pdflatex

#remove the non-pdf files that come with compiling
os.unlink(save + "randomized_" + title + ".tex")
os.unlink(save + "randomized_" + title + ".log")
