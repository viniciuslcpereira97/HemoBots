import time
import Bbot
import BotConnections
from urllib import request
from bs4 import BeautifulSoup

def main():
    result = BotConnections.getHemocentersTable()
    site_hemocenters = countSiteHemocenters()
    firebase_hemocenters = countFirebaseHemocenters(result)

    while True:
        print("Hemocentros Firebase: " + str(firebase_hemocenters))
        print("Hemocentros Site: " + str(site_hemocenters))
        if(site_hemocenters != firebase_hemocenters):
            print(str(site_hemocenters - firebase_hemocenters) + " hemocentro(s) novo(s)")
            print(newHemocentersList())
        else:
            print("Nenhum hemocentro novo")
        time.sleep((60 * 60) * 12)

def countFirebaseHemocenters(firebase_result):
    firebase_hemocenters = 0
    for state in firebase_result['-KKEAkcj-mdSibaQTol0']:
        for hemocenter in firebase_result['-KKEAkcj-mdSibaQTol0'][state]:
            firebase_hemocenters += 1
    return firebase_hemocenters

def countSiteHemocenters():
    data = request.urlopen("http://prosangue.sp.gov.br/hemocentros/Default.aspx").read()
    bsoup = BeautifulSoup(data , 'html.parser')
    state_list = bsoup('ul' , {'id' : 'estados'})
    bsoup = BeautifulSoup(str(state_list) , 'html.parser')
    all_hemocenters = bsoup('ul' , {'class' : 'nostyle'})
    return len(all_hemocenters) - 1

def newHemocentersList():
    site_list = siteList()
    firebase_list = firebaseList()
    firebase_list_size = len(firebase_list)
    new_hemocenter_list = []
    for site_hemocenter in site_list:
        for i, firebase_hemocenter in enumerate(firebase_list):
            if(site_hemocenter != firebase_hemocenter):
                if(i == firebase_list_size - 1):
                    new_hemocenter_list.append(firebase_hemocenter)
            else:
                break
        break
    return new_hemocenter_list

def siteList():
    siteList = []
    bdictionary = Bbot.getBloodbanksDict()
    for estate in bdictionary:
        for bloodbank in bdictionary[estate]:
            siteList.append(bloodbank['Name'])
    return siteList

def firebaseList():
    firebase_list = []
    firebase_states = BotConnections.getHemocentersTable()['-KKEAkcj-mdSibaQTol0']
    for state in firebase_states:
        for hemocenter in firebase_states[state]:
            firebase_list.append(hemocenter['Name'])
    return firebase_list

if __name__ == '__main__':
    main()