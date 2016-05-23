import urllib.request as request
from bs4 import BeautifulSoup

def main():

    estados = {}
    cidades = {}
    file =  open("hemocentros.html").read()
    cidades = file.split('/><h3>&bull; ')
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
            # print(soup.h4.text)
            # print(informacoes[0].text) #Endereço
            # print(informacoes[1].text) #Bairro
            # print(informacoes[2].text) #Cidade
            # print(informacoes[3].text) #telefone
            # print('----------------------------------')

        # print('#################################################################################')
    # states_soup = BeautifulSoup(file , 'html.parser')
    # estados = states_soup.select('ul#estados > li')
    
    
    # print (cidades['AC'])

# def getCitiesList(state_list):
    # cities_soup = BeautifulSoup(state_list , 'html.parser')
    # cities_list = cities_soup('h3')
    # for i in range(len(cities_list)):
        # print(cities_list[i].string)

# def getBloodBanks(state_list):
    # bloodbanks_soup = BeautifulSoup(state_list , 'html.parser')
    # blood_banks = bloodbanks_soup('ul' , {'class' : 'nostyle'})
    # for i in range(len(blood_banks)):
        # print(blood_banks[i].h4)


if __name__ == '__main__':
    main()


def backup():
    # site = request.urlopen('http://www.prosangue.sp.gov.br/hemocentros/')
    # data = site.read()
    states_soup = BeautifulSoup(file , 'html.parser')
    estados = states_soup.select('ul#estados > li')
    # state_list = states_soup('ul' , {'id' : 'estados'})
    # estados = BeautifulSoup(str(state_list) , 'html.parser')
    # print(estados('li')[1])
    for estado in estados:
        id = str(estado).split('"')[1]
        cidades[id] = []
        teste = states_soup.select('#estados ul')
        cidades[id].append(teste)
        # break
    print (cidades['SP']) 
