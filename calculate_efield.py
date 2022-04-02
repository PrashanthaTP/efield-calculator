#!/bin/env python3
# Description : Gui to Calculate Electric Field Due to multiple charges

#=========================modules======================================
from tkinter import *
from tkinter import Toplevel
from math import sqrt
import math
from tkinter.ttk import *
#==========================Constants======================================
e0=8.854187817*pow(10,-12)
use=1/(4*math.pi*e0)
#=================Creating to Window components and configuring its components========

def answer(event):
   top=Toplevel(root1)
   top.geometry("560x400+750+350")
   top.minsize(width=600, height=300)
   dist = Label(top, text="Distance ",font=("bold"))
   dist.grid(row=1, column=2)
   dist1 = Label(top, text="Distance of Q1 from reference point :")
   dist1.grid(row=3, column=1)
   dist2 = Label(top, text="Distance of Q2 from reference point :")
   dist2.grid(row=5, column=1)
   dist3 = Label(top, text="Distance of Q3 from reference point :")
   dist3.grid(row=7, column=1)
   d1=Label(top,text="")
   d1.grid(row=3,column=2)
   d2 = Label(top, text="")
   d2.grid(row=5, column=2)
   d3 = Label(top, text="")
   d3.grid(row=7, column=2)
   mag1=(entry1.get())
   mag2=(entry2.get())
   mag3=(entry3.get())
   if (mag1 == ""):
      m1 = (0.0)
   else:
      m1 = float(mag1)
   if (mag2 == ""):
      m2 = (0.0)
   else:
      m2= float(mag2)
   if (mag3 == ""):
      m3 = (0.0)
   else:
      m3 = float(mag3)

   a = (entry11X.get())
   b = (entry11Y.get())
   c = (entry11Z.get())
   x1=  (entry1X.get())
   y1 = (entry1Y.get())
   z1 = (entry1Z.get())
   x2 = (entry2X.get())
   y2 = (entry2Y.get())
   z2 = (entry2Z.get())
   x3 = (entry3X.get())
   y3 = (entry3Y.get())
   z3 = (entry3Z.get())
   if(a==""):
     aa=(0.0)
   else:
     aa=float(a)

   if (b == ""):
      bb = (0.0)
   else:
      bb = float(b)

   if (c == ""):
      cc = (0.0)
   else:
      cc = float(c)

   if (x1 == ""):
      xx1 =(0)
   else:
      xx1 = float(x1)

   if (y1 == ""):
      yy1 =(0.0)
   else:
      yy1 = float(y1)

   if (z1 == ""):
      zz1 =(0.0)
   else:
      zz1 = float(z1)
   if (x2 == ""):
      xa = (0)
   else:
      xa = float(x2)
   if (y2 == ""):
      ya = (0.0)
   else:
      ya = float(y2)

   if (z2 == ""):
      za = (0.0)
   else:
      za = float(z2)

   if (x3 == ""):
      xa1 = (0)
   else:
      xa1 = float(x3)

   if (y3 == ""):
    ya1 = (0.0)
   else:
      ya1 = float(y3)

   if (z3 == ""):
      za1 = (0.0)
   else:
      za1 = float(z3)

   s1=(aa-xx1)
   s2=(bb-yy1)
   s3=(cc-zz1)
   s4=(aa-xa)
   s5=(bb-ya)
   s6=(cc-za)
   s7=(aa-xa1)
   s8=(bb-ya1)
   s9=(cc-za1)
   sum1=((s1)**2)+ ((s2)**2) +((s3)**2)
   sqrt1=math.sqrt(sum1)
   d1.configure(text=" %.3f  meters"%sqrt1)
  
   sum2 = ((s4) ** 2)+ ((s5) ** 2 )+ ((s6) ** 2)
   sqrt2 = math.sqrt(sum2)
   d2.configure(text="  {0:.3f} meter".format(sqrt2))

   sum3 = ( (s7) ** 2) + ((s8)** 2) + ((s9) ** 2)
   sqrt3 = math.sqrt(sum3)
   d3.configure(text="  {0:.3f} meter".format(sqrt3))

   vector1=Label(top,text="--> Vector in this direction(Q1P)   :")
   vector1.grid(row=4,column=1)
   vector2 = Label(top, text="--> Vector in this direction(Q2P)   :")
   vector2.grid(row=6, column=1)
   vector3 = Label(top, text="--> Vector in this direction(Q3P)   :")
   vector3.grid(row=8, column=1)

   dv1 = Label(top, text="",  justify="left")
   dv1.grid(row=4, column=2)
   dv2 = Label(top, text="", justify="left")
   dv2.grid(row=6, column=2)
   dv3 = Label(top, text="", justify="left")
   dv3.grid(row=8, column=2)

   dv1.configure(text="({0:.2f}) Ax + ({1:.2f}) Ay + ({2:.2f}) Az".format((s1),(s2),(s3)))
   dv2.configure(text="({0:.2f}) Ax + ({1:.2f}) Ay + ({2:.2f}) Az".format((s4),(s5),(s6)))
   dv3.configure(text="({0:.2f}) Ax + ({1:.2f}) Ay + ({2:.2f}) Az".format((s7),(s8),(s9)))

   ef1 = Label(top, text="Electric Field due to Q1   :", justify="left")
   ef1.grid(row=10, column=1)
   ef2 = Label(top, text="Electric Field  due to Q2   :", justify="left")
   ef2.grid(row=11, column=1)
   ef3 = Label(top, text="Electric Field due to Q3   :",  justify="left")
   ef3.grid(row=12, column=1)

   e1 = Label(top, text="", justify="left")
   e1.grid(row=10, column=2)
   e2 = Label(top, text="" ,justify="left")
   e2.grid(row=11, column=2)
   e3 = Label(top, text="" ,justify="left")
   e3.grid(row=12, column=2)

   if(m1!=0.0 and sum1!=0):
     E1x = (use * m1*s1)/((sum1)**(3/2))
     E1y = (use * m1*s2)/((sum1)**(3/2))
     E1z = (use * m1*s3)/((sum1)**(3/2))
     e1.configure(text="({0:.3f}) Ax + ({1:.3f}) Ay + ({2:.3f}) Az N/C".format((E1x), (E1y), (E1z)))
   else:
      E1x = 0
      E1y = 0
      E1z = 0
      e1.configure(text="-----")
      dv1.configure(text="-----")
      d1.configure(text="-----")

   if(m2!=0.0 and sum2!=0):
     E2x = (use * m2*s4)/((sum2)**(3/2))
     E2y = (use * m2*s5)/((sum2)**(3/2))
     E2z =( use * m2*s6)/((sum2)**(3/2))
     e2.configure(text="({0:.3f}) Ax + ({1:.3f}) Ay + ({2:.3f}) Az N/C".format((E2x), (E2y), (E2z)))
   else:
      E2x = 0
      E2y = 0
      E2z = 0
      e2.configure(text="-----")
      dv2.configure(text="-----")
      d2.configure(text="-----")

   if((m3!=0.0) and (sum3!=0)):
      E3x = (use * m3*s7)/((sum3)**(3/2))
      E3y =( use * m3*s8)/((sum3)**(3/2))
      E3z = (use * m3*s9)/((sum3)**(3/2))
      e3.configure(text="({0:.3f}) Ax + ({1:.3f}) Ay + ({2:.3f}) Az N/C".format((E3x), (E3y), (E3z)))
   else:
       E3x = 0
       E3y = 0
       E3z = 0
       e3.configure(text="-----")
       dv3.configure(text="-----")
       d3.configure(text="-----")

   Eheading=Label(top,text="Electric field ",font=("bold"))
   Eheading.grid(row=9,column=2)

   
   fa=Label(top,text=" * Total Electric field    :")
   fa.grid(row=13, column=1)
   faa = Label(top,text="")
   faa.grid(row=13, column=2)

   faa.configure(text="({0:.3f}) Ax + ({1:.3f}) AY + ({2:.3f}) Az N/C".format((E1x+E2x+E3x),(E1y+E2y+E3y),(E1z+E2z+E3z)))


   fsum=(E1x+E2x+E3x)**2 + (E1y+E2y+E3y)**2 + (E1z+E2z+E3z)**2
   fm=Label(top,text="* magnitude   :")
   fm.grid(row=14,column=1)
   fs=Label(top,text=("{0:.3f} N/C".format(math.sqrt(fsum))))
   fs.grid(row=14,column=2)

   if((E1x+E2x+E3x)!=0 or (E1y+E2y+E3y)!=0 or (E1z+E2z+E3z)!=0):
    fdx= (E1x+E2x+E3x)/math.sqrt(fsum)
    fdy = (E1y + E2y + E3y) / math.sqrt(fsum)
    fdz = (E1z + E2z + E3z) / math.sqrt(fsum)
    fdir = Label(top, text="* Direction   :")
    fdir.grid(row=15, column=1)
    fd = Label(top, text=("({0:.3f}) Ax + ({1:.3f}) Ay + ({2:.3f}) Az N/C".format((fdx),(fdy),(fdz))))
    fd.grid(row=15, column=2)

#================================Creating the main window===================
root1=Tk()
root1.title('ELECTRIC FIELD (CARTESIAN SYSTEM)')
root1.geometry("1000x700+70+150")
root1.maxsize(width=1200,height=300)
root1.minsize(width=1000,height=300)
#======================================================================
var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()
var8=StringVar()
var9=StringVar()
var10=StringVar()
var11=StringVar()
var12=StringVar()
var13=StringVar()
var14=StringVar()
var15=StringVar()

#===================Label and Entry widgets of main window=====================
Name=Label(text="ELECTRIC FIELD due to Multiple Charges")
Name.grid(row=0,column=3)
position=Label(root1,text="Pointat  which field strength has to be found(P)",width=45,relief=RAISED)
position.grid(row=1,column=2)

xxx=Label(root1,text=" X= ",relief=RAISED)          
xxx.place(x=429,y=20)
yyy=Label(root1,text=" Y= ",relief=RAISED)
yyy.grid(row=1,column=4)
zzz=Label(root1,text=" Z= ",relief=RAISED)
zzz.grid(row=1,column=6)

entry11X = Entry(root1, textvariable=var1)
entry11X.grid(row=1, column=3)
var1.set("0.0")

entry11Y= Entry(root1,textvariable=var2)
entry11Y.grid(row=1, column=5)
var2.set("0.0")

entry11Z= Entry(root1,textvariable=var3)
entry11Z.grid(row=1, column=7)
var3.set("0.0")

#mag.grid(row=2,column=2)
xx=Label(root1,text="Position in X direction")
xx.grid(row=2,column=3)                                  #Labels for magitude, x axis postion, y axis position and
yy=Label(root1,text="Position in Y direction")           #z axis postion
yy.grid(row=2,column=5)
zz=Label(root1,text="Position in Z direction")
zz.grid(row=2,column=7)
#=======================================================================
AnsButton=Button(root1,text=" Answer ",width=20)       #Button for getting the answer
AnsButton.place(x=500,y=200)

AnsButton.bind("<Button-1>",answer)
#=======================================================================
Charge1=Label(root1,text=" Charge 1 (in Coulombs)",width=22,relief=SUNKEN)
Charge1.grid(row=3,sticky=E)
Charge11 = Label(root1, text="X",  width=6, relief=FLAT)
Charge2 = Label(root1, text=" Charge 2 (in Coulombs)",   width=22,  relief=SUNKEN)
Charge2.grid(row=4, sticky=E)
Charge3 = Label(root1, text=" Charge 3 (in Coulombs)", width=22,relief=SUNKEN)
Charge3.grid(row=5, sticky=E)   
entry1=Entry(root1,textvariable=var4)              #entry widgets for magnitude of charges
entry1.grid(row=3,column=2)
var4.set("0.0")
entry2 = Entry(root1,textvariable=var5)
entry2.grid(row=4, column=2)
var5.set("0.0")
entry3 = Entry(root1,textvariable=var6)
entry3.grid(row=5, column=2)
var6.set("0.0")
entry1X = Entry(root1, textvariable=var7)
entry1X.grid(row=3, column=3)
var7.set("0.0")
entry1Y= Entry(root1, textvariable=var8)
entry1Y.grid(row=3, column=5)
var8.set("0.0")
entry1Z= Entry(root1,textvariable=var9)
entry1Z.grid(row=3, column=7)
var9.set("0.0")
entry2X = Entry(root1,textvariable=var10)
entry2X.grid(row=4, column=3)
var10.set("0.0")
entry2Y= Entry(root1, textvariable=var11)
entry2Y.grid(row=4, column=5)
var11.set("0.0")
entry2Z= Entry(root1, textvariable=var12)
entry2Z.grid(row=4, column=7)
var12.set("0.0")
entry3X = Entry(root1,textvariable=var13)
entry3X.grid(row=5, column=3)
var13.set("0.0")
entry3Y= Entry(root1,textvariable=var14)
entry3Y.grid(row=5, column=5)
var14.set("0.0")
entry3Z= Entry(root1,textvariable=var15)
entry3Z.grid(row=5, column=7)
var15.set("0.0")

root1.mainloop()
