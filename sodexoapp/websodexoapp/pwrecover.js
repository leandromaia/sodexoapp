Ext.application({
    requires: ['Ext.container.Viewport'],
    name: 'Sodexoapp',

    appFolder: '/static/app',

    controllers: [
        'access.NewPassword'
    ],

    launch: function() {
        Ext.create('Ext.container.Viewport', {
            layout: {
                type: 'vbox',
                align: 'center'
            },
            items: [
                {
                    xtype: 'newpassword',
                    layout: {align:'center'}
                }
            ]
        });
    }
});