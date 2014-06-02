describe('Controller Balance', function() {
    var ctr;
    var view;

    beforeEach(function () {
        view = Ext.create('Sodexoapp.view.consultation.Balance');
        ctr = Ext.create('Sodexoapp.controller.consultation.Balance');
    });

    afterEach(function() {
    });

    it('should exist', function () {
        expect(ctr.$className).toEqual('Sodexoapp.controller.consultation.Balance');
    });

    it('should ref BalanceView', function() {
        var BalanceView = ctr.getBalanceView();
        expect(BalanceView).toBeDefined();
    });

    it('should ref BalanceView button send', function() {
        var btnsend = ctr.getSendCaptcha();
        expect(btnsend.text).toBe('Enviar');
    });

    it('buildPost method should be called if it exist', function () {
        spyOn(ctr, 'buildPost');
        ctr.buildPost();
        expect(ctr.buildPost).toHaveBeenCalled();
    });

    describe('Mocking Ajax controller calls', function() {

        beforeEach(function() {
            jasmine.Ajax.install();
            window.Sodexoapp = {Session: {}};

            Sodexoapp.Session.logged_user = {'id': 1 ,
                                             'username':  "admin",
                                             'email': 'admin@example.com'};
        });

        afterEach(function() {
            jasmine.Ajax.uninstall();
        });

        it('should make an AJAX request to the correct URL', function() {
            var controller = Ext.create('Sodexoapp.controller.consultation.Balance');
            //Setup for add valid text captch field
            controller.getCaptchField().setValue("fdasfd8");
            controller.buildPost(1);

            expect(jasmine.Ajax.requests.mostRecent().url).toContain('/consultation/balance');
        });

    });

});