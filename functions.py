from traceback import print_tb

import pandas as pd
from requests import Response
import re
from keys import OPEN_PAGE_RANK_API_KEY
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

#
# Receber Parâmetros da URL
#

def get_row(url: str) -> pd.DataFrame:
    response = get_response(url)
    ssl_response = get_ssl_response(url)

    parsed_url = urlparse(url)
    scheme = parsed_url.scheme
    host = parsed_url.hostname

    atributos = [tamanho_url(url), use_https(scheme), has_ip_format(url),
                 points_number(url), has_arroba(url), has_form(response),
                 active_days(ssl_response), pagerank_pontos(url), validade_ssl(ssl_response),
                 has_barra(host), has_https_text(host), has_hifen(url),
                 has_iframe(response)]

    return pd.DataFrame(columns= ["url_lenght", "is_https", "ip_format",
                                  "dot_count", "suspect_char", "html_input",
                                  "activate_days", "page_rank", "certificate",
                                  "redirect", "https_text", "caract_hifen",
                                  "iframe"],
                        data=[atributos], )


# Receber o objeto de resposta da página
def get_response(url: str) -> Response:
    return requests.get(url)

# Receber o objeto de resposta da API de certificado SSL
def get_ssl_response(url: str) -> Response:
    return requests.get(f"https://ssl-checker.io/api/v1/check/{url[8:]}")

# A1 - Tamanho da URL
def tamanho_url(url: str) -> int:
    return len(url)

# A2 - Utiliza HTTPS
def use_https(scheme: str) -> bool:
    return "https" in scheme

# A3 - Possui formato IP
def has_ip_format(url: str) -> bool:
    padrao = r'^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$'
    return True if re.match(padrao, url) else False

# A4 - Quantidade de pontos (.)
def points_number(url : str) -> int:
    return len(url.split(".")) - 1

# A5 - Contem o caractere ’@’
def has_arroba(url : str) -> bool:
    return "@" in url

# A6 - Total de dias ativo
def active_days(response : Response) -> int:
    json = response.json()
    return json.get("result").get("validity_days") - json.get("result").get("days_left")

# A7 - PageRank
def pagerank_pontos(url: str) -> float:
    response = requests.get(
        "https://openpagerank.com/api/v1.0/getPageRank",
        headers={"API-OPR": OPEN_PAGE_RANK_API_KEY},
        params={"domains[]": [url]}
    ).json()

    if response.get("response")[0].get("page_rank_decimal"):
        return response.get("response")[0].get("page_rank_decimal")

    return 0

# A8 - Possui formulario HTML
def has_form(page : Response) -> bool:
    soup = BeautifulSoup(page.content, "html.parser")
    form = soup.find("form")
    return True if form is not None else False

# A9 - Validade do Certificado SSL
def validade_ssl(response : Response) -> bool:
    return response.json().get("result").get("cert_valid")

# A10 - Contem caracteres ’//’ Quando usado, exceto em ’https://’ ou ’http://’
def has_barra(host : str) -> bool:
    return "//" in host

# A11 - Possui texto ’https’ na URL
def has_https_text(host : str) -> bool:
    return "https" in host

# A12 - Possui caractere "-" no domínio
def has_hifen(url : str) -> bool:
    return "-" in url

# A13 - Possui iframe no codigo HTML
def has_iframe(page : Response) -> bool:
    soup = BeautifulSoup(page.content, "html.parser")
    iframe = soup.find("iframe")
    return True if iframe is not None else False
