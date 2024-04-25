

import pyautogui
import time
import pandas


link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

pyautogui.PAUSE = 0.1;


pyautogui.press('win');
time.sleep(1)
pyautogui.write('chrome');
pyautogui.press('enter');
time.sleep(3)
pyautogui.write(link);
pyautogui.press('enter');

time.sleep(3);

pyautogui.click(x=835, y=411)
pyautogui.write('dyeggo0102@gmail.com');
pyautogui.press('tab')
pyautogui.write('dyeggo0102@gmail.com');
pyautogui.press('enter')

tabela =  str.read_csv("produtos.csv")

for linha in tabela.index:
    
    pyautogui.click(x=940, y=290)
    
    #cod
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo);
    pyautogui.press('tab')
    
    #marc
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca);
    pyautogui.press('tab')
    #tipro
    
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo);
    pyautogui.press('tab')
    
    #catepro
 
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press('tab')
    
    #pre
    
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]));
    pyautogui.press('tab')
    
    #cus
    
    pyautogui.write(str(tabela.loc[linha, "custo"]));
    pyautogui.press('tab')
    
    #obs
    obs = tabela.loc[linha, "obs"]
    if not str.isna(obs):
        pyautogui.write(obs);
        
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)



