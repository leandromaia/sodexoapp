describe('Store User', function() {

    it('should exists',function() {
        var userStore = Ext.create('Sodexoapp.store.access.Users');
        expect(userStore.$className).toEqual('Sodexoapp.store.access.Users');
    });

    describe('Mocking Ajax', function() {

        beforeEach(function() {
            jasmine.Ajax.install();
        });

        afterEach(function() {
            jasmine.Ajax.uninstall();
        });

        it('should make an AJAX request to the correct URL', function() {
            var store = Ext.create('Sodexoapp.store.access.Users');
            store.load();

            expect(jasmine.Ajax.requests.mostRecent().url).toContain('/access/user');
        });

        it('makes a REST request to test the response data', function() {
            var idFn = jasmine.createSpy("success");
            var usernameFn = jasmine.createSpy("success");
            var emailFn = jasmine.createSpy("sucess");
            var passwordFn = jasmine.createSpy("sucess");

            var store = Ext.create('Sodexoapp.store.access.Users');

            store.on('load', function(store){
                var userFake = store.data.items[0].data;
                idFn(userFake.id);
                usernameFn(userFake.username);
                emailFn(userFake.email);
                passwordFn(userFake.password);
            });

            store.load();

            var mockedRequest = jasmine.Ajax.requests.mostRecent();

            mockedRequest.response({
                status:       200,
                responseText: "{success: 'true',"+
                               "result: ["+
                                   "{"+
                                       "id: '1',"+
                                       "username: 'zoio',"+
                                       "email: 'leandroc@inatel.br',"+
                                       "password: 'svcfasasdasd'}"+
                                "]}"
            });

            expect(idFn).toHaveBeenCalledWith(1);
            expect(usernameFn).toHaveBeenCalledWith('zoio');
            expect(emailFn).toHaveBeenCalledWith('leandroc@inatel.br');
            expect(passwordFn).toHaveBeenCalledWith('svcfasasdasd');
        });

        it('makes a REST request to load more than one user', function() {
            var countFn = jasmine.createSpy("success");

            var store = Ext.create('Sodexoapp.store.access.Users');

            store.on('load', function(store){
                countFn(store.data.length);
            });

            store.load();

            var mockedRequest = jasmine.Ajax.requests.mostRecent();

            mockedRequest.response({
                status:       200,
                responseText: "{success: 'true',"+
                               "result: ["+
                                   "{"+
                                       "id: '1',"+
                                       "username: 'zoio',"+
                                       "email: 'leandroc@inatel.br',"+
                                       "password: 'svcfasasdasd'},"+
                                   "{"+
                                       "id: '2',"+
                                       "username: 'corvo',"+
                                       "email: 'felipe.douglas@inatel.br',"+
                                       "password: 'fkfkfkfkfkfkfk'}"+
                                "]}"
            });

            expect(countFn).toHaveBeenCalledWith(2);
        });
    });
});

