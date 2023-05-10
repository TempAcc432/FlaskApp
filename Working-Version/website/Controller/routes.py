# https://www.geeksforgeeks.org/executing-sql-query-with-psycopg2-in-python/
import psycopg2
from flask import Blueprint, render_template, request

routes = Blueprint('routes', __name__)

# NOTE: If this is switched to an ORM, we do not need a direct connection to the PostgreSQL DB
conn = psycopg2.connect("dbname=boeing user=postgres password=password")
cursor = conn.cursor()

# ** Important **
# I was given a file from our Boeing mentors that had the 777-9 charted on a map in excel
# I exported that graph as an SVG and I'm displaying that in map.html
# My original plan was to sync the coordinates between the excel graph and the map on our page
# For example, in the excel map the nose is centered at X: 200, so I wanted to have that match here
# Due to time constraints, this has been very challenging (due to my inexperience with SVG viewboxes)
# So for now, the center is hardcoded at 279 (based off of eyeballing the view..)
# Resolution scaling of monitors may offset this as well

# WHAT I WOULD CHANGE
# Sync the coordinate system between the excel graph and the website map, ensure the coordinates are not affected by resolution scaling, etc.
# Use the excel graph data (which has all points mapped of each location on the plane) to map the SVG file in our website
# This could allow a developer to create a system where if they hover over a certain coordinate point (based off of the SVG vectors) it could display which part of the plane that section is
class Vector:
    # Coordinates
    x : float
    y : float
    z : float

    # we need offsets because our coordinate origins are different than boeings
    xOffset : float
    yOffset : float
    zOffset : float # don't need this for 2D

    def __init__(self): # at the moment our coord scale is hardcoded at X: 2000 Y: 700
        self.yOffset = 279 # 0 is the center of the airplane

    def offset_vector(self):
        # Max X: 3500 Max Y: 800
        # I believe the calculation is: newCoordX = (OldCoordX / (MaxBoeingCoord / MaxOurCoord))
        self.x = (self.x / (3500/1500))
        self.y = (self.y / (800/1000)) + self.yOffset
#****

# UNTIL WE USE AN ORM THIS IS OUR MODEL
class Defect:
    pkgID: str
    coord : Vector
    type : str
    desc : str
    disp : str
    castleLink: str
    cmesLink: str

    def __init__(self, vector, defect): 
        self.coord = vector
        self.pkgID = defect[0]
        self.type = defect[1]
        self.desc = defect[2]
        self.disp = defect[3]
        self.coord.x = defect[4]
        self.coord.y = defect[5]
        self.coord.z = defect[6]
        self.coord.offset_vector()

        # Generate links
        self.castleLink = "https://castle-cfprod.web.boeing.com/app-external-interface-package/" + str(self.pkgID) + "-0001/" + str(self.pkgID)
# ****

# All routes
@routes.route('/', methods=['GET','POST']) # decorator
def home():
    cursor.execute('SELECT detail_pn FROM part') # populate the part section # UPDATE QUERY HERE
    instance = cursor.fetchall()
    defects = []
    filterList = []
    cursor.execute("SELECT * FROM defect") # UPDATE QUERY HERE

    # Request Handling
    if request.method == "POST":
        if 'Package ID' in request.form:
            pkgID = request.form['Package ID']
            filterList.append("Package ID: " + pkgID)
            cursor.execute("SELECT * FROM defect WHERE package_id = %s", [pkgID, ]) # UPDATE QUERY HERE
        if 'Tag ID' in request.form:
            pkgAprvr = request.form['Tag ID']
            filterList.append("Tag ID: " + pkgAprvr)
        if 'Package Type' in request.form:
            pkgType = request.form['Package Type']
            filterList.append("'Package Type: " + pkgType)
            cursor.execute("SELECT * FROM defect WHERE defect_type = %s", [pkgType, ]) # UPDATE QUERY HERE
        if 'Package Status' in request.form:
            pkgStatus = request.form['Package Status']
            filterList.append("Package Status: " + pkgStatus)
        if 'Archive Date' in request.form:
            archvDate = request.form['Archive Date']
            filterList.append("Archive Date: " + archvDate)

        # User clicks on "View On Map"
        if 'map-id' in request.form:
            pkgID = request.form['map-id']
            cursor.execute("SELECT * FROM defect WHERE package_id = %s", [pkgID, ]) # fetches the defect related to what the user clicked on # UPDATE QUERY HERE
            for defect in cursor.fetchall():
                newDef = Defect(Vector(), defect)
                defects.append(newDef)
            return render_template("map.html", defects=defects)
        
    for defect in cursor.fetchall():
        newDef = Defect(Vector(), defect)
        defects.append(newDef)

    return render_template("index.html", instance=instance, defects=defects, filterList=filterList)

@routes.route('/job', methods=['GET','POST'])
def job():
    # ****This code will change to match the job properties in our DB once those are added****
    cursor.execute('SELECT detail_pn FROM part') # populate the part section
    instance = cursor.fetchall()
    defects = []
    newDefects = []
    outText = ''
    vectorList = []
    filterList =[]
    cursor.execute("SELECT * FROM defect")

    for defect in cursor.fetchall():
        newDef = Defect(Vector(), defect)
        defects.append(newDef)

    # Request Handling
    if request.method == "POST":
        if 'filter-checkbox' in request.form:
            filterList = request.form.getlist('filter-checkbox')
            text = request.form.getlist('filter-text') # text boxes from the checkboxes
    return render_template("job.html", instance=instance, defects=defects, filterList=filterList, outText=outText, vectorList=vectorList)

@routes.route('/map', methods=['GET','POST'])
def map():
    defects = []
    cursor.execute("SELECT * FROM defect")
    for defect in cursor.fetchall():
        newDef = Defect(Vector(), defect)
        defects.append(newDef)
    return render_template("map.html", defects=defects)
# ****

