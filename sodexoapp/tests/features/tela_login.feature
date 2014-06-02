#coding: utf-8
#language: pt

Funcionalidade: Login e password recovery

    Cenário: Login com sucesso

        Dado que estou na pagina de login
        Quando eu digito um login valido
        E eu preencho o campo senha com uma senha valida
		E eu clico em entrar
        Então eu acesso a pagina

	Cenário: Login sem sucesso
		
		Dado que estou na pagina de login
		Quando eu digito um login inexistente
		E eu preencho o campo senha com uma senha valida
		E eu clico em entrar
		Então eu vejo mensagem de Usuário ou senha inválido

	Cenário: Campo login em branco
		
		Dado que estou na pagina de login
		Quando eu preencho o campo senha com uma senha valida
        E eu clico em entrar
		Então eu vejo mensagem de Usuário ou senha inválido

	Cenário: Campo senha em branco

        Dado que estou na pagina de login
        Quando eu digito um login valido
        E eu clico em entrar
        Então eu vejo mensagem de Usuário ou senha inválido

	Cenário: Campo login e senha em branco

        Dado que estou na pagina de login
        Quando eu clico em entrar
        Então eu vejo mensagem de Usuário ou senha inválido

		
	Cenário: Esqueci minha senha
		
        Dado que estou na pagina de login
        Quando eu clico em esqueci minha senha
		E eu digito um email valido
        E eu clico em enviar
		Então eu vejo mensagem de confirmação do envio de e-mail	

	
	Cenário: Envio de senha sem preencher o campo e-mail

        Dado que estou na pagina de login
        Quando eu clico em esqueci minha senha
		E eu clico em enviar
		Então eu vejo mensagem que o campo e-mail é obrigatorio
	
	@wip
	Cenário: Tentar recuperar senha com e-mail invalido
		
        Dado que estou na pagina de login
        Quando eu clico em esqueci minha senha
		E eu digito um e-mail invalido
		E eu clico em enviar
		Então eu vejo mensagem de formato email invalido

 	Cenário: Tentar recuperar senha com e-mail inexistente

        Dado que estou na pagina de login
        Quando eu clico em esqueci minha senha      
        E eu digito um e-mail inexistente
        E eu clico em enviar
        Então eu vejo mensagem de e-mail não encontrado

