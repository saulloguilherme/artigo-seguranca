from requests import Response

from keys import OPEN_PAGE_RANK_API_KEY
from bs4 import BeautifulSoup
import requests

#
# Receber Parâmetros da URL
#

def get_attr_list(url: str) -> list:
    response = get_response(url)

    atributos = [tamanho_url(url), use_https(url), has_ip_format(url), points_number(url), has_arroba(url),
                 active_days(url), pagerank_pontos(url), has_form(response), validade_ssl(url), has_barra(url),
                 has_https(url), has_hifen(url), has_iframe(response)]

    return atributos


# Receber o objeto de resposta da página
def get_response(url: str) -> Response:
    return requests.get(url)

# A1 - Tamanho da URL
def tamanho_url(url: str) -> int:
    return len(url)

# A2 - Utiliza HTTPS
def use_https(url: str) -> bool:
    return "https" in url[0:7]

# A3 - Possui formato IP ///////////////////////////////////////////q
def has_ip_format(url: str) -> bool:
    return True

# A4 - Quantidade de pontos (.)
def points_number(url : str) -> int:
    return len(url.split(".")) -1

# A5 - Contem o caractere ’@’
def has_arroba(url : str) -> bool:
    return "@" in url

# A6 - Total de dias ativo ///////////////////////
def active_days(url : str) -> int:
    return 3

# A7 - PageRank
def pagerank_pontos(url: str) -> int:
    response = requests.get(
        "https://openpagerank.com/api/v1.0/getPageRank",
        headers={"API-OPR": OPEN_PAGE_RANK_API_KEY},
        params={"domains[]": [url]}
    ).json()

    if response.get("response")[0].get("page_rank_integer"):
        return response.get("response")[0].get("page_rank_integer")

    return 0

# A8 - Possui formulario HTML
def has_form(page : Response) -> bool:
    soup = BeautifulSoup(page.content, "html.parser")
    form = soup.find("form")
    return True if form is not None else False

# A9 - Validade do Certificado SSL
def validade_ssl(url : str) -> bool:
    response = requests.get(f"https://ssl-checker.io/api/v1/check/{url}").json()
    return response.get("result").get("cert_valid")

# A10 - Contem caracteres ’//’ Quando usado, exceto em ’https://’ ou ’http://’
def has_barra(url : str) -> bool:
    return "//" in url[7:]

# A11 - Possui texto ’https’ na URL
def has_https(url : str) -> bool:
    return "https" in url[7:]

# A12 - Possui caractere "-" no domínio
def has_hifen(url : str) -> bool:
    return "-" in url

# A13 - Possui iframe no codigo HTML
def has_iframe(page : Response) -> bool:
    soup = BeautifulSoup(page.content, "html.parser")
    iframe = soup.find("iframe")
    return True if iframe is not None else False
