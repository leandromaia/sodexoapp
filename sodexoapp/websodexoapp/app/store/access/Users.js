Ext.define('Sodexoapp.store.access.Users',{
    extend:'Ext.data.Store',
    model: 'Sodexoapp.model.access.User',

    proxy: {
        type: 'rest',
        url: '/access/user',

        reader: {
            type: 'json',
            root: 'result',
            successProperty: 'success'
        }
    }
});