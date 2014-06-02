Ext.define('Sodexoapp.view.consultation.Balance', {
    extend:'Ext.panel.Panel',
    alias: 'widget.balaceConsult',

    header: false,
    height: 600,
    title: 'Container Panel',


    initComponent: function() {

        this.items = [
            {
                xtype: 'panel',
                header: false,
                itemId: 'consultPanel',
                border: 0,
                layout: {
                    type: 'vbox',
                    align: 'center'
                },
                items:[
                    {
                        xtype: 'text',
                        text: 'Consulta do saldo:',
                        margin: "5",
                        style: {
                            fontSize: '16px'
                        }
                    },
                    {
                        xtype: 'component',
                        header: false,
                        itemId: 'captchaBox',
                        height: 80,
                        width: 200,
                        margin: "10 0 10 0",
                        autoEl: {
                            tag:'div', children:[
                                {
                                    tag:'img',
                                    src:'/consultation/getCaptcha',
                                    width: '100%',
                                    name:'image',
                                    id:'captchaImage'
                                }
                            ]
                        }
                    },
                    {
                        xtype: 'textfield',
                        itemId:'captchaField',
                        fieldLabel:'Captcha',
                        labelWidth: 50,
                        margin: "5 0 5 0",
                        allowBlank:false,
                        blankText: 'Campo Obrigatório',
                        msgTarget: 'under',
                        listeners: {
                            afterrender: function(field) {
                                field.focus();
                            }
                        },
                    },
                    {
                        xtype: 'button',
                        text : 'Enviar',
                        itemId: 'sendCaptcha',
                        margin: "10 0 10 0"
                    }
                ]
            },
            {
                xtype: 'panel',
                header: false,
                itemId: 'infoPanel',
                border: 0,
                layout: {
                    type: 'vbox',
                    align: 'center'
                },
                items:[
                    {
                        xtype: 'panel',
                        header: false,
                        itemId: 'infoBox',
                        width: 350,
                        border: '10 10 10 10',
                        hidden: true,
                        layout: 'column',
                        items:[
                            {
                                xtype: 'panel',
                                header: false,
                                itemId: 'infoBoxL',
                                columnWidth: 0.5,
                                border: 0,
                                layout: {
                                    type: 'vbox',
                                    align: 'left'
                                },
                                items:[
                                    {
                                        xtype: 'text',
                                        text: 'Data:',
                                        margin: "5"
                                    },
                                    {
                                        xtype: 'text',
                                        text: 'Saldo:',
                                        margin: "5"
                                    },
                                    {
                                        xtype: 'text',
                                        text: 'Valor Diário:',
                                        margin: "5"
                                    },
                                    {
                                        xtype: 'text',
                                        text: 'Dias Restantes:',
                                        margin: "5"
                                    },
                                    {
                                        xtype: 'text',
                                        text: 'Resto:',
                                        margin: "5"
                                    },
                                ]
                            },
                            {
                                xtype: 'panel',
                                header: false,
                                itemId: 'infoBoxR',
                                columnWidth: 0.5,
                                border: 0,
                                layout: {
                                    type: 'vbox',
                                    align: 'right'
                                },
                                items:[
                                    {
                                        itemId: 'dataValText',
                                        xtype: 'text',
                                        text: '',
                                        margin: "5"
                                    },
                                    {
                                        itemId: 'saldoValText',
                                        xtype: 'text',
                                        text: '',
                                        margin: "5"
                                    },
                                    {
                                        itemId: 'valorDiarioValText',
                                        xtype: 'text',
                                        text: '-',
                                        margin: "5"
                                    },
                                    {
                                        itemId: 'diasRestantesValText',
                                        xtype: 'text',
                                        text: '',
                                        margin: "5"
                                    },
                                    {
                                        itemId: 'restoValText',
                                        xtype: 'text',
                                        text: '',
                                        margin: "5"
                                    },
                                ]
                            }
                        ]
                    },
                ]
            }
        ];
        this.callParent(arguments);
    }

});