describe('Model User', function(){

    it('exists', function() {
        var model = Ext.create('Sodexoapp.model.access.User', {});
        expect(model.$className).toEqual('Sodexoapp.model.access.User');
    });

    it('has properties', function() {
        var model = Ext.create('Sodexoapp.model.access.User', {
            username:'defaultName',
            password:'123456',
            email:'defaultEmail@email.com'
        });
        expect(model.get('username')).toEqual('defaultName');
        expect(model.get('password')).toEqual('123456');
        expect(model.get('email')).toEqual('defaultEmail@email.com');
    });

    it('requires username', function() {
        var model = Ext.create('Sodexoapp.model.access.User',{
            password:'defaultName',
            email:'defaultEmail@email.com'
        });
        var validationResult = model.validate();
        expect(validationResult.isValid()).toBeFalsy();
    });

    it('requires password', function() {
        var model = Ext.create('Sodexoapp.model.access.User',{
            username:'defaultName',
            email:'defaultEmail@email.com'
        });
        var validationResult = model.validate();
        expect(validationResult.isValid()).toBeFalsy();
    });

    it('requires email', function() {
        var model = Ext.create('Sodexoapp.model.access.User',{
            username:'defaultName',
            password:'123456',
        });
        var validationResult = model.validate();
        expect(validationResult.isValid()).toBeFalsy();
    });

});