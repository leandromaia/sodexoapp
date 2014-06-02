describe('Store SodexoClient', function() {

    it('should exists',function() {
        var userStore = Ext.create('Sodexoapp.store.consultation.SodexoClients');
        expect(userStore.$className).toEqual('Sodexoapp.store.consultation.SodexoClients');
    });

    describe('Mocking Ajax', function() {

        beforeEach(function() {
            jasmine.Ajax.install();
        });

        afterEach(function() {
            jasmine.Ajax.uninstall();
        });

        it('should make a request to the correct URL', function() {
            var store = Ext.create('Sodexoapp.store.consultation.SodexoClients');
            store.load();

            expect(jasmine.Ajax.requests.mostRecent().url).toContain('/consultation/sodexoclient');
        });

        it('should return the correct JSON into the response data', function() {
            var idDm = jasmine.createSpy("success");
            var cpfDm = jasmine.createSpy("success");
            var cardNumberDm = jasmine.createSpy("sucess");
            var dailyValueDm = jasmine.createSpy("success");

            var store = Ext.create('Sodexoapp.store.consultation.SodexoClients');

            store.on('load', function(store){
                var sodexoclientFake = store.data.items[0].data;
                idDm(sodexoclientFake.id);
                cpfDm(sodexoclientFake.cpf);
                cardNumberDm(sodexoclientFake.card_number);
                dailyValueDm(sodexoclientFake.daily_value);
            });

            store.load();

            var mockedRequest = jasmine.Ajax.requests.mostRecent();

            mockedRequest.response({
                status:       200,
                responseText: "{success: 'true',"+
                               "result: ["+
                                   "{"+
                                       "id: '1',"+
                                       "cpf: '24263676360',"+
                                       "card_number: '6598264110258',"+
                                       "daily_value: '19.6'}"+
                                "]}"
            });

            expect(idDm).toHaveBeenCalledWith(1);
            expect(cpfDm).toHaveBeenCalledWith('24263676360');
            expect(cardNumberDm).toHaveBeenCalledWith('6598264110258');
            expect(dailyValueDm).toHaveBeenCalledWith(19.6);
        });

        it('should return empty JSON when the response has the property success with false value', function() {
            var dataLength = jasmine.createSpy("success");

            var store = Ext.create('Sodexoapp.store.consultation.SodexoClients');

            store.on('load', function(store){
                dataLength(store.data.length);
            });

            store.load();

            var mockedRequest = jasmine.Ajax.requests.mostRecent();

            mockedRequest.response({
                status:       200,
                responseText: "{success: 'false',"+
                               "result: []}"
            });

            expect(dataLength).toHaveBeenCalledWith(0);
        });

        it('should filter by CPF field', function() {
            var idDm = jasmine.createSpy("success");
            var dataLength = jasmine.createSpy("success");

            var store = Ext.create('Sodexoapp.store.consultation.SodexoClients');

            store.on('load', function(store){
                var sodexoclientFake = store.data.items[0].data;
                dataLength(store.data.length);
                idDm(sodexoclientFake.id);
            });

            store.filter('cpf','43536100317');
            store.load();

            var mockedRequest = jasmine.Ajax.requests.mostRecent();

            mockedRequest.response({
                status:       200,
                responseText: "{success: 'true',"+
                               "result: ["+
                                   "{"+
                                       "id: '1',"+
                                       "cpf: '24263676360',"+
                                       "card_number: '6598264110258',"+
                                       "daily_value: '19.6'},"+
                                    "{"+
                                       "id: '2',"+
                                       "cpf: '43536100317',"+
                                       "card_number: '0455845012585',"+
                                       "daily_value: '15.5'}"+
                                "]}"
            });

            expect(dataLength).toHaveBeenCalledWith(1);
            expect(idDm).toHaveBeenCalledWith(2);
        });
    });
});