
from website import db

#One-to-Many relationship: 1 package to many Jobs
# Can multiple packages have the same job? Assuming no.

class Package(db.Model) :
    __tablename__="Package"
    id = db.Column(db.Integer, primary_key=True) #comes from castle
    tagID = db.Column(db.String(64)) #Make this a list (Potential solution, add a table for Tag and a db.relationship)
    packageApprover = db.Column(db.String(64)) #drop-down
    packageType = db.Column(db.String(64)) #drop-down
    packageStatus = db.Column(db.String(64))  #drop-down
    packageName = db.Column(db.String(256)) #how is this determined?
    #packageDescription = db.Column(db.String(256)), these appears to be a group of fields, (problem, solution, subject*)
    packageProblem = db.Column(db.String(256))
    packageSolution = db.Column(db.String(256))
    packageReferences = db.Column(db.String(256))
    #analysis = db.Column(db.String(256))
    #packageHistory = db.Column(db.String(256))    , Appear to be collected under "Package Notes", (Package Note*, Package History, Package Rev Note)
    packageRevNote = db.Column(db.String(256))
    planeModel = db.Column(db.Integer) #named planeModel so there is not confusion with Model
    #references = db.Column(db.)
    archiveDate = db.Column(db.String(32)) # potentially use data type DateTime --> archiveDate = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    #One-to-Many relationship: 1 package to many Jobs
    # Can multiple packages have the same job? Assuming no.
    jobs = db.relationship('Job')
    
    
    
    
class Job(db.Model) :
    __tablename__="Job"
    #we have no current datafiled from castle to assign to id. For now, this will be randomly generated.
    id = db.Column(db.Integer, primary_key=True) #It would be cool to have this based off of the associated Package id
    package_id = db.Column(db.Integer, db.ForeignKey('Package.id'))
    assignee = db.Column(db.String(32))
    jobApprover = db.Column(db.String(32))
    castleInDate = db.Column(db.String(32)) # potentially use data type DateTime --> castleInDate = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    responseDate = db.Column(db.String(32)) # potentially use data type DateTime --> responseDate = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    jobStatus = db.Column(db.String(32)) #Is this a boolean?
    
    #collected under "Job Description"
    subject = db.Column(db.String(256))
    specificQuestion = db.Column(db.String(256))
    
    dispositionText = db.Column(db.String(256))
    
    #collected under "Job Notes"
    dispositionSummary = db.Column(db.String(256))
    jobNote = db.Column(db.String(256))
    #jobRevNote = db.Column(db.String(256))
    
    



