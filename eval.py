from tkinter import messagebox

#                  ^^^^
# Put your imports here ("from tkinter import messagebox" is important;
# do not change or delete it.)
maxeval = 30
for line in open("firsttime.shell.firstuse-v3.1.9"):
    firstuse = eval(line)
if firstuse:
    firstuse = False
    evaluation = maxeval + 1
    open("evaluation.shell.evaluation-v3.1.9", "w").write(str(evaluation))
    open("firsttime.shell.firstuse-v3.1.9", "w").write(str(firstuse))
for line in open("evaluation.shell.evaluation-v3.1.9"):
    evaluation = eval(line)
evaluation -= 1
open("evaluation.shell.evaluation-v3.1.9", "w").write(str(evaluation))
messagebox.showinfo("Evaluation", "You have {} uses left.".format(str(evaluation)))
if evaluation == 0:
    messagebox.showinfo("Evaluation Expiration",
                        "EXPIRED.\nPay for this app if you still need it.")
else:
    # Put your code here
