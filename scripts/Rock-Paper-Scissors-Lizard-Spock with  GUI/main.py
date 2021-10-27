# libraries imported#
from tkinter import *
from PIL import Image, ImageTk
from random import randint
# first window#
def firstwindow():
    root.withdraw()
    firstwin=Toplevel()
    label1 = Label(firstwin, text="The Game of\nChances", bg="Lime", fg="red", font=("Comic Sans MS", 22, "bold"),padx=0, pady=0)
    label1.pack()
    # enter name#
    entrname=Label(firstwin, text="Enter Name", bg="Silver", fg="black", font=("Comic Sans MS", 12, "bold"))
    entry1 = Entry(firstwin, font=("Comic Sans MS", 12, "bold"))
    # entry1.insert(0, "Name Here.....")
    label1.grid(row=0, column=0,columnspan=4)
    entrname.grid(row=1, column=0, columnspan=2)
    entry1.grid(row=1, column=2, columnspan=2)

    # button to call second window#

    btn = Button(firstwin, width=14, height=2, text="Start", bg="blue", fg="white",
                 command=lambda: second_win(entry1.get()))
    btn.grid(row=2, column=2)

    # second window#
    def second_win(uname):
        window = Toplevel()
        window.title("The game of Chances")
        window.configure(background="aqua")
        username = uname
        if username=="":
            username="Player"

        # closing first window#
        firstwin.destroy()
        # importing images#
        image_rock1 = ImageTk.PhotoImage(Image.open("./image/rock.png"))
        image_paper1 = ImageTk.PhotoImage(Image.open("./image/paper.png"))
        image_scissor1 = ImageTk.PhotoImage(Image.open("./image/scissor.png"))
        image_spock1= ImageTk.PhotoImage(Image.open("./image/spock.png"))
        image_lizard1=ImageTk.PhotoImage(Image.open("./image/lizard.png"))
        image_rock2 = ImageTk.PhotoImage(Image.open("./image/rock.png"))
        image_paper2 = ImageTk.PhotoImage(Image.open("./image/paper.png"))
        image_scissor2 = ImageTk.PhotoImage(Image.open("./image/scissor.png"))
        image_spock2 = ImageTk.PhotoImage(Image.open("./image/spock.png"))
        image_lizard2 = ImageTk.PhotoImage(Image.open("./image/lizard.png"))

        # creating image label for user and computer#
        label_computer = Label(window, image=image_scissor2)
        label_user = Label(window, image=image_scissor1)
        label_computer.grid(row=2, column=5, rowspan=4)
        label_user.grid(row=2, column=1, rowspan=4)

        # infolabel=Label(window, text="If you lose thrice! Gameover !", font=("Comic Sans MS", 12, "bold"),bg="green",fg="white",padx=10, pady=10)
        # infolabel.grid()
        # labels to display score#
        computer_score = Label(window, text=0, font=("Comic Sans MS", 20, "bold"), fg="red",bg="green" )
        user_score = Label(window, text=0, font=("Comic Sans MS", 20, "bold"), fg="blue", bg="green")



        computer_indi = Label(window, text="computer",font=("Comic Sans MS", 16, "bold"),padx=10, pady=10,bg="Navy",fg="yellow")
        user_indi1 = Label(window, text=username,font=("Comic Sans MS", 16, "bold"), padx=10, pady=10,bg="Navy",fg="yellow")
        computer_indi.grid(row=0, column=5)
        user_indi1.grid(row=0, column=1)
        user_indi2 = Label(window, text=username+"=> 0", font=("Comic Sans MS", 16, "bold"), padx=10, pady=10, bg="Navy",
                           fg="yellow")
        user_indi2.grid(row=6, column=1)
        computer_indi2 = Label(window, text="computer=> 0", font=("Comic Sans MS", 16, "bold"), padx=10, pady=10, bg="Navy",
                              fg="yellow")

        computer_indi2.grid(row=6, column=5)

        # updating who won#
        def msg_update(a):
            final_msg['text'] = a

        # updating computer score#
        def comp_update():
            finalc = int(computer_score['text'])
            finalc += 1
            computer_score["text"] = str(finalc)
            computer_indi2["text"]= "computer => "+str(finalc)


            def gameover(xyz):
                # creating third window#
                win = Toplevel()
                if xyz==0:
                    userfinalscore = "0"
                else:
                    userfinalscore = xyz
                # destroying second window
                window.destroy()
                win.title("The game of Chances")
                win.configure(background="blue")
                # label to display score
                userfscore = Label(win, text="Gameover!\n"+ username +"'s score is " + userfinalscore, bg="yellow", fg="red", font=("Comic Sans MS", 16, "bold"),padx=40, pady=10)
                userfscore.grid(row=0, column=0, columnspan=2)
                # quit button which closes root window
                quitbtn = Button(win, text="Exit",width=14, height=2,bg="red", fg="white", command=lambda: root.destroy())
                quitbtn.grid(row=1, column=0)

                # restart button which opens fisrt window and closes third window
                def restartfunc():
                    firstwindow()
                    win.destroy()
                # restart button
                restartbtn = Button(win, text="Start New Game",width=14,height=2,bg="grey",fg="black",command=lambda: restartfunc())
                restartbtn.grid(row=1, column=1)
            # if user loses thrice calling game over func#
            if finalc == 3:
                # disabling buttons
                button_rock.configure(state='disabled')
                button_paper.configure(state='disabled')
                button_scissor.configure(state='disabled')
                button_spock.configure(state='disabled')
                button_lizard.configure(state='disabled')
                final_msg['text'] = "Game Over"
                userscr=user_score.cget("text")
                def gameovr():
                    # calling gameover function
                    gameover(userscr)

                def delay():
                    window.after(2000, gameovr)
                delay()

        # user score update
        def user_update():
            finalu = int(user_score['text'])
            finalu += 1
            user_score["text"] = str(finalu)
            user_indi2["text"]=username+"=> "+str(finalu)


        # logic to check the result
        def winner_check(p, c):
            if p == c:
                msg_update("IT'S A Tie !")
            elif p == "rock":
                if c == "paper":
                    msg_update("computer wins")
                    comp_update()
                elif c== "spock":
                    msg_update("computer wins")
                    comp_update()
                else:
                    msg_update(username + " wins")
                    user_update()
            elif p == "paper":
                if c == "scissor":
                    msg_update("computer wins")
                    comp_update()
                elif c== "lizard":
                    msg_update("computer wins")
                    comp_update()
                else:
                    msg_update(username + " wins")
                    user_update()
            elif p == "scissor":
                if c == "rock":
                    msg_update("computer wins")
                    comp_update()
                elif c== "spock":
                    msg_update("computer wins")
                    comp_update()
                else:
                    msg_update(username + " wins")
                    user_update()
            elif p == "spock":
                if c == "paper":
                    msg_update("computer wins")
                    comp_update()
                elif c== "lizard":
                    msg_update("computer wins")
                    comp_update()
                else:
                    msg_update(username + " wins")
                    user_update()
            elif p == "lizard":
                if c == "rock":
                    msg_update("computer wins")
                    comp_update()
                elif c== "scissor":
                    msg_update("computer wins")
                    comp_update()
                else:
                    msg_update(username + " wins")
                    user_update()
            else:
                pass

        # comp to select randomly from available options
        to_select = ["rock", "paper", "scissor", "spock", "lizard"]

        def choice_update(a):
            # assigning images to available options
            choice_computer = to_select[randint(0, 4)]
            if choice_computer == "rock":
                label_computer.configure(image=image_rock2)
            elif choice_computer == "paper":
                label_computer.configure(image=image_paper2)
            elif choice_computer == "scissor":
                label_computer.configure(image=image_scissor2)
            elif choice_computer == "spock":
                label_computer.configure(image=image_spock2)
            else:
                label_computer.configure(image=image_lizard2)

            if a == "rock":
                label_user.configure(image=image_rock1)
            elif a == "paper":
                label_user.configure(image=image_paper1)
            elif a == "scissor":
                label_user.configure(image=image_scissor1)
            elif a == "spock":
                label_user.configure(image=image_spock1)
            else:
                label_user.configure(image=image_lizard1)
            winner_check(a, choice_computer)

        # label to display result after every round
        final_msg = Label(window, text="Vs", bg="green", fg="pink", font=("Comic Sans MS", 12, "bold"), padx=20)
        final_msg.grid(row=3, column=2)

        # buttons for stone , paper, scissor, spock, lizard
        button_rock = Button(window, width=9, height=2, text="ROCK", bg="red", fg="white", padx=8, pady=8,
                             command=lambda: choice_update("rock"),font=("Comic Sans MS", 12, "bold"))
        button_rock.grid(row=1, column=0)
        button_rock.configure(state='normal')
        button_paper = Button(window, width=9, height=2, text="PAPER", bg="red", fg="white", padx=8, pady=8,
                              command=lambda: choice_update("paper"), font=("Comic Sans MS", 12, "bold"))
        button_paper.grid(row=2, column=0)
        button_paper.configure(state='normal')
        button_scissor = Button(window, width=9, height=2, text="SCISSOR", bg="red", fg="white", padx=8, pady=8,
                                command=lambda: choice_update("scissor"), font=("Comic Sans MS", 12, "bold"))
        button_scissor.grid(row=3, column=0)
        button_scissor.configure(state='normal')
        button_spock = Button(window, width=9, height=2, text="SPOCK", bg="red", fg="white", padx=8, pady=8,
                                command=lambda: choice_update("spock"), font=("Comic Sans MS", 12, "bold"))
        button_spock.grid(row=4, column=0)
        button_spock.configure(state='normal')
        button_lizard = Button(window, width=9, height=2, text="LIZARD", bg="red", fg="white", padx=8, pady=8,
                                command=lambda: choice_update("lizard"), font=("Comic Sans MS", 12, "bold"))
        button_lizard.grid(row=5, column=0)
        button_lizard.configure(state='normal')
        points = Label(window, text="Points=>", bg="yellow", fg="red",
                           font=("Comic Sans MS", 18, "bold"), padx=10, pady=10)
        points.grid(row=6, column=0)
        # buttons for stone , paper, scissor, spock, lizard for computer
        button_rock1 = Button(window, width=9, height=2, text="ROCK", bg="red", fg="white", padx=8, pady=8,
                             command=lambda: choice_update("rock"), font=("Comic Sans MS", 12, "bold"))
        button_rock1.grid(row=1, column=6)
        button_rock1.configure(state='disabled')
        button_paper1 = Button(window, width=9, height=2, text="PAPER", bg="red", fg="white", padx=8, pady=8,
                              command=lambda: choice_update("paper"), font=("Comic Sans MS", 12, "bold"))
        button_paper1.grid(row=2, column=6)
        button_paper1.configure(state='disabled')
        button_scissor1 = Button(window, width=9, height=2, text="SCISSOR", bg="red", fg="white", padx=8, pady=8,
                                command=lambda: choice_update("scissor"), font=("Comic Sans MS", 12, "bold"))
        button_scissor1.grid(row=3, column=6)
        button_scissor1.configure(state='disabled')
        button_spock1 = Button(window, width=9, height=2, text="SPOCK", bg="red", fg="white", padx=8, pady=8,
                              command=lambda: choice_update("spock"), font=("Comic Sans MS", 12, "bold"))
        button_spock1.grid(row=4, column=6)
        button_spock1.configure(state='disabled')
        button_lizard1 = Button(window, width=9, height=2, text="LIZARD", bg="red", fg="white", padx=8, pady=8,
                               command=lambda: choice_update("lizard"), font=("Comic Sans MS", 12, "bold"))
        button_lizard1.grid(row=5, column=6)
        button_lizard1.configure(state='disabled')
        points1 = Label(window, text="<=Points", bg="yellow", fg="red",
                       font=("Comic Sans MS", 18, "bold"), padx=10, pady=10)
        points1.grid(row=6, column=6)


#The root window

root=Tk()
root.title("The Game of Chances")
#calling the first window
firstwindow()
root.mainloop()