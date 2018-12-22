import re
import random
import subprocess
import os

numOfFiles = 8
array = []
questions = ""

for i in range(numOfFiles):
    file = open('C:/Users/poote/Documents/MATH147/LaTeX - new/A' + str((i + 1)) + '.tex')
    temp = re.findall(r'\\begin{question}(.*?)\\end{question}', file.read(), re.S)
    rand = random.randint(0, len(temp) - 1)
    array.append(temp[rand])

for i in array:
    questions += "\\begin{question}\n" + i[5:None] + "\\end{question}\n\n"

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
\textbf{\large Math 147 (Davidson: section 2) Randomized Assignments}\\[1ex]
\end{center}

''' + questions + "\end{document}"

with open('randomized_147.tex', 'w') as f:
    f.write(document)

print(document)

#os.system("pdflatex randomized_147.tex")

#os.unlink("randomized_147.tex")
#os.unlink("randomized_147.log")