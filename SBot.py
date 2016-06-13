import BotConnections
from bs4 import BeautifulSoup
import urllib.request as request


def uploadStagesDict(stages_list):
    stages_dict = {'stages' : stages_list}

    conn = BotConnections.getConnection()
    result = conn.post(BotConnections.getStagesTable() , stages_dict)

    if(result != None):
        print("Inserted")
    else:
        print("Error")

def getStageTitle(title):
    return_title = title.split('">')[1].split("</")
    return_title = str(return_title[0]).strip()
    return return_title

def createStagesDict(title , description):
    return {
        'title' :   title,
        'description'   :   description
    }

def main():
    stages = []
    data = request.urlopen("http://www.prosangue.sp.gov.br/doacao/etapasdoacao.aspx").read()
    bsoup = BeautifulSoup(data , 'html.parser')
    itens_content_list = bsoup.find('ul' , {'class' : 'conteudoItens'})
    bsoup = BeautifulSoup(str(itens_content_list) , 'html.parser')
    itens = bsoup.findAll('li')

    for i , item in enumerate(itens):
        if not((i >= 7) and (i <= 10)):
            bsoup = BeautifulSoup(str(item) , 'html.parser')
            title = str(bsoup('div' , {'class' : 'title'}))
            description_bsoup = BeautifulSoup(str(bsoup('div' , {'class' : 'text'})) , 'html.parser')
            title = getStageTitle(title)
            description = description_bsoup.p.text.strip()
            stages.append(createStagesDict(title , description))

    uploadStagesDict(stages)

if __name__ == "__main__":
    main()