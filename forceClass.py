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


class forcePoint():
    def __init__(self):
        self.mag = 0
        self.ang = 0
        self.distX = 0

    def magnitude(self, newMag):
        self.mag = newMag

    def angle(self, newAng, hflip=False):
        if hflip:
            self.ang = math.pi - math.radians(newAng)
        else:
            self.ang = math.radians(newAng)

    def distanceX(self, distance):
        self.distX = distance

    def horizontal(self):
        Fhor = self.mag*math.cos(self.ang)
        return round(Fhor, 5)

    def vertical(self):
        Fver = self.mag*math.sin(self.ang)
        return round(Fver, 5)

    def torque(self):
        tor = self.distX*self.vertical()
        return round(tor, 5)


class forceUDL():
    def __init__(self):
        self.mag = 0
        self.spread = 0
        self.distX = 0

    def magnitude(self, newMag, newSpread):
        self.mag = newMag*newSpread
        self.spread = newSpread

    def distanceX(self, distance):
        self.distX = distance

    def vertical(self):
        return round(self.mag, 5)

    def torque(self):
        tor = (self.distX+(self.spread/2))*self.vertical()
        return round(tor, 5)


class forceUVL():
    def __init__(self):
        self.mag = 0
        self.spread = 0
        self.distX = 0
        self.flip = False
        # |\
        # | \
        # |__\

    def magnitude(self, newMag, newSpread):
        self.mag = newMag*newSpread*0.5
        self.spread = newSpread

    def distanceX(self, distance):
        self.distX = distance

    def vertical(self):
        return round(self.mag, 5)

    def orientation(self, stat):
        self.flip = stat

    def torque(self):
        if not self.flip:
            tor = (self.distX+(self.spread/3))*self.vertical()
        else:
            tor = (self.distX+(self.spread*2/3))*self.vertical()
        return round(tor, 5)


def summationH(forces):
    sum = 0
    for force in forces:
        if not((isinstance(force, forceUDL)) or(isinstance(force, forceUVL))):
            sum += round(force.horizontal(), 5)
    return sum


def summationV(forces):
    sum = 0
    for force in forces:
        try:
            sum += round(force.vertical(), 5)
        except AttributeError:
            print("Force does not have vertical component")
    return sum


def summationT(torques):
    sum = 0
    for torque in torques:
        try:
            sum += round(torque.torque(), 5)
        except AttributeError:
            print("Force does not have Tourque component")
    return sum
