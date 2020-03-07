from bs4 import BeautifulSoup as BS
import requests

def get_codes(url='http://orcz.com/Borderlands_Pre-Sequel:_Shift_Codes', cell=4, cellLenght=7, tableIndex=0, codeLenght=29):
    '''
    Returns a list of all codes found on the website. Contains the codes of the specified platform and the respective game.
    '''
    source = requests.get(url).text
    soup = BS(source, 'lxml')
    tables = soup.findAll('table')
    table = tables[tableIndex]

    redCodes = [] # invalid codes
    codeList = []
    clCheck = True

    if (codeLenght == 0):
        clCheck = False

    for row in table.findAll("tr"):
        cells = row.findAll("td")

        if len(cells) == cellLenght:

            isValid = True

            if (clCheck and len(cells[cell].text.rstrip()) != codeLenght):
                isValid = False

            if (cells[cell].find(style="color:red") != None):
                redCodes.append(cells[cell].find(style="color:red").text.rstrip())

            if cells[cell].text.rstrip() not in redCodes and isValid:
                codeList.append(cells[cell].text.strip())

    return codeList
