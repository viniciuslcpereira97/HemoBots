import urllib
from unidecode import unidecode
import BeautifulSoup
import firebaseConnection

def main():
    site = str(urllib.urlopen('http://www.prosangue.sp.gov.br/hemocentros/').read())
    cidades = site.split('/><h3>&bull; ')
    cidades.pop(0)
    hemocentros = str(cidades).split('<input type="hidden"')

    for i , info in enumerate(hemocentros):
        if(i > 0):
            try:
                informacoes = info.split("</h3>")
                estado = informacoes[0].split("', '")[1]
                print estado
            except Exception as e:
                print e
        else:
            try:
                informacoes = info.split("</h3>")
                estado = informacoes[0][2:]
                print estado
            except Exception as e:
                print e

if __name__ == '__main__':
    main()