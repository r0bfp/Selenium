# Selenium Bot
Bot para realizar o download dos arquivos .csv no site da Porto Seguro.
### Dependências importantes para o funcionamento
#### Para Windows: 
Após a clonagem do repositório, será necessário baixar o driver do Firefox no link https://github.com/mozilla/geckodriver/releases. 
Efetuado o download, arraste o arquivo **geckodriver.exe** para a raiz da unidade **C:** e crie um novo caminho de variável de 
ambiente acessando **Painel de Controle > Sistema e Segurança > Sistema > Configurações avançadas do sistema > Variáveis de Ambiente**. Dentro da 
janela que foi exibida será possível encontrar dentro da região **Variáveis do sistema** a variável **Path**. Após selecioná-la  
clique em **Editar...**, na janela que apareceu clique em **Novo** e insira o valor **C:\geckodriver.exe**. Após todo o procedimento 
realizado, basta executar o arquivo .py que irá funcionar normalmente.
