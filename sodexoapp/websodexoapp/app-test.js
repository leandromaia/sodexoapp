Ext.Loader.setConfig({
    enabled: true
});

Ext.application({
    requires: ['Ext.container.Viewport'],
    name: 'Sodexoapp',

    appFolder: 'app',

    controllers: [
        'access.NewPassword',
        'consultation.SodexoClient',
        'consultation.Balance'
    ],

    autoCreateViewport: false
});