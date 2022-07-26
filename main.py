
####Firstly import and initialize TKInter
from tkinter import *
from maths import Math
from physics import Physics

maths = Math()
physics = Physics()

#Create an instance of tkinter frame
window = Tk()
###I also set the size of the app, its title and a background color
window.geometry('500x300')
window.title("CMP")
window.configure(background="grey")


########################   MATH CLASS  ##################################
def run_math():
    window2 = Toplevel()
    window2.geometry('300x200')
    def areaoftriangle():
        def findareaoftriangle():

            ## the .insert means to get characters within a given range

            par.insert(0, str(maths.areaoftriangle(int(base.get()), int(height.get()))))

        triangle_area = Toplevel()

#########labels and input fields to read the entered numbers

        Label(triangle_area,
              text="Input your base",
              font="Helvetica 20 bold").grid(row=0, column=0)
        base = Entry(triangle_area)
        base.grid(row=0, column=1, pady=10)

        Label(triangle_area,
              text="Input your height",
              font="Helvetica 20 bold").grid(row=1, column=0)
        height = Entry(triangle_area)
        height.grid(row=1, column=1)

        Button(triangle_area, text="AREA OF TRIANGLE",
               font="Helvetica 20 bold",
               command=findareaoftriangle).grid(row=2, column=0)
        par = Entry(triangle_area)
        par.grid(row=2, column=1)


    def areaofcylinder():
        def findareaofcylinder():
            cyl.insert(0, str(maths.areaofcylinder(int(length.get()), int(width.get()))))

        cylinder_area = Toplevel()

        Label(cylinder_area,
              text="Input your length",
              font="Helvetica 20 bold").grid(row=0, column=0)
        length = Entry(cylinder_area)
        length.grid(row=0, column=1)

        Label(cylinder_area,
              text="Input your width",
              font="Helvetica 20 bold").grid(row=1, column=0)
        width = Entry(cylinder_area)
        width.grid(row=1, column=1)

        Button(cylinder_area,
               text="AREA OF CYLINDER:",
               font="Helvetica 20 bold",
               command=findareaofcylinder).grid(row=2, column=0)
        cyl = Entry(cylinder_area)
        cyl.grid(row=2, column=1)


    def volumeofcone():
        def findvolumeofcone():
            con.insert(0, str(maths.volumeofcone(int(radius.get()), int(length.get()))))

        cone_volume = Toplevel()

        Label(cone_volume,
              text="Input your radius",
              font="Helvetica 20 bold").grid(row=0, column=0)
        radius = Entry(cone_volume)
        radius.grid(row=0, column=1)

        Label(cone_volume,
              text="Input your height",
              font="Helvetica 20 bold").grid(row=1, column=0)
        length = Entry(cone_volume)
        length.grid(row=1, column=1)

        Button(cone_volume, text="VOLUME OF CONE:",
               font="Helvetica 20 bold",
               command=findvolumeofcone).grid(row=2, column=0)
        con = Entry(cone_volume)
        con.grid(row=2, column=1)

    def areaofrectangle():
        def findareaofrectangle():
            rectangle_area.insert(0, str(maths.areaofrectangle(int(length.get()), int(breadth.get()))))

        rectangle_area = Toplevel()

        Label(rectangle_area,
              text="Input your length",
              font="Helvetica 20 bold").grid(row=0, column=0)
        length = Entry(rectangle_area)
        length.grid(row=0, column=1)

        Label(rectangle_area,
              text="Input your breadth",
              font="Helvetica 20 bold").grid(row=1, column=0)
        breadth = Entry(rectangle_area)
        breadth.grid(row=1, column=1)

        Button(rectangle_area,
               text="AREA OF RECTANGLE",
               font="Helvetica 20 bold",
               command=findareaofrectangle).grid(row=2, column=0)
        rectangle_area = Entry(rectangle_area)
        rectangle_area.grid(row=2, column=1)

    window2.configure(background="grey")
    Label(master=window2, bg="#339966", fg="pink").grid(row=0, column=0)
    Button(window2,
           text="AREA OF TRIANGLE",
           bg="#339966",
           fg="white",
           font="Helvetica 20 bold",
           command=areaoftriangle).grid(row=0, column=0, pady=10)

    Button(window2,
           text="AREA OF CYLINDER",
           bg="#339966",
           fg="white",
           font="Helvetica 20 bold",
           command=areaofcylinder).grid(row=1, column=0, pady=10)

    Button(window2,
           text="VOLUME OF CONE",
           bg="#339966",
           fg="white",
           font="Helvetica 20 bold",
           command=volumeofcone).grid(row=2, column=0, pady=10)

    Button(window2,
           text="AREA OF RECTANGLE",
           bg="#339966",
           fg="white",
           font="Helvetica 20 bold",
           command=areaofrectangle).grid(row=3, column=0, pady=10)


########################### PHYSICS CLASS ###########################
def clicked_physics():
    window3 = Toplevel()
    window3.geometry('500x200')

    def speed():
        def findspeed():
            top.insert(0, str(physics.speed(int(distance.get()), int(time.get()))))

        pot = Toplevel()
        Label(pot, text="Input your Distance:", font="Helvetica 20 bold").grid(row=0, column=0)
        distance = Entry(pot)
        distance.grid(row=0, column=1)

        Label(pot, text="Input your Time:", font="Helvetica 20 bold").grid(row=1, column=0)
        time = Entry(pot)
        time.grid(row=1, column=1)

        Button(pot, text="SPEED:", font="Helvetica 20 bold", command=findspeed).grid(row=2, column=0)
        top = Entry(pot)
        top.grid(row=2, column=1)

    def workdone():
        def findworkdone():
            top.insert(0, str(physics.workdone(int(force.get()), int(distance.get()))))

        pot = Toplevel()
        Label(pot, text="Input your Force:", font="Helvetica 20 bold").grid(row=0, column=0)
        force = Entry(pot)
        force.grid(row=0, column=1)

        Label(pot, text="Input your Distance:", font="Helvetica 20 bold").grid(row=1, column=0)
        distance = Entry(pot)
        distance.grid(row=1, column=1)

        Button(pot, text="WORKDONE:", font="Helvetica 20 bold", command=findworkdone).grid(row=2, column=0)
        top = Entry(pot)
        top.grid(row=2, column=1)

    def potentialenergy():
        def findpotentialenergy():
            top.insert(0, str(physics.potentialenergy(int(mass.get()), int(height.get()))))

        pot = Toplevel()

        Label(pot, text="Input your Mass:", font="Helvetica 20 bold").grid(row=0, column=0)
        mass = Entry(pot)
        mass.grid(row=0, column=1)

        Label(pot, text="Input your Height:", font="Helvetica 20 bold").grid(row=1, column=0)
        height = Entry(pot)
        height.grid(row=1, column=1)

        Button(pot, text="POTENTIAL ENERGY:", font="Helvetica 20 bold", command=findpotentialenergy).grid(row=2, column=0)
        top = Entry(pot)
        top.grid(row=2, column=1)

    def kineticenergy():
        def findkineticenergy():
            top.insert(0, str(physics.kineticenergy(int(mass.get()), int(velocity.get()))))

        pot = Toplevel()

        Label(pot, text="Input your Mass:", font="Helvetica 20 bold").grid(row=0, column=0)
        mass = Entry(pot)
        mass.grid(row=0, column=1)

        Label(pot, text="Input your Velocity:", font="Helvetica 20 bold").grid(row=1, column=0)
        velocity = Entry(pot)
        velocity.grid(row=1, column=1)

        Button(pot, text="KINETIC ENERGY:", font="Helvetica 20 bold", command=findkineticenergy).grid(row=2, column=0)
        top = Entry(pot)
        top.grid(row=2, column=1)

    window3.configure(background="grey")
    Button(window3, text="SPEED", bg="#339966", fg="white", font="Helvetica 45 bold", command=speed).grid(row=1, column=0, pady=10)
    Button(window3, text="WORKDONE", bg="#339966", fg="white", font="Helvetica 45 bold", command=workdone).grid(row=3, column=0, pady=10)
    Button(window3, text="POTENTIAL ENERGY", bg="#339966", fg="white", font="Helvetica 45 bold", command=potentialenergy).grid(row=4, column=0, pady=10, padx=5)
    Button(window3, text="KINETIC ENERGY", bg="#339966", fg="white", font="Helvetica 45 bold", command=kineticenergy).grid(row=5, column=0, pady=10)

Label(master=window,
      text="Math OR Physics?",
      bg="#0000FF",
      fg="white",
      font="Helvetica 45 bold"). grid(row=0, column=1, padx=60, pady=20)

Button(master=window,
       text="MATH",
       bg="#0000FF",
       fg="white",
       font="Helvetica 45 bold",
       command=run_math). grid(row=1, column=1, pady=30, padx=80)

Button(master=window,
       text="PHYSICS",
       bg="#0000FF",
       fg="white",
       font="Helvetica 45 bold",
       command=clicked_physics). grid(row=2, column=1, pady=10)

window.mainloop()
###########we run .mainloop() so that our application won’t stop immediately after execution.


#########The command parameter to Button function calls the call_function, which does the simple logic.
#########Then I add a button, when clicked, calculates the result and displays it in the label labelResult I initialized above.
########So when the button is clicked, a function is called which calculates the desired formula of both the numbers.
########Here I used, grid layout for designing the layout, rather than pack() which sets the widgets
##################automatically based on available space in the window, but here we can set the widgets where we want to place

