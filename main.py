import wget
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


# cria um dataframe vazio com as colunas relacionadas com os dados coletados do site
planilha = pd.DataFrame(columns=['Nome', 'Preco', 'Imagem'])

# criar um objeto para manipular o navegador
navegador = webdriver.Firefox()

# abrir uma página no navegador

contador = 0
navegador.get("https://www.amazon.com.br/s?k=notebook&crid=2G9GE1TUWS1Q2&sprefix=n%2Caps%2C428&ref=nb_sb_ss_ts-doa-p_1_1")

while contador < 2:

    # procurar pelo elemento que possui o nome do produto
    elementNome = navegador.find_element(By.CSS_SELECTOR, '.a-size-mini .a-spacing-none .a-color-base .s-line-clamp-4')

    # procura pelo preco do produto
    elementPreco = navegador.find_element(By.CLASS_NAME, 'a-price-whole')

    # procurar pelo elemento que possui a imagem do pokemon
    elementImagem = navegador.find_elements(By.CLASS_NAME, 's-image')
    endercoImage = elementImagem.get_attribute('src')

    # cria um novo nome para a imagem
    nomeProduto = elementNome.split(' ')[0]
    extensaoImg = endercoImage.split('.')[-1]
    nomeImagem = nomeProduto + "." + extensaoImg
    ondeSalvar = "./img/" + nomeImagem

    wget.download(endercoImage, ondeSalvar)

    print("Nome:", elementNome.text)
    print("Preco:", elementPreco.text)
    print("Imagem:", nomeImagem.text)

    # adiciona os dados na planilha
    planilha.loc[contador] = [elementNome.text, elementPreco.text, nomeImagem]
    
    contador += 1

# salva a planilha em formato de excel
planilha.to_excel('pokemons.xlsx', index=False)

# mantem a página aberta
input()

