Ext.define('Sodexoapp.controller.consultation.SodexoClient',{
    extend:'Ext.app.Controller',

    views: [
        'consultation.SodexoClient'
    ],

    refs: [
        {ref: 'profile', selector: 'profile'},
        {ref: 'name', selector: 'profile #profilename'},
        {ref: 'username', selector: 'profile #profileuser'},
        {ref: 'password', selector: 'profile #profilepassword'},
        {ref: 'rePassword', selector: 'profile #profilerepassword'},
        {ref: 'cpf', selector: 'profile #profilecpf'},
        {ref: 'card', selector: 'profile #profilecard'},
        {ref: 'email', selector: 'profile #profileemail'},
        {ref: 'dailyValue', selector: 'profile #profilevalue'},
    ],

    init: function(){
         this.control({
            'profile button[itemId=savebutton]': {
                click: this.saveData
            },
            'profile textfield[itemId=profileuser]':{
                blur: this.userExists
            },
            'profile textfield[itemId=profileemail]':{
                blur: this.emailExists
            },
            'profile textfield[itemId=profilecpf]':{
                blur: this.cpfExists
            }
        });
    },

    saveData: function(button){
        var rePasswordField = this.getRePassword();
        var passwordField = this.getPassword();

        if(passwordField.getValue() != rePasswordField.getValue()) {
            passwordField.markInvalid('senhas diferem');

        } else if(this.getProfile().getForm().isValid()){
            var data = {
               name:this.getName().getValue(),
               cpf: this.getCpf().getValue(),
               card_number: this.getCard().getValue(),
               daily_value: this.getDailyValue().getValue(),
               user: {
                    username: this.getUsername().getValue(),
                    password: passwordField.getValue(),
                    email: this.getEmail().getValue()
               }
            };

            Ext.Ajax.request({
                url : '/consultation/sodexoclient',
                method: 'POST',
                header:{'Content-Type': 'application/json'},
                jsonData: data,
                scope: this,
                success: function(response, eOpts){
                    var msgSuccess = Ext.String.format("O seu usuário: {0} foi criado com sucesso.\n"+
                        "Você recebeu um email confirmando o seu cadastro.", this.getName().getValue());
                    window.location = './access/login?report_msg='+ msgSuccess;
                },
                failure: function(response, opts) {
                    console.error(response.responseText);
                    var msgError = "Ocorreu uma falha ao criar seu usuário. "+
                        "Por favor, entre em contato com o administrador do sistema.";
                    window.location = './access/login?error_msg='+msgError;
                }
            });
        }
    },

    userExists: function(){
        var userField = this.getUsername();

        var store = Ext.create('Sodexoapp.store.access.Users');
        store.on('load', function(store){
            if(store.getCount() > 0) {
                userField.markInvalid('Usuário já existente');
            }
        },this);
        store.filter('username',userField.getValue());
        store.load();
    },

    emailExists: function(){
        var emailField = this.getEmail();

        var store = Ext.create('Sodexoapp.store.access.Users');
        store.on('load', function(store){
            if(store.getCount() > 0) {
                emailField.markInvalid('Email já existente');
            }
        },this);
        store.filter('email',emailField.getValue());
        store.load();
    },

    cpfExists: function(){
        var cpfField = this.getCpf();

        var store = Ext.create('Sodexoapp.store.consultation.SodexoClients');
        store.on('load', function(store){
            if(store.getCount() > 0) {
                cpfField.markInvalid('CPF já existente');
            }
        },this);
        store.filter('cpf',cpfField.getValue());
        store.load();
    }
});