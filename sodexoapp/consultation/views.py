# encoding: utf-8
from bs4 import BeautifulSoup
import requests
import json
import time
from decimal import *

from django.http import HttpResponse, \
                        HttpResponseBadRequest, \
                        HttpResponseNotAllowed

from consultation.models import SodexoClient


CAPTCHA_URL = 'https://sodexosaldocartao.com.br/saldocartao/jcaptcha.do'
POST_URL = 'https://sodexosaldocartao.com.br/saldocartao/'\
                                        'consultaSaldo.do?operation=consult'


def getCaptcha(request):
    session = requests.Session()
    r = session.get(CAPTCHA_URL)
    request.session['JSESSIONID'] = session.cookies['JSESSIONID']
    return HttpResponse(r.content)


def calculate_balance(request):
    if request.method not in ('POST'):
        return HttpResponseNotAllowed(
            ("Erro: Esta funcionalidade aceita\
             apenas os métodos POST"))

    jsonData = json.loads(request.body)

    if not jsonData:
        return HttpResponseBadRequest(
            ("Erro: Os parâmetros enviados estão incorretos"))

    user_id = jsonData['user_id']
    captcha_text = jsonData['captcha_text']

    if not user_id or not captcha_text:
        return HttpResponseBadRequest(\
            "Erro: Os parâmetros enviados estão incorretos")

    sodexo_client = SodexoClient.objects.get(user=user_id)
    session_id = request.session['JSESSIONID']

    sodexo_result = get_sodexo_balance(sodexo_client, captcha_text, session_id)

    if isinstance(sodexo_result, HttpResponseBadRequest):
        return sodexo_result

    balance_result = perform_calculation(sodexo_client, sodexo_result)
    response = HttpResponse(json.dumps(balance_result),
                                                content_type="text/html")
    return response


def get_sodexo_balance(sodexo_client, captcha_text, sodexo_session_id):
    post_data = {
                'service': '5;1;6',
                'cardNumber': sodexo_client.card_number,
                'cpf': sodexo_client.cpf,
                'jcaptcha_response': captcha_text,
                'x': '6',
                'y': '9',
            }

    cookie = {'JSESSIONID': sodexo_session_id}

    resp = requests.post(POST_URL, params=post_data, cookies=cookie)

    soup = BeautifulSoup(resp.content)
    error_message = soup.find("span", {"class": "textRed"})

    if not error_message:
        clientBalance = 0

        for link in soup.find_all(id='balance'):
            balance = link.find('var')
            clientBalance = Decimal(balance.string.split()[2])
        return clientBalance
    else:
        return HttpResponseBadRequest(error_message.get_text())


def perform_calculation(sodexo_client, balance):
    remaining_days = 0
    leftover = 0

    if balance >= sodexo_client.daily_value:
        remaining_days = int(balance / sodexo_client.daily_value)
        leftover = balance % sodexo_client.daily_value
    else:
        leftover = balance

    balance_result = {
        "date": time.strftime("%d/%m/%Y"),
        "balance": str(balance),
        "daily_value": str(sodexo_client.daily_value),
        "remaining_days": str(remaining_days),
        "leftover": str(leftover)
    }
    return balance_result
