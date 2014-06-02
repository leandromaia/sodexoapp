#coding: utf-8

from behave import step
from modules import *

#@step(u'')
#def eu_nome_classe(context):
#   nome_classe(context)

@step(u'que estou na pagina de login')
def eu_pagina_login_url(context):
	pagina_login_url(context)

@step(u'eu digito um login valido')
def eu_digito_login_valido(context):
	digito_login_valido(context)

@step(u'eu digito um login inexistente')
def eu_digito_login_inexistente(context):
    digito_login_inexistente(context)

@step(u'eu preencho o campo senha com uma senha valida')
def eu_digito_senha_valida(context):
	digito_senha_valida(context)

@step(u'eu clico em entrar')
def eu_clico_entrar(context):
	clico_entrar(context)

@step(u'eu acesso a pagina')
def eu_acesso_pagina(context):
	acesso_pagina(context)

@step(u'eu vejo mensagem de Usuário ou senha inválido')
def eu_vejo_mensagem_usuario_ou_senha_invalido(context):
	vejo_mensagem_usuario_ou_senha_invalido(context)

@step(u'eu clico em esqueci minha senha')
def eu_clico_link_esqueci_senha(context):
	clico_link_esqueci_senha(context)

@step(u'eu digito um email valido')
def eu_digito_email_valido(context):
	digito_email_valido(context)

@step(u'eu clico em enviar')
def eu_clico_enviar(context):
	clico_enviar(context)

@step(u'eu vejo mensagem de confirmação do envio de e-mail')
def eu_verifico_mensagem_email_enviado(context):	
	verifico_mensagem_email_enviado(context)

@step(u'eu vejo mensagem que o campo e-mail é obrigatorio')
def eu_verifico_mensagem_email_obrigatorio(context):
	verifico_mensagem_email_obrigatorio(context)

@step(u'eu digito um e-mail invalido')
def eu_digito_email_invalido(context):
	digito_email_invalido(context)

@step(u'eu vejo mensagem de formato email invalido')
def eu_verifico_mensagem_formato_email_invalido(context):
	verifico_mensagem_formato_email_invalido(context)

@step(u'eu digito um e-mail inexistente')
def eu_digito_email_inexistente(context):
	digito_email_inexistente(context)

@step(u'eu vejo mensagem de e-mail não encontrado')
def eu_verifico_mensagem_email_nao_encontrado(context):
	verifico_mensagem_email_nao_encontrado(context)


