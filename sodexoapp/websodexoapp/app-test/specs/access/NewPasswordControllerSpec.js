describe('Controller NewPassword', function() {
    var ctr;
    var view;

    beforeEach(function () {
        view = Ext.create('Sodexoapp.view.access.NewPassword');
        ctr = Ext.create('Sodexoapp.controller.access.NewPassword');
    });

    afterEach(function() {
    });

    it('should exist', function () {
        expect(ctr.$className).toEqual('Sodexoapp.controller.access.NewPassword');
    });

    it('should ref MyView', function() {
        var myView = ctr.getMyView();
        expect(myView).toBeDefined();
    });

    it('should ref MyView button confirm', function() {
        var btnsend = ctr.getMySendButton();
        expect(btnsend.text).toBe('Confirmar');
    });

    it('sendEmail method should be called if it exist', function () {
        spyOn(ctr, 'sendEmail');
        ctr.sendEmail();
        expect(ctr.sendEmail).toHaveBeenCalled();
    });

    describe('Mocking Ajax controller calls', function() {

        beforeEach(function() {
            jasmine.Ajax.install();
        });

        afterEach(function() {
            jasmine.Ajax.uninstall();
        });

        it('should make an AJAX request to the correct URL', function() {
            var controller = Ext.create('Sodexoapp.controller.access.NewPassword');
            controller.defineNewPassword(1);

            expect(jasmine.Ajax.requests.mostRecent().url).toContain('/access/userauthentication/1');
        });

    });
});
