Ext.define('Sodexoapp.store.consultation.SodexoClients',{
    extend:'Ext.data.Store',
    model: 'Sodexoapp.model.consultation.SodexoClient',
    proxy: {
        type: 'rest',
        url: '/consultation/sodexoclient',

        reader: {
            type: 'json',
            root: 'result',
            successProperty: 'success'
        }
    }
});