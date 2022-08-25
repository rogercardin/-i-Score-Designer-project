from lib2to3.pgen2 import driver
from selenium.webdriver.support import ui
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from Bio import SeqIO
from Bio.Seq import Seq
import time
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

driver.get('https://www.med.nagoya-u.ac.jp/neurogenetics/i_Score/i_score.html')

start_time = time.time()

#Criando a tabela
tabela = []


def analisar(seq):
   
    ui.WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Input"]')))
    driver.find_element("xpath", '//*[@id="Input"]').click()
    driver.find_element("xpath", '//*[@id="Input"]').clear()
    driver.find_element("xpath", '//*[@id="Input"]').send_keys(seq)
    driver.find_element("xpath", '//*[@id="Analyze"]').click()
    ui.WebDriverWait(driver, 120).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[8]/table/tbody')))
    head = driver.find_element("xpath",('/html/body/div[8]/table/tbody'))
    head_line = head.find_elements("xpath",'tr')
    for linhas in head_line:
        tabela.append(linhas.text)
    return tabela
def fasta_gene(nome_arquivo):
    with open(nome_arquivo,'r') as alvo:
        for gene in SeqIO.parse(alvo, "fasta"):
            saida = open(gene.id,'w')
            tabela = analisar(gene.seq)
            for linha in tabela:
                saida.write("{}\n".format(linha))
            saida.close()
            tabela[:] = []
            print(time.time() - start_time)
fasta_gene('seqAlldsRNA_offtarget_GM.fasta')
