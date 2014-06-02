describe('Model SodexoClient', function(){

    it('exists', function() {
        var model = Ext.create('Sodexoapp.model.consultation.SodexoClient', {});
        expect(model.$className).toEqual('Sodexoapp.model.consultation.SodexoClient');
    });

    it('has properties', function() {
        var model = Ext.create('Sodexoapp.model.consultation.SodexoClient', {
            id: 1,
            cpf:'24263676360',
            card_number:'69784583651580',
            daily_value: 18.5,
            name: 'Heman'
        });

        expect(model.get('id')).toEqual(1);
        expect(model.get('cpf')).toEqual('24263676360');
        expect(model.get('card_number')).toEqual('69784583651580');
        expect(model.get('daily_value')).toEqual(18.5);
        expect(model.get('name')).toEqual('Heman');
    });
});
