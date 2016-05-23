import urllib.request as request
from bs4 import BeautifulSoup

def main():

    estados = {}
    cidades = {}
    # site = request.urlopen('http://www.prosangue.sp.gov.br/hemocentros/').read()
    # file = open('hemocentros.html' , 'w')
    # file.truncate()
    # file.write(str(site))
    site = open("hemocentros.html")
    cidades = site.split('/><h3>&bull; ')
    cidades.pop(0)
    for cidade in cidades:
        listaCidades = cidade.split('<li>')[1][:-11]
        hemocentros = cidade.split('</h3>')[1]
        hemocentros_soup = BeautifulSoup(hemocentros , 'html.parser')

        hemocentros = hemocentros_soup('ul' , {'class' : 'nostyle'})
        

        estados = str(cidade.replace('</h3>' , ', <!h3!>').split('<!h3!>')[0])
        estados = estados.split(',')

        for estado in estados:
            if(estado != ' '):
                estados = estado;
        
        for hemocentro in hemocentros:
            soup = BeautifulSoup(str(hemocentros) , 'html.parser')
            informacoes = soup.findAll('p')
            print(soup.h4.text)
            print(informacoes[0].text) #Endereço
            print(informacoes[1].text) #Bairro
            print(informacoes[2].text) #Cidade
            print(informacoes[3].text) #telefone
            print('----------------------------------')

if __name__ == '__main__':
    main()