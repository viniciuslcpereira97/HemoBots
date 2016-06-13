from firebase import firebase

url = "http://www.prosangue.sp.gov.br/hemocentros/"

def getConnection():
    conn = firebase.FirebaseApplication("https://hemocentrosapp.firebaseio.com/")
    return conn

def getTable():
    return 'HemocentrosBR'

def getHemocentersTable():
    return getConnection().get('HemocentrosBR' , None)

def getStagesTable():
    return "DonationStages"

def decode(string):
    return string.replace('\\\xe1' , 'á').replace('\\\xed' , 'í').replace('\\\xe3o' , 'ã').replace('\\\xf4' , 'ô')

