# NOTE: When we start creating new pages, we should look into "BLOCK CONTENT" from flask for each html page, right now we are not doing that
from website import create_app, db
from website.Model.models import Package, Job
import psycopg2

app = create_app()

#generating database
@app.before_first_request
def initDB(*args, **kwargs):
    db.create_all()
    if Package.query.count() == 0: #adding sample data
        packages = [{'id':1,'tagID': 'N0000000001', 'packageApprover':'other', 'packageType':'Factory Support', 'packageStatus':'unassigned','packageName':'Package 1', 'packageProblem':'problem','packageSolution':'solution','packageReferences':'References','packageRevNote':'RevNote', 'planeModel':'777-x','archiveDate':'Nov 13, 2003'},
                    {'id':2,'tagID': 'N0000000002', 'packageApprover':'other', 'packageType':'Supplier Support','packageStatus':'assigned',  'packageName':'Package 2', 'packageProblem':'problem','packageSolution':'solution','packageReferences':'References','packageRevNote':'RevNote', 'planeModel':'777-x','archiveDate':'April 4, 2002'},
                    {'id':3,'tagID': 'N0000000003', 'packageApprover':'other', 'packageType':'Other',            'packageStatus':'accepted', 'packageName':'Package 3', 'packageProblem':'problem','packageSolution':'solution','packageReferences':'References','packageRevNote':'RevNote', 'planeModel':'777-x','archiveDate':'Apr 11, 2008'},
                    {'id':4,'tagID': 'N0000000004', 'packageApprover':'other', 'packageType':'Factory Support',  'packageStatus':'in work',  'packageName':'Package 4', 'packageProblem':'problem','packageSolution':'solution','packageReferences':'References','packageRevNote':'RevNote', 'planeModel':'777-x','archiveDate':'Mar 19, 2004'},
                    {'id':5,'tagID': 'N0000000005', 'packageApprover':'other', 'packageType':'Supplier Support', 'packageStatus':'rejected', 'packageName':'Package 5', 'packageProblem':'problem','packageSolution':'solution','packageReferences':'References','packageRevNote':'RevNote', 'planeModel':'777-x','archiveDate':'Jun 13, 2006'},
                    {'id':6,'tagID': 'N0000000006', 'packageApprover':'other', 'packageType':'Factory Support',  'packageStatus':'assigned', 'packageName':'Package 6', 'packageProblem':'problem','packageSolution':'solution','packageReferences':'References','packageRevNote':'RevNote', 'planeModel':'777-x','archiveDate':'Apr 12, 2003'},
                   ] #Jobs is empty, not sure how to do that one.
        jobs = [{'id':1,'package_id':1,'assignee':'assignee','jobApprover':'Job Approver','castleInDate':'Nov 25, 2003','responseDate':'Dec 15, 2003','jobStatus':'Status','subject':'Subject','specificQuestion':'Question','dispositionText':'Disposition','dispositionSummary':'Disposition','jobNote':'Job Note'},
                {'id':2,'package_id':1,'assignee':'assignee','jobApprover':'Job Approver','castleInDate':'Jan 2, 2004','responseDate':'Jan 15, 2004','jobStatus':'Status','subject':'Subject','specificQuestion':'Question','dispositionText':'Disposition','dispositionSummary':'Disposition','jobNote':'Job Note'},
                {'id':3,'package_id':2,'assignee':'assignee','jobApprover':'Job Approver','castleInDate':'Apr 25, 2002','responseDate':'May 15, 2002','jobStatus':'Status','subject':'Subject','specificQuestion':'Question','dispositionText':'Disposition','dispositionSummary':'Disposition','jobNote':'Job Note'},
                {'id':4,'package_id':4,'assignee':'assignee','jobApprover':'Job Approver','castleInDate':'Mar 25, 2004','responseDate':'Apr 15, 2004','jobStatus':'Status','subject':'Subject','specificQuestion':'Question','dispositionText':'Disposition','dispositionSummary':'Disposition','jobNote':'Job Note'},
                {'id':5,'package_id':4,'assignee':'assignee','jobApprover':'Job Approver','castleInDate':'May 25, 2004','responseDate':'Jun 15, 2004','jobStatus':'Status','subject':'Subject','specificQuestion':'Question','dispositionText':'Disposition','dispositionSummary':'Disposition','jobNote':'Job Note'},
                {'id':6,'package_id':6,'assignee':'assignee','jobApprover':'Job Approver','castleInDate':'Apr 25, 2003','responseDate':'May 15, 2003','jobStatus':'Status','subject':'Subject','specificQuestion':'Question','dispositionText':'Disposition','dispositionSummary':'Disposition','jobNote':'Job Note'},
                {'id':7,'package_id':5,'assignee':'assignee','jobApprover':'Job Approver','castleInDate':'Jun 25, 2006','responseDate':'Jul 15, 2006','jobStatus':'Status','subject':'Subject','specificQuestion':'Question','dispositionText':'Disposition','dispositionSummary':'Disposition','jobNote':'Job Note'},
                ]
                
        for j in jobs:
            db.session.add(Job(id=j['id'],package_id=j['package_id'],assignee=j['assignee'],jobApprover=j['jobApprover'],castleInDate=j['castleInDate'],responseDate=j['responseDate'],jobStatus=j['jobStatus'],subject=j['subject'],specificQuestion=j['specificQuestion'],dispositionText=j['dispositionText'],dispositionSummary=j['dispositionSummary'],jobNote=j['jobNote']))
        db.session.commit()
        
        for p in packages:
            list_jobs = []
            for job in jobs:
                if job['package_id'] == p['id']:
                    list_jobs.append(job)
            #db.session.add(Package(jobs=list_jobs, id=p['id'],tagID=p['tagID'],packageApprover=p['packageApprover'],packageType=p['packageType'],packageStatus=p['packageStatus'],packageName=p['packageName'],packageProblem=p['packageProblem'],packageSolution=p['packageSolution'],packageReferences=p['packageReferences'],packageRevNote=p['packageRevNote'],planeModel=p['planeModel'],archiveDate=p['archiveDate']))
        db.session.commit()     
       
        


if __name__ == '__main__':
    app.run(debug=True) # auto reruns server
    