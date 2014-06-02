Ext.define('Sodexoapp.controller.access.NewPassword', {
    extend:'Ext.app.Controller',

    views: [
        'access.NewPassword'
    ],

    refs: [
        {ref: 'myView', selector: 'newpassword'},
        {ref: 'mySendButton', selector: 'newpassword #sendEmailBtn'},
        {ref: 'emailField', selector: 'newpassword #emailField'},
        {ref: 'errorBox', selector: 'newpassword #errorBox'}
    ],

    init : function(){
        this.control({
            'newpassword #sendEmailBtn':{
                click: this.sendEmail
            },
        });
    },

    getCmpView: function(component){
        if(component.getId().match('newpassword')){
            return component;
        }
        return component.up('newpassword');
    },

    sendEmail: function(button){
        var view = this.getCmpView(button);
        var email = view.down('#emailField');

        if(email.isValid()) {
            var store = Ext.create('Sodexoapp.store.access.Users');
            store.on('load', function(store){
                if(store.getCount()===0) {
                    email.markInvalid('Email nao encontrado');
                }else {
                    var user = store.data.items[0].data;
                    this.defineNewPassword(user.id);
                }
            },this);

            store.filter('email',email.getValue());
            store.load();
        }
    },

    defineNewPassword : function(userId){
        var view = this.getMyView();
        var email = view.down('#emailField');

        Ext.Ajax.request({
            url : '/access/userauthentication/'+userId,
            method: 'PUT',
            scope: this,
            success: function(response, eOpts){
                var jsonResponse = Ext.JSON.decode(response.responseText);
                window.location = './access/login?report_msg='+jsonResponse.result;
            },
            failure: function(response, opts) {
                console.error("Failed to define new password: "+response.statusText);
                email.markInvalid("Ocorreu uma falha ao enviar o email com a nova senha. "+
                                    "Por favor, tente mais tarde.");
            }
        });
    }
});