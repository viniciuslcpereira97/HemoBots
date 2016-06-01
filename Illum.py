import time
import firebaseConnection
from urllib import request
from bs4 import BeautifulSoup

def main():
    
    conn = firebaseConnection.getConnection()
    result = conn.get(firebaseConnection.getHemocentersTable() , None)
    site_hemocenters = countSiteHemocenters()
    firebase_hemocenters = countFirebaseHemocenters(result)

    while True:
        print("Hemocentros Firebase: " + str(firebase_hemocenters))
        print("Hemocentros Site: " + str(site_hemocenters))
        if(site_hemocenters != firebase_hemocenters):
            print(str(site_hemocenters - firebase_hemocenters) + " hemocentro(s) novo(s)")
        else:
            print("Nenhum hemocentro novo")

        time.sleep((60 * 60) * 12)

def countFirebaseHemocenters(firebase_result):
    firebase_hemocenters = 0
    for state in firebase_result['-KJ1sgno9wwBzoTuz663']:
        for hemocenter in firebase_result['-KJ1sgno9wwBzoTuz663'][state]:
            firebase_hemocenters += 1
    return firebase_hemocenters

def countSiteHemocenters():
    data = request.urlopen("http://prosangue.sp.gov.br/hemocentros/Default.aspx").read()
    bsoup = BeautifulSoup(data , 'html.parser')
    state_list = bsoup('ul' , {'id' : 'estados'})
    bsoup = BeautifulSoup(str(state_list) , 'html.parser')
    all_hemocenters = bsoup('ul' , {'class' : 'nostyle'})
    return len(all_hemocenters)

if __name__ == '__main__':
    main()