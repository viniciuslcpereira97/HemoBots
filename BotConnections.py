from firebase import firebase

# Site url
url = "http://www.prosangue.sp.gov.br/hemocentros/"

# Firebase App connection
def getConnection():
    conn = firebase.FirebaseApplication("https://hemocentrosapp.firebaseio.com/")
    return conn

# Bloodbanks table
def getTable():
    return 'HemocentrosBR'

# Bloodbanks table data
def getHemocentersTable():
    return getConnection().get('HemocentrosBR' , None)

# Donation stages table
def getStagesTable():
    return "DonationStages"

# Decode state name
def decode(string):
    return string.replace('\\\xe1' , 'á').replace('\\\xed' , 'í').replace('\\\xe3o' , 'ã').replace('\\\xf4' , 'ô')

