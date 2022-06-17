# Functions utils
# By VictorKlitzke(Sem copia safado)

from csv import writer
from pyautogui import *
from time import sleep as wait

def Novo():

  print('Inicio')
  x, y = locateCenterOnScreen('./imgs/faturamento.png')
  click(x, y)
  wait(3)
  print('Prevenda')
  x, y = locateCenterOnScreen('./imgs/prevenda.png')
  click(x, y)
  wait(3)
  print('New')
  x, y = locateCenterOnScreen('./imgs/new.png')
  click(x, y)
  