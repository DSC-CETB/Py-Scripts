import turtle
import random
from pygame import mixer
import time
import sys

ths='sounds/boom.wav'


def main():
	ff=True
	st=time.time()
	scr.bgcolor('pink')

	mixer.init()
	ths=mixer.Sound('sounds/boom.wav')
	walsound = mixer.Sound('sounds/wall.wav')
	padsound = mixer.Sound('sounds/wall.wav')
	
	#defining a single block
	a_blo=turtle.Turtle()
	a_blo.shape('square')
	a_blo.shapesize(1,3,2)
	a_blo.color(random.choice(['red','green','blue','cyan','magenta','purple','yellow']))
	a_blo.penup()
	a_blo.goto(-380,283)

	# function that creates a series of blocks
	l=[a_blo]
	def block(r,c):
		b_blo=turtle.Turtle()
		b_blo.shape('square')
		b_blo.speed(50)
		b_blo.shapesize(1,3,2)
		b_blo.color(random.choice(['red','green','blue',])) #'cyan','magenta','purple','yellow'
		b_blo.penup()
		b_blo.goto(a_blo.xcor()+(95*r),a_blo.ycor()-(50*c))
		#return b_blo()
		l.append(b_blo)

	#the bouncer
	bon=turtle.Turtle()
	bon.shape('square')
	bon.color('purple')
	bon.shapesize(1,7,2)
	bon.penup()
	bon.speed(100)
	bon.goto(0,-250)
	bon.speed(5)

	def right():
		x=bon.xcor()
		if x<=355:
			x+=20
		bon.setx(x)

	def left():
		x=bon.xcor()
		if x>=-355:
			x-=20
		bon.setx(x)

	def restart():
		scr.clearscreen()
		main()

	def stop():
		scr.clearscreen()
		scr.bye()
		sys.exit()

	#the ball
	bal=turtle.Turtle()
	bal.penup()
	bal.shape('circle')
	bal.color('red')
	bal.shapesize(1,1,1)
	bal.penup()
	# bal.right(86)
	bal.dx=4.0
	bal.dy=-4.0
	
	turtle.listen()
	scr.onkeypress(right,'Right')
	scr.onkeypress(left,'Left')
	turtle.onkeypress(restart,'r')
	scr.onkeypress(stop,'q')

	#creating the bricks
	for r in range(9):
		for c in range(5):
			block(r,c)
	while True:
		# hit with the paddle
		if int(bal.ycor())>=int(bon.ycor()+20) and int(bal.ycor())<=int(bon.ycor()+30) and bal.xcor()>=bon.xcor()-100 and bal.xcor()<=bon.xcor()+100:
			bal.sety(-215)
			bal.dy=-bal.dy
			# winsound.PlaySound('sounds/paddle.wav',winsound.SND_ASYNC)
			padsound.play()
			# mixer.music.play()

		# hit on right wall
		if int(bal.xcor())>=415:
			bal.setx(415)
			bal.dx*=-1
			# winsound.PlaySound('sounds/wall.wav',winsound.SND_ASYNC)
			# mixer.music.load(walsound)
			# mixer.music.play()
			walsound.play()

		#hit on left wall
		if int(bal.xcor())<=-415:
			bal.setx(-415)
			bal.dx*=-1
			# winsound.PlaySound('sounds/wall.wav',winsound.SND_ASYNC)
			# mixer.music.load(walsound)
			# mixer.music.play()
			walsound.play()
		# hit the roof 
		if int(bal.ycor())>=288:
			bal.sety(287)
			bal.dy*=-1
			# winsound.PlaySound('sounds/wall.wav',winsound.SND_ASYNC)
			# mixer.music.load(walsound)
			# mixer.music.play()
			walsound.play()
			#l[6].color('pink')
			#del l[6]
		#hit a brick
		for bri in l:
			if (bal.xcor()>=bri.xcor()-30 and bal.xcor()<=bri.xcor()+30) and (bal.ycor()>=bri.ycor()-10 and bal.ycor()<=bri.ycor()+10):
				bri.color('pink')
				bal.sety(bri.ycor())
				bal.dy*=-1
				try:
					l.remove(bri)
					# winsound.PlaySound(ths,winsound.SND_ASYNC)
					# mixer.music.load(ths)
					# mixer.music.play()
					ths.play()
					if len(l)==1:
						ths=mixer.Sound('sounds/Patt se headshot.wav')
				except ValueError:
					pass
			if ((bal.xcor()<=bri.xcor()-30 and bal.xcor()>=bri.xcor()-40 and bal.dx>0) or (bal.xcor()>=bri.xcor()+30 and bal.xcor()<=bri.xcor()+40 and bal.dx<0)) and (bal.ycor()>=bri.ycor()-5 and bal.ycor()<=bri.ycor()+5):
				bri.color('pink')
				bal.setx(bal.xcor())
				bal.dx*=-1
				try:
					l.remove(bri)
					# winsound.PlaySound(ths,winsound.SND_ASYNC)
					# mixer.music.load(ths)
					# mixer.music.play()
					ths.play()
					if len(l)==1:
						ths=mixer.Sound('sounds/Patt se headshot.wav')
				except ValueError:
					pass

		bal.setx(bal.xcor()+bal.dx)
		bal.sety(bal.ycor()+bal.dy)

		#check if the ball goes down
		if int(bal.ycor())<=-288:
			et=time.time()
			# winsound.PlaySound('sounds/paddle.wav',winsound.SND_ASYNC)
			# mixer.music.load(padsound)
			# mixer.music.play()
			# padsound.play()
			#scr.clearscreen()
			k=turtle.Turtle()
			k.ht()
			k.color('purple')
			k.write("GAME OVER",align="center",font=("Courier",44,"bold"))
			tt=turtle.Turtle()
			tt.penup()
			tt.ht()
			tt.color('red')
			tt.goto(0,-50)
			#res.sety(-100)
			if ff:
				tt.write("in {}s".format(int(et-st)),align='center',font=("Courier",24,"bold"))
				ff=False
			tt.goto(0,-50)
			res=turtle.Turtle()
			res.penup()
			res.ht()
			res.color('green')
			res.goto(0,-100)
			#res.sety(-100)
			res.write("Press R to restart",align='center',font=("Courier",24,"bold"))
			res.goto(0,-1000)
			#jff()


		# check if the game ends
		if len(l)==0:
			et=time.time()
			#scr.clear()
			bal.clear()
			k=turtle.Turtle()
			k.color('purple')
			k.ht()
			k.write("YOU WIN",align="center",font=("Courier",44,"bold"))
			tt=turtle.Turtle()
			tt.penup()
			tt.ht()
			tt.color('red')
			tt.goto(0,-50)
			#res.sety(-100)
			if ff:
				tt.write("in {}s".format(int(et-st)),align='center',font=("Courier",24,"bold"))
				ff=False
			tt.goto(0,-1000)
			res=turtle.Turtle()
			res.penup()
			res.ht()
			res.color('green')
			res.goto(0,-100)
			#res.sety(-100)
			res.write("Press R to restart",align='center',font=("Courier",24,"bold"))
			res.goto(0,-100)


	bal.home()

	scr.mainloop()

if __name__=='__main__':
	scr=turtle.Screen()
	scr.bgcolor('pink')
	scr.setup(870,600)
	main()