# Functions utils
# By VictorKlitzke(Sem copia safado)

from csv import writer
from pyautogui import *
from time import sleep as wait

def Novo():

  wait(3)
  print('Inicio')
  wait(3)
  print('Faturamento')
  x, y = locateCenterOnScreen('./imgs/faturamento.png')
  click(x, y)
  wait(3)
  print('Pré Venda')
  x, y = locateCenterOnScreen('./imgs/prevenda.png')
  click(x, y)
  wait(3)
  print('Novo')
  x, y = locateCenterOnScreen('./imgs/novo.png')
  click(1588, 238)
  press('clique')
  wait(3)
  write('CLIENTE CONSUMIDOR')
  wait(.7)
  press('enter')
  write('VENDEDOR PADRAO')
  wait(.7)
  press('enter')
  write('CLIENTE PADRAO')
  wait(.7)
  press('enter')
  write('A Vista')
  wait(.7)
  press('enter')
  wait(.7)
  press('enter')
  write('1122')
  wait(.7)
  press('enter')
  wait(.7)
  
 



  