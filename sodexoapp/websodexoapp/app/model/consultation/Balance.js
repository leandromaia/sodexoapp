Ext.define('Sodexoapp.model.consultation.Balance',{
    extend:'Ext.data.Model',
    fields: [
        {name:'id',type:'int'},
        {name:'date', type: 'date'},
        {name:'balance',type:'float'},
        {name:'daily_value',type:'float'},
        {name:'remaining_days',type:'int'},
        {name:'leftover',type:'float'},
    ],
});