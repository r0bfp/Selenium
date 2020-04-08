# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os

# Classe porto seguro onde toda manipulação vai ocorrer
class Porto_Seguro:
    # Passando o objeto do driver para a classe
    def __init__(self, driver):
        self.driver = driver
        
    # metodo para navegar para as paginas
    def navigate_to_url(self, url):
        self.driver.get(url)

    # metodo para realizar login 
    def login(self, username, password):
        self.field_username_id = 'it-cpfCnpj' 
        self.field_password_id = 'it-senha' 
        self.btn_login_id = 'btnContinuar'


        self.driver.find_element_by_id(self.field_username_id).send_keys(username)
        self.driver.find_element_by_id(self.field_password_id).send_keys(password)
        self.driver.find_element_by_id(self.btn_login_id).click()

    # metodo para realizar o download do arquivo
    def download_file(self):
        self.btn_download_file_id = 'bodyContent_btcsv'
        
        self.driver.find_element_by_id(self.btn_download_file_id).click()





# Credenciais de acesso
username = input('Insira o usuario de acesso: ')
password = input('Insira a senha de acesso: ')
# Data de competencia formato MesAno
competence = input('Insira a data de competencia MM/AAAA: ')

# Configuração do perfil do browser
firefox_profile = webdriver.FirefoxProfile()

# Configuração do browser para realizar o download sem caixa de dialogo
firefox_profile.set_preference('browser.download.folderList', 2)
firefox_profile.set_preference('browser.download.manager.showWhenStarting', False)
# A linha a baixo é responsável por definir o caminho onde o download será realizado
firefox_profile.set_preference('browser.download.dir', os.getcwd())
firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')

# Configuraçoes importantes
# Localizando o binario do firefox
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
# Abrindo o browser passando como argumento o binario do firefox e o executavel do driver
browser = webdriver.Firefox(firefox_binary=binary, executable_path='C:\\geckodriver.exe', firefox_profile=firefox_profile)

# Instanciando objeto da classe porto seguro
porto_seguro = Porto_Seguro(browser)


# Variaveis de configuração
login_page_url = 'https://cliente.portoseguro.com.br/portaldecliente/LoginPorto'
# pagina caminho para o resto do processo
download_page = 'https://wwws.portoseguro.com.br/ResumoFaturamentoCol/Pages/ResumoFatura.aspx?estipulante%253d58757809%2526tipoproduto%253d1%2526portal%253d7%2526uid%253drh%252540foursys.com.br&comp=032020&corr=132904&ncor=ARBOS%20CORRETORA%20DE%20SEGUROS%20LTDA&est=165652&nest=0058757809%20-%20FOURSYS%20PROJETOS%20E%20SISTEMAS%20EM%20INFORMATICA%20LT&sub=217749&uni=273214&nsub=0001737291%20-%20FOURSYS%20PROJETOS%20E%20SISTEMAS%20EM%20INFORMATICA%20LT&nuni=0000000001%20-%20MATRIZ%20CNPJ%2003.808.125/0001-30'
# caminho da tab exportação de arquivos
download_tab = 'https://wwws.portoseguro.com.br/ResumoFaturamentoCol/Pages/RelacaoArquivo.aspx?estipulante=58757809&tipoproduto=1&portal=7&uid=rh@foursys.com.br&comp=' + competence + '&corr=132904&ncor=ARBOS%20CORRETORA%20DE%20SEGUROS%20LTDA&est=165652&nest=0058757809%20-%20FOURSYS%20PROJETOS%20E%20SISTEMAS%20EM%20INFORMATICA%20LT&sub=217749&uni=273214&nsub=0001737291%20-%20FOURSYS%20PROJETOS%20E%20SISTEMAS%20EM%20INFORMATICA%20LT&nuni=0000000001%20-%20MATRIZ%20CNPJ%2003.808.125/0001-30' 


# Navegando até a pagina de login
porto_seguro.navigate_to_url(login_page_url)
# Realizando o login
porto_seguro.login(username, password)
# Navegando até a pagina de download
porto_seguro.navigate_to_url(download_page)
porto_seguro.navigate_to_url(download_tab)
# Relizar o download do arquivo
porto_seguro.download_file()    



