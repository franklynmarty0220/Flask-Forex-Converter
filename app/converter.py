from forex_python.converter import CurrencyRates, CurrencyCodes

cr = CurrencyRates(force_decimal=True)
cc = CurrencyCodes()

class Currency():

    def __init__(self,init):
        self.currency_name = self.currency_name(init)
        self.currency_rate = self.currency_rate(init)
        self.currency_symbol = self.currency_symbol(init)
        self.init = init

    def currency_name(self,init):

        
        c_name = cc.get_currency_name(init)
        return c_name

    def currency_rate(self,init):

        cr = CurrencyRates()
        cr_rate = cr.get_rate(init)
        return cr_rate

    def conversion_rate(self,init, new):

        cr = CurrencyRates()
        conv_rate = cr.get_rate(init, new)
        return conv_rate

    def convert_amount(self,init, new, amount):
        
        currency = CurrencyRates()
        curr_conversion = currency.convert(init,new,amount)
        return curr_conversion

    def currency_symbol(self,init):

        symbol = cc.get_symbol(init)
        return symbol

    def check_curr_validity(self,init):

        currencies = open("supported_curr.txt", "r")
        alert = "Not Vailid Currency"

        if init in currencies:
            return init
        else:
            return alert
    
    def check_amount_validity(self, amount):

        amount_alert = "Not Valid Amount."

        if type(amount) == int or type(amount) == float:
            return amount
        else:
            return amount_alert
