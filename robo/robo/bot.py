"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *
from selenium import webdriver
from PIL import Image

import pytesseract
import cv2
import os
import glob


class Bot(DesktopBot):
    def action(self, execution=None):
        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.
        navegador = webdriver.Chrome()
        #navegador.get("http://192.168.1.177")
        self.browse("http://192.168.1.177")

        # Open file with r
        #self.execute(r'C:\Users\jimini.costa\Pictures\Camera Roll')
        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,/
        #     message="Task Finished OK."s
        # )
        # def tratar_imagens(pasta_origem, pasta_destino='resources'):
        #     arquivos = glob.glob(f"{pasta_origem}/*")
        #     for arquivo in arquivos:
        #         imagem = cv2.imread(arquivo)
        imagem = cv2.imread(
            # C:\Users\jimini.costa\PycharmProjects\robobot\robo\robo\resources
            r"C://Users/jimini.costa/PycharmProjects/robobot/robo/robo/resources/TextoImagem.png")
        caminho = r"C:\Program Files\Tesseract-OCR"
        pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
        texto = pytesseract.image_to_string(imagem, lang="por")  #
        print(texto)

        # if not self.find( "iconeguilherme", matching=0.97, waiting_time=100):
        #     self.not_found("iconeguilherme")
        # self.click()
        #
        # if not self.find( "GuilhermeJogador", matching=0.97, waiting_time=10000):
        #     self.not_found("GuilhermeJogador")
        #
        # if not self.find( "Jogar", matching=0.97, waiting_time=10000):


        
        if not self.find( "AceBonus", matching=0.97, waiting_time=10000):
            self.not_found("AceBonus")
        self.click()
        
        
        if not self.find( "21", matching=0.97, waiting_time=10000):
            self.not_found("21")
        self.click()
        for i in range(20):

            if not self.find( "1", matching=0.97, waiting_time=10000):
                self.not_found("1")
            self.click()

        for i in range(20):

            if not  self.find( "PlayButton", matching=0.97, waiting_time=10000):
                self.not_found("PlayButton")
                #for x in range(2000):
                if not self.find( "Buy", matching=0.97, waiting_time=10000):
                    self.not_found("Buy")
                self.click_relative(68, 38)
            self.click()

            if not self.find( "BE1", matching=0.97, waiting_time=10000):
                self.not_found("BE1")
            self.click()

        if not self.find( "Exit", matching=0.97, waiting_time=10000):
            self.not_found("Exit")
        self.click()
        self.click()

        def not_found(self, label):
            print(f"Element not found: {label}")

        # Match CASE Para criação de Cenarios e definições e resultados especificos
    # def contas(centros): # Def definição , Contas Variavel, Centros Lista de Dados
    #     match centros:
    #     case [area, centros]: # apenas 1 centro de custo
    #     print("Area {} possui o centro de custo {}".format(area,centros))

#     def contas(centros):
#         match centros:
#             case [area, centros]: # Apenas 1 centro de custo
#             print("A área {} possui o centro de custo {}".format(area,centros))
#
#         case [area, *centros]: #2 ou mais centros
#             print( ' A área {} possui os centros de custo abaixo:'.format(area))
#             for centro in centros:
#                 print (centro)
#
#
# contas(['Financeiro', 'ABC'])
# contas(['Marketing', 'ABC','XYZ','HJG'])


if __name__ == '__main__':
    Bot.main()











