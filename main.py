import wget
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


# cria um dataframe vazio com as colunas relacionadas com os dados coletados do site
planilha = pd.DataFrame(columns=['Nome', 'Preco', 'Imagem'])

# criar um objeto para manipular o navegador
navegador = webdriver.Firefox()

# abrir uma página no navegador
navegador.get("https://www.amazon.com.br/s?k=notebook&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1AP5DD1ETMLKI&sprefix=notebook%2Caps%2C256&ref=nb_sb_noss_1")


# wait = WebDriverWait(navegador, 20)

# procurar pelo elemento que possui o nome do produto
elementNome = navegador.find_elements(By.CSS_SELECTOR, 'h2.a-size-mini > a > span.a-size-base-plus')
print(len(elementNome))

# procura pelo preco do produto
elementPreco = navegador.find_elements(By.CSS_SELECTOR, 'span.a-price > span > span.a-price-whole')

# procurar pelo elemento que possui a imagem do pokemon
elementImage = navegador.find_elements(By.CLASS_NAME, 's-image')
print(len(elementImage))


# loop para gerar os novos nomes nas imagens e armazenar os dados em ordem na planilha
contador = 0
while contador < 15:
    enderecoImage = elementImage[contador].get_attribute('src')

    # cria um novo nome para a imagem
    extensaoImg = enderecoImage.split('.')[-1]

    nomeProduto = "notebook_produto_" + str(contador)
    nomeImagem = nomeProduto + "." + extensaoImg
    ondeSalvar = ".\\img\\" + nomeImagem


    wget.download(enderecoImage, ondeSalvar)

    print("Nome:", elementNome[contador].text)
    print("Preco:", elementPreco[contador].text)
    print("Imagem:", nomeImagem)

    # adiciona os dados na planilha
    planilha.loc[contador] = [elementNome[contador].text, elementPreco[contador].text, nomeImagem]

    contador += 1
        
   

# salva a planilha em formato de excel
planilha.to_excel('produtos.xlsx', index=True)

# mantem a página aberta
input("ENTER para encerrar")


