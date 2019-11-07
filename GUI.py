# MIT License

# Copyright(c)2019 Saksham

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files(the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from tkinter import *
from forceClass import forcePoint, forceUDL, forceUVL
from calculatingForce import simpleSupported, cantilever, oneHingedOtherRoller
from PIL import Image, ImageTk

window = Tk()
window.geometry("750x750")
# window.resizable(0, 0)
window.title("Support Reaction Calculator")
v = IntVar()
flippedVariable = IntVar()


class guiForce:
    secs = ['Point Force', 'UDL Force', 'UVL Force']

    def __init__(self, window, startpoint, forceNo):
        self.v = StringVar(window)
        self.v.set(self.secs[0])
        self.x = startpoint

        Label(window, text="Force {} Configration".format(
            forceNo), font=('Arial', 12)).grid(row=self.x, column=1, padx=15, pady=5, sticky=E)
        self.forceConfigPoint = Frame(window)
        self.forceConfigPoint.grid(row=self.x+1, column=1)
        #  Force Type
        Label(self.forceConfigPoint, text="Force Type is").grid(
            row=0, column=0, padx=4, pady=2, sticky=E)
        OptionMenu(self.forceConfigPoint, self.v, *self.secs, command=self.on_option_change).grid(row=0,
                                                                                                  column=1, sticky=W, padx=4, pady=2)
        #  Magnitude
        Label(self.forceConfigPoint, text="Magnitude =").grid(
            row=1, column=0, padx=4, pady=2, sticky=E)
        Label(self.forceConfigPoint, text="N").grid(
            row=1, column=2, pady=2)
        self.magnitudeP = Entry(self.forceConfigPoint, justify=RIGHT)
        self.magnitudeP.grid(row=1, column=1, padx=4, pady=2)
        #  Angle
        Label(self.forceConfigPoint, text="Angle =").grid(
            row=2, column=0, padx=4, pady=2, sticky=E)
        Label(self.forceConfigPoint, text="°").grid(
            row=2, column=2, pady=2)
        self.angleP = Entry(self.forceConfigPoint, justify=RIGHT)
        self.angleP.grid(row=2, column=1, padx=4, pady=2)
        # Distance
        Label(self.forceConfigPoint, text="Application distance =").grid(
            row=3, column=0, padx=4, pady=2)
        Label(self.forceConfigPoint, text="m").grid(
            row=3, column=2, pady=2, sticky=W)
        self.distanceP = Entry(self.forceConfigPoint, justify=RIGHT)
        self.distanceP.grid(row=3, column=1, padx=4, pady=2)

        self.forceConfigUniform = Frame(window)
        Label(self.forceConfigUniform, text="Force Type is").grid(
            row=0, column=0, padx=4, pady=2, sticky=E)
        OptionMenu(self.forceConfigUniform, self.v, *self.secs,
                   command=self.on_option_change).grid(row=0, column=1, sticky=W, padx=4, pady=2)

        #  Magnitude
        Label(self.forceConfigUniform, text="Maximum Magnitude =").grid(
            row=1, column=0, padx=4, pady=2, sticky=E)
        Label(self.forceConfigUniform, text="N").grid(
            row=1, column=2, pady=2)
        self.magnitudeU = Entry(self.forceConfigUniform, justify=RIGHT)
        self.magnitudeU.grid(row=1, column=1, padx=4, pady=2)
        #  Spread
        Label(self.forceConfigUniform, text="Spread of force =").grid(
            row=2, column=0, padx=4, pady=2, sticky=E)
        Label(self.forceConfigUniform, text="m").grid(
            row=2, column=2, pady=2)
        self.spreadU = Entry(self.forceConfigUniform, justify=RIGHT)
        self.spreadU.grid(row=2, column=1, padx=4, pady=2)
        # Distance
        Label(self.forceConfigUniform, text="Application distance =").grid(
            row=3, column=0, padx=4, pady=2, sticky=E)
        Label(self.forceConfigUniform, text="m").grid(
            row=3, column=2, pady=2, sticky=W)
        self.distanceU = Entry(self.forceConfigUniform, justify=RIGHT)
        self.distanceU.grid(row=3, column=1, padx=4, pady=2)
        Checkbutton(self.forceConfigUniform, text='Flipping the orientation about y-axis', variable=flippedVariable).grid(
            row=4, column=0, columnspan=2)

    def on_option_change(self, event):
        if (self.v.get() == "Point Force"):
            self.forceConfigPoint.grid(row=self.x+1, column=1)
            self.forceConfigUniform.grid_forget()
        if not (self.v.get() == "Point Force"):
            self.forceConfigPoint.grid_forget()
            self.forceConfigUniform.grid(row=self.x+1, column=1)

    def getValues(self):
        try:
            if (self.v.get() == "Point Force"):
                self.forceOut = forcePoint()
                self.forceOut.magnitude(float(self.magnitudeP.get()))
                self.forceOut.angle(float(self.angleP.get()))
                self.forceOut.distanceX(float(self.distanceP.get()))
            elif (self.v.get() == "UDL Force"):
                self.forceOut = forceUDL()
                self.forceOut.magnitude(
                    float(self.magnitudeU.get()), float(self.spreadU.get()))
                self.forceOut.distanceX(float(self.distanceU.get()))
            else:
                self.forceOut = forceUVL()
                self.forceOut.magnitude(
                    float(self.magnitudeU.get()), float(self.spreadU.get()))
                self.forceOut.distanceX(float(self.distanceU.get()))
                self.forceOut.orientation(
                    bool(flippedVariable.get() == 1))  # todo
        except:
            pass
        return self.forceOut


result = Frame(window)


def calculate():
    global result
    result.destroy()
    result = Frame(window)
    result.grid(row=5, column=2, rowspan=10)
    if v.get() is 1:
        # print("Simple Supported", )
        aVertical, bVertical, balanced, excess = simpleSupported([force1.getValues(),
                                                                  force2.getValues(), force3.getValues(), force4.getValues()], float(beamWidth.get()))
        Label(result, text="\tResult", font=('Arial', 10, 'bold')).grid(
            row=0, column=1, columnspan=3)
        if(balanced):
            Label(result, text="\tVertical Reaction at support A is ").grid(
                row=1, column=2)
            Label(result, text=str(aVertical)+" N").grid(row=1, column=3)
            Label(result, text="\tVertical Reaction at support B is ").grid(
                row=2, column=2)
            Label(result, text=str(bVertical)+" N").grid(row=2, column=3)
        else:
            Label(result, text="\tWARNING! - Beam not in equilibrium ", font=('Arial', 12, 'bold')).grid(
                row=1, column=2, columnspan=2)
            Label(result, text="\tSystem has excess horizontal force ->").grid(
                row=2, column=2, sticky=E)
            Label(result, text=str(excess) +
                  " N").grid(row=2, column=3, sticky=W)
    elif v.get() is 2:
        # print("Cantilever", )
        aVertical, aHorizontal, aMoment = cantilever([force1.getValues(),
                                                      force2.getValues(), force3.getValues(), force4.getValues()])
        Label(result, text="\tResult", font=('Arial', 10, 'bold')).grid(
            row=0, column=1, columnspan=3)
        Label(result, text="\tVertical Reaction at support A is ").grid(
            row=1, column=2)
        Label(result, text=str(aVertical)+" N").grid(row=1, column=3)
        Label(result, text="\tHorizontal Reaction at support A is ").grid(
            row=2, column=2)
        Label(result, text=str(aHorizontal)+" N").grid(row=2, column=3)
        Label(result, text="\tMoment Reaction at support A is ").grid(
            row=3, column=2)
        Label(result, text=str(aMoment)+" N").grid(row=3, column=3)
    elif v.get() is 3:
        # print("One end hinged other on roller",)
        aVertical, aHorizontal, bVertical = oneHingedOtherRoller([force1.getValues(),
                                                                  force2.getValues(), force3.getValues(), force4.getValues()], float(beamWidth.get()))

        Label(result, text="\tResult", font=('Arial', 10, 'bold')).grid(
            row=0, column=1, columnspan=3)
        Label(result, text="\tVertical Reaction at support A is ").grid(
            row=1, column=2)
        Label(result, text=str(aVertical)+" N").grid(row=1, column=3)
        Label(result, text="\tHorizontal Reaction at support A is ").grid(
            row=2, column=2)
        Label(result, text=str(aHorizontal)+" N").grid(row=2, column=3)
        Label(result, text="\tVertical Reaction at support B is ").grid(
            row=3, column=2)
        Label(result, text=str(bVertical)+" N").grid(row=3, column=3)


def clear():
    global result
    result.grid_forget()


supportType = Frame(window)
supportType.grid(row=0, column=2, columnspan=5, pady=8)
Label(supportType, text="What type of support beam?", font=('bold')).grid(
    row=0, column=1, columnspan=3, pady=3)
Radiobutton(supportType, text='Simple Support',
            variable=v, value=1).grid(row=1, column=1)
Radiobutton(supportType, text='Cantilever', variable=v,
            value=2).grid(row=1, column=2)
Radiobutton(supportType, text='Hinged-Roller', variable=v,
            value=3).grid(row=1, column=3)
beamFrame = Frame(window)
beamFrame.grid(row=2, column=2, columnspan=5)
Label(beamFrame, text="Beam Width =").grid(
    row=0, column=0, padx=5)
beamWidth = Entry(beamFrame, justify=RIGHT)
beamWidth.grid(row=0, column=1, columnspan=2)
Label(beamFrame, text="m").grid(row=0, column=3)

force1 = guiForce(window, 3, 1)  # 4
force2 = guiForce(window, 8, 2)  # 8
force3 = guiForce(window, 13, 3)  # 12
force4 = guiForce(window, 18, 4)

calculationButton = Frame(window)
calculationButton.grid(row=3, column=2, columnspan=3,
                       rowspan=2, pady=10, sticky=N)
Button(calculationButton, text="Calculate", command=calculate).pack(
    side=LEFT, ipadx=10, padx=20)
Button(calculationButton, text="Clear", command=clear).pack(
    side=RIGHT, ipadx=10, padx=20)

window.mainloop()
