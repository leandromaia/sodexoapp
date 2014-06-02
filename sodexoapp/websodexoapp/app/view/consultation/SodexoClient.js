Ext.define('Sodexoapp.view.consultation.SodexoClient',{
    extend:'Ext.form.Panel',
    alias: 'widget.profile',

    title: 'Criar Usuario',
    width: 500,
    margin: '30',

    bbar: [
        '->',
        {
            xtype:'button',
            itemId:'savebutton',
            text:'Confirmar',
            textAling:'center',
            action:'save'
        }
    ],

    initComponent: function(){
        this.items = [
            {
                xtype:'textfield',
                itemId:'profilename',
                fieldLabel:'Nome:',
                allowBlank:false,
                blankText: 'Campo Obrigatório',
                msgTarget: 'under',
                margin:'50 0 0 40',
                width:420
            },{
                xtype:'textfield',
                itemId:'profileuser',
                fieldLabel:'Usuario:',
                allowBlank:false,
                blankText: 'Campo Obrigatório',
                msgTarget: 'under',
                margin:'10 0 0 40',
                width:420
            },{
                xtype:'textfield',
                itemId:'profilepassword',
                fieldLabel:'Senha:',
                allowBlank:false,
                blankText: 'Campo Obrigatório',
                msgTarget: 'under',
                margin:'10 0 0 40',
                width:420,
                inputType: 'password'
            },{
                xtype:'textfield',
                itemId:'profilerepassword',
                fieldLabel:'Confirmar Senha:',
                allowBlank:false,
                blankText: 'Campo Obrigatório',
                msgTarget: 'under',
                margin:'10 0 0 40',
                width:420,
                inputType: 'password'
            },{
                xtype:'textfield',
                itemId:'profilecpf',
                fieldLabel:'CPF:',
                allowBlank:false,
                blankText: 'Campo Obrigatório',
                msgTarget: 'under',
                margin:'10 0 0 40',
                width:420,
                maskRe:/[0-9.]/,
                minLength: '11',
                maxLengthText:'CPF 11 digitos',
                minLengthText:'CPF 11 digitos'
            },{
                xtype:'textfield',
                itemId:'profilecard',
                fieldLabel:'N. Cartão',
                allowBlank:false,
                blankText: 'Campo Obrigatório',
                msgTarget: 'under',
                margin:'10 0 0 40',
                width:420,
                maskRe:/[0-9.]/
            },{
                xtype:'textfield',
                itemId:'profileemail',
                fieldLabel:'Email:',
                allowBlank:false,
                blankText: 'Campo Obrigatório',
                msgTarget: 'under',
                vtype: 'email',
                vtypeText: 'Formato inválido. Use o formato: "name@sample.com"',
                margin:'10 0 0 40',
                width:420
            },{
                xtype:'numberfield',
                itemId:'profilevalue',
                fieldLabel:'Valor Diario',
                allowBlank:false,
                blankText: 'Campo Obrigatório',
                msgTarget: 'under',
                margin:'10 0 10 40',
                width:420,
                maskRe: /[\d\.]/,
                minValue: '0.01',
                maxValue: '9999.00',
                minText:'Valor acimade R$0.01',
                maxText:'Valor abaixo de R$9999,00',
                hideTrigger: true
            }
        ];

        this.callParent(arguments);
    }
});