import wget
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import base64


# cria um dataframe vazio com as colunas relacionadas com os dados coletados do site
planilha = pd.DataFrame(columns=['Nome', 'Preco', 'Imagem'])

# criar um objeto para manipular o navegador
navegador = webdriver.Firefox()

# abrir uma página no navegador
navegador.get("https://lista.mercadolivre.com.br/cadeira-gamer#D[A:cadeira_gamer]")


wait = WebDriverWait(navegador, 20)

# procurar pelo elemento que possui o nome do produto
elementNome = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.poly-component__title > a')))
print(len(elementNome))

# procura pelo preco do produto
elementPreco = navegador.find_elements(By.CSS_SELECTOR, '.andes-money-amount > .andes-money-amount__fraction')

# procurar pelo elemento que possui a imagem do pokemon
elementImagem = navegador.find_elements(By.CLASS_NAME, 'poly-component__picture')

# loop para gerar os novos nomes nas imagens e armazenar os dados em ordem na planilha
contador = 0

for img in elementImagem:
    endercoImagem = img.get_attribute('src')
    contador = contador + 1

    # cria um novo nome para a imagem
    #extensaoImg = "webp"
    extensaoImg = endercoImagem.split('.')[-1]

    nomeProduto = "cadeira_produto_" + str(contador)
    nomeImagem = nomeProduto + "." + extensaoImg
    ondeSalvar = "./img/" + nomeImagem

    
    if "data" not in extensaoImg:

        wget.download(endercoImagem, ondeSalvar)

        print("Nome:", elementNome[contador].text)
        print("Preco:", elementPreco[contador].text)
        print("Imagem:", nomeImagem)

        # adiciona os dados na planilha
        planilha.loc[contador] = [elementNome[contador].text, elementPreco[contador].text + ',00', nomeImagem]
        
   

# salva a planilha em formato de excel
planilha.to_excel('pokemons.xlsx', index=False)
print("Terminei")

# mantem a página aberta
input()
