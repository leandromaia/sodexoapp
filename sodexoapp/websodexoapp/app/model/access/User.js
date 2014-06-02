Ext.define('Sodexoapp.model.access.User',{
    extend:'Ext.data.Model',
    fields: [
        {name:'id',type:'int'},
        {name:'username',type:'string'},
        {name:'password',type:'string'},
        {name:'email',type:'string'}
    ],
    validations: [
        {type: 'presence', field: 'username', message: "Preencha o campo nome"},
        {type: 'presence', field: 'password', message: "Preencha o campo senha"},
        {type: 'presence', field: 'email', message: "Preencha o campo email"},
    ]
});