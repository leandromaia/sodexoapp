function prepareDOM(obj) {
    Ext.DomHelper.append(Ext.getBody(), obj);
}

describe('View Balance', function(){

    var balanceForm = null;
    beforeEach(function () {
        prepareDOM({tag: 'div', id: 'test-balance'});
        balanceForm = Ext.create('Sodexoapp.view.consultation.Balance', {
            renderTo: 'test-balance'
        });
    });

    afterEach(function () {
            balanceForm.destroy();
            balanceForm = null;
        });


    it('exists', function() {
        expect(balanceForm.$className).toEqual('Sodexoapp.view.consultation.Balance');
    });

    it('should have balaceConsult xtype', function(){
        expect(balanceForm.isXType('balaceConsult')).toEqual(true);
    });

    it('should have expected items ', function(){
        var item = balanceForm.getComponent('consultPanel');
        expect(item).toBeDefined();
        expect(item.getComponent('captchaBox')).toBeDefined();
        expect(item.getComponent('captchaField')).toBeDefined();
        expect(item.getComponent('sendCaptcha')).toBeDefined();
        item = balanceForm.getComponent('infoPanel');
        expect(item).toBeDefined();
        item = item.getComponent('infoBox');
        expect(item).toBeDefined();
        expect(item.getComponent('infoBoxL')).toBeDefined();
        expect(item.getComponent('infoBoxR')).toBeDefined();
        expect(item.getComponent('infoBoxR').getComponent('dataValText')).toBeDefined();
        expect(item.getComponent('infoBoxR').getComponent('saldoValText')).toBeDefined();
        expect(item.getComponent('infoBoxR').getComponent('valorDiarioValText')).toBeDefined();
        expect(item.getComponent('infoBoxR').getComponent('diasRestantesValText')).toBeDefined();
        expect(item.getComponent('infoBoxR').getComponent('restoValText')).toBeDefined();
    });
});