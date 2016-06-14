from unidecode import unidecode
import BotConnections
from bs4 import BeautifulSoup
import urllib.request as request

## python tutorial
## http://ozgur.github.io/python-firebase/

def main():
    bloodbanks = getBloodbanksDict()
    uploadBloodBank(bloodbanks)

def getBloodbanksDict():
    bloodbanks = {}
    site = str(request.urlopen(BotConnections.url).read())
    cidades = site.split('/><h3>&bull; ')
    cidades.pop(0)
    hemocentros = str(cidades).split('<input type="hidden"')
    for i , info in enumerate(hemocentros):
        if(i > 0):
            try:
                informacoes = info.split("</h3>") 
                estado = informacoes[0]
                estado = str(estado[2:]).split("', '")[1]
                bsoup = BeautifulSoup(str(informacoes[1]) , 'html.parser')                
                bloodbanks[estado] = (getAllStateBloodBanks(bsoup , estado))
            except Exception as e:
                print (e)
        else:
            try:
                informacoes = info.split("</h3>") 
                estado = str(informacoes[0][2:])
                bsoup = BeautifulSoup(str(informacoes[1]) , 'html.parser')                
                bloodbanks[estado] = getAllStateBloodBanks(bsoup , estado)
            except Exception as e:
                print (e)
    return bloodbanks

def createStateBloodBanksDict(bsoup):
    blood = {
        'Name'  :   bsoup.h4.text,
        'Address'   :   bsoup.findAll('p')[0].text,
        'District'  :   bsoup.findAll('p')[1].text,
        'City'  :   bsoup.findAll('p')[2].text,
        'Phone' :   bsoup.findAll('p')[3].text,
    }

    return blood

def getAllStateBloodBanks(bsoup , state):
    bloodStates = []
    for hemocentro in bsoup('li'):
        bloodStates.append(createStateBloodBanksDict(hemocentro))
    print("\n")

    return bloodStates

def printBloodBankInformations(bloodbank):
    nome = bloodbank.h4.text
    info = bloodbank.findAll('p')
    print("Nome hemocentro > " + nome)
    for i in info[:-1]:
        print("\t" + i.text)

def uploadBloodBank(bloodbanks_dict):
    conn = BotConnections.getConnection()
    result = conn.post(BotConnections.getTable() , bloodbanks_dict)

    if(result != None):
        print("Inserted")
    else:
        print("Error")

if __name__ == '__main__':
    main()