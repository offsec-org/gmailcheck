from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import argparse
import os

if sys.version_info < (3, 7):
    sys.stdout.write("Sorry, dirsearch requires Python 3.7 or higher\n")
    sys.exit(1)


# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-e", "--emails", required=True,
   help="Lista de emails.")

ap.add_argument("-d", "--driver", required=True,
   help="Adicionar o './' no binario por exemplo:'./geckodriver'")

ap.add_argument("-o", "--output", required=True,
   help="Nome do arquivo para saida dos emails validos.")

args = vars(ap.parse_args())
path = ((args['emails']))
pathdriver = ((args['driver']))
output = ((args['output']))
replace = 0
emailvali = ''

def writeARQ(outPath,content):
    out = open(outPath, 'w')
    out.write(content)
    out.close()

if os.path.exists(output):
    very = 0
    while very != 1:
        sub = input("Arquivo existente!!! Dejesa substituir o arquivo??? [Y/n] ")
        
        if sub == "y" or sub == "Y":
            replace = 1
            very = 1
        elif sub == "n" or sub == "N":
            veryPath = 0
            while veryPath != 1:
                inputPath = input("Nome do novo arquivo: ")
                if inputPath != output:
                    replace = 0
                    veryPath=1
                    very = 1
else:
    replace = 3


arq = open(path, 'r')
for linha in arq:
    linha = linha.strip()
    profile = webdriver.FirefoxProfile()
    profile.set_preference("usergent:","Mozilla/5.0")

    driver = webdriver.Firefox(executable_path=pathdriver)
    driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    elem = driver.find_element_by_name("identifier")
    elem.clear()
    elem.send_keys(linha)
    elem.send_keys(Keys.RETURN)
    time.sleep(6)
    code = driver.page_source
    invalido = "Não foi possível encontrar sua Conta do Google"
    if invalido not in code:
        emailvali += linha+'\n'
        driver.close()
    else:
        driver.close()

if replace == 1:
    os.remove(output)
    writeARQ(output, emailvali)
elif replace == 0:
    writeARQ(inputPath, emailvali)
elif replace == 3:
    writeARQ(output, emailvali)
