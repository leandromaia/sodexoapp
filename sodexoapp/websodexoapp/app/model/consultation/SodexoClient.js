Ext.define('Sodexoapp.model.consultation.SodexoClient',{
    extend:'Ext.data.Model',
    fields: [
        {name:'id',type:'int'},
        {name:'name',type:'string'},
        {name:'cpf',type:'string'},
        {name:'card_number',type:'string'},
        {name: 'daily_value', type:'float'},
        {name: 'user'}
    ],
});