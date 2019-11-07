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

import math
from forceClass import summationH, summationT, summationV
from forceClass import forcePoint, forceUDL, forceUVL


def simpleSupported(forces, beamWidth):
    reacA = 0
    reacB = 0
    balanced = True
    print(beamWidth)
    if (summationH(forces) == 0):
        reacB = summationT(forces)/beamWidth
        reacA = summationV(forces)-reacB
        balanced = True
    else:
        print("WARNING - Not a balanced beam!!")
        print("Excess Force is", summationH(forces))
        balanced = False
    return round(reacA, 5), round(reacB, 5), balanced, round(summationH(forces), 5)


def cantilever(forces):
    reacV = summationV(forces)
    reacH = summationH(forces)
    reacT = summationT(forces)
    return round(reacV, 5), round(reacH, 5), round(reacT, 5)


def oneHingedOtherRoller(forces, beamWidth):
    reacVA = 0
    reacHA = 0
    reacVB = 0
    print(beamWidth)
    reacVB = summationT(forces)/beamWidth
    reacVA = summationV(forces)-reacVB
    reacHA = summationH(forces)
    return round(reacVA, 5), round(reacHA, 5), round(reacVB, 5)


# F1 = forcePoint()
# F1.magnitude(10000)
# F1.angle(math.radians(90))
# F1.distanceX(4)
# print("F1", F1.vertical())
# print("F1", F1.torque())

# F2 = forcePoint()
# F2.magnitude(15000)
# F2.angle(math.radians(30))
# F2.distanceX(6)

# F3 = forcePoint()
# F3.magnitude(20000)
# F3.angle(math.radians(45))
# F3.distanceX(10)

# F4 = forcePoint()
# F4.magnitude(27132.51668)
# F4.angle(math.radians(180))
# F4.distanceX(0)


# F5 = forcePoint()
# F5.magnitude(15000)
# F5.angle(math.radians(90))
# F5.distanceX(3)

# F7 = forcePoint()
# F7.magnitude(20000)
# F7.angle(math.radians(60))
# F7.distanceX(2)

# F6 = forceUDL()
# F6.magnitude(10000, 2)
# F6.distanceX(0)

# F8 = forcePoint()
# F8.magnitude(20)
# F8.angle(math.radians(90))
# F8.distanceX(7)

# F9 = forcePoint()
# F9.magnitude(60)
# F9.angle(math.radians(45), True)
# F9.distanceX(2)

# F10 = forceUDL()
# F10.magnitude(30, 4)
# F10.distanceX(3)

# F3 = forceUVL()
# F3.magnitude(100, 3)
# F3.distanceX(50)
# F3.orientation(True)
# print("F3", F3.vertical())
# print("F3", F3.torque())

# print("Summation Vertical", summationV([F8, F9,  F10]))
# print("Summation Horizontal", summationH([F8, F9, F10]))
# print("Summation Torque", summationT([F8, F9, F10]))
# print("Simple Supported", simpleSupported([F1, F2, F3, F4], 12))
# print("Cantilever", cantilever([F5, F6, F7]))
# print("One end hinged other on roller",
#       oneHingedOtherRoller([F8, F9, F10], 9))
