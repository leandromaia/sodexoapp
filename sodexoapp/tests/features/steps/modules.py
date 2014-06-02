#coding: utf-8
#from selenium import webdriver
#from selenium.webdriver.support.select import Select
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.keys import Keys
from splinter import Browser
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
#import ipdb
import os
from nose import tools

def pagina_login_url(context):
	url = 'http://127.0.0.1:8000/access/login?next=/'
	context.driver.visit(url)

def digito_login_valido(context):
	campo_login = context.driver.find_by_xpath('//*[@id="username"]')
	campo_login.type('admin')

def digito_login_inexistente(context):
    campo_login = context.driver.find_by_xpath('//*[@id="username"]')
    campo_login.type('teste')

def digito_senha_valida(context):
	campo_senha = context.driver.find_by_xpath('//*[@id="password"]') 
	campo_senha.type('admin')

def clico_entrar(context):
	submit = context.driver.find_by_xpath('/html/body/div/div/form/div[2]/input')
	submit.first.click()

def acesso_pagina(context):
	frase = context.driver.find_by_xpath('//*[@id="panel-1002-innerCt"]')
	context.driver.is_text_present('List of users will go here', wait_time=2)

def vejo_mensagem_usuario_ou_senha_invalido(context):
	frase = context.driver.find_by_xpath('/html/body/div/div[1]')
	context.driver.is_text_present('Usuário ou senha inválido', wait_time=2)

def clico_link_esqueci_senha(context):
	link = context.driver.find_by_xpath('/html/body/div/div/form/div[1]/div[1]/a')
	link.click()

def digito_email_valido(context):
	campo_email = context.driver.find_by_xpath('//*[@id="textfield-1003-inputEl"]')
	campo_email.type('ricardo.franca@ispm.com.br')

def clico_enviar(context):
	submit2 = context.driver.find_by_xpath('//*[@id="button-1006-btnIconEl"]')			
	submit2.first.click()

def verifico_mensagem_email_enviado(context):
	#texto = context.driver.find_by_xpath('/html/body/div/div[1]')
	texto = context.driver.find_by_css("div.reportmsg")
	context.driver.is_text_present('Sua nova senha foi gerada com sucesso e enviada por email', wait_time=2)

def verifico_mensagem_email_obrigatorio(context):
	texto = context.driver.find_by_xpath('//*[@id="textfield-1003-errorEl"]/ul/li')
	context.driver.is_text_present('Campo Obrigatorio', wait_time=2)

def digito_email_invalido(context):
    campo_email = context.driver.find_by_xpath('//*[@id="textfield-1003-inputEl"]')
    campo_email.type('ricardo.franca@gmail')

def verifico_mensagem_formato_email_invalido(context):
	texto = context.driver.find_by_xpath('//*[@id="textfield-1003-errorEl"]/ul/li')	
	context.driver.is_text_present('Formato invalido. Use o formato: "name@sample.com"', wait_time=2)

def digito_email_inexistente(context):
    campo_email = context.driver.find_by_xpath('//*[@id="textfield-1003-inputEl"]')
    campo_email.type('ricardo.franca@gmail.com')

def verifico_mensagem_email_nao_encontrado(context):
    #texto = context.driver.find_by_xpath('//*[@id="textfield-1003-errorEl"]/ul/li')
	texto = context.driver.find_by_xpath('//*[@id="textfield-1003-errorEl"]')
	context.driver.is_text_present('Emaiool nao encontrado', wait_time=2)
	
