Ext.define('Sodexoapp.controller.consultation.Balance', {
    extend:'Ext.app.Controller',

    views: [
        'consultation.Balance'
    ],

    refs: [
        {ref: 'balanceView', selector: 'balaceConsult'},
        {ref: 'captchField', selector: 'balaceConsult #captchaField'},
        {ref: 'sendCaptcha', selector: 'balaceConsult #sendCaptcha'},
        {ref: 'infoBox', selector: 'balaceConsult #infoBox'},
        {ref: 'dataValText', selector: 'balaceConsult #dataValText'},
        {ref: 'saldoValText', selector: 'balaceConsult #saldoValText'},
        {ref: 'valorDiarioValText', selector: 'balaceConsult #valorDiarioValText'},
        {ref: 'diasRestantesValText', selector: 'balaceConsult #diasRestantesValText'},
        {ref: 'restoValText', selector: 'balaceConsult #restoValText'},
        {ref: 'captchaBox', selector: 'balaceConsult #captchaBox'}
    ],

    init: function(){
         this.control({
            'balaceConsult button[itemId=sendCaptcha]': {
                click: this.buildPost
            }
        });
    },

    buildPost: function(button){
        if(this.getCaptchField().isValid()){
            var captchText = this.getCaptchField().getValue();
            var user = Sodexoapp.Session.logged_user;
            Ext.Ajax.request({
                url: '/consultation/balance',
                method: 'POST',
                scope: this,
                jsonData: {
                    "user_id" : user.id,
                    "captcha_text" : captchText,
                },
                success: function(response){
                    var jsonResponse = Ext.JSON.decode(response.responseText);
                    this.setTexts(jsonResponse);
                    Ext.get('captchaImage').dom.src = "/consultation/getCaptcha";
                    this.getCaptchField().reset();
                },
                failure: function(response){
                    Ext.get('captchaImage').dom.src = "/consultation/getCaptcha";
                    this.getCaptchField().markInvalid(response.responseText);
                    this.getInfoBox().setVisible(false);
                }
            });
        }
    },

    setTexts: function(balance){

        var infoBox = this.getInfoBox();
        var dataValText = this.getDataValText();
        var saldoValText = this.getSaldoValText();
        var valorDiarioValText = this.getValorDiarioValText();
        var diasRestantesValText = this.getDiasRestantesValText();
        var restoValText = this.getRestoValText();

        dataValText.setText(balance.date);
        saldoValText.setText(balance.balance);
        valorDiarioValText.setText(balance.daily_value);
        diasRestantesValText.setText(balance.remaining_days);
        restoValText.setText(balance.leftover);
        infoBox.setVisible(true);
    }
});