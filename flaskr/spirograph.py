import math
import json

from flask import Blueprint
from flask import render_template

bp = Blueprint("spirograph", __name__, url_prefix="/spirograph")

@bp.route("/")
def spirograph():
    return render_template("spirograph/spirograph.html")

@bp.route("/getCoords/<int:holeRadius>/<int:smallRadius>")
def getSpirographCoords(holeRadius, smallRadius):
    return json.dumps(Spirograph(holeRadius, smallRadius).getSpirographCoords())

class Spirograph:

    def __init__(self, holeRadius, smallRadius, bigx=175, bigy=175, bigradius=150, numPoints=1000):
        self.holeRadius = holeRadius
        self.smallRadius = smallRadius
        self.bigx = bigx
        self.bigy = bigy
        self.bigradius = bigradius
        self.numPoints = numPoints

    def getSpirographCoords(self):
        spirographCoords = []

        for theyta in range(0, self.numPoints, 1):
            smallx = (self.bigradius - self.smallRadius) * math.cos(theyta / 57.2958) + self.bigx
            smally = (self.bigradius - self.smallRadius) * math.sin(theyta / 57.2958) + self.bigy
            ''' centerpoint of small circle revolves around centerpoint of big circle
            '''
            holex = int(self.holeRadius * math.cos((360 - theyta) / 57.2958 * (self.bigradius / self.smallRadius)) + smallx)
            holey = int(self.holeRadius * math.sin((360 - theyta) / 57.2958 * (self.bigradius / self.smallRadius)) + smally)

            spirographCoordGroup = []
            spirographCoordGroup.append(holex)
            spirographCoordGroup.append(holey)
            spirographCoords.append(spirographCoordGroup)

        return spirographCoords

# spirograph = Spirograph(102, 46)
# print(spirograph.getSpirographCoords())