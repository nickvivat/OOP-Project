import uuid
import datetime
from SearchRoom import SelectedRoom

class Payment:
    def __init__(self, member, info, method='', creditcard='', specialcode=''):
        self.__member = member
        self.__amount = info.get_total_cost()
        self.__info = info
        self.__method = method
        self.__creditcard = creditcard
        self.__specialcode = specialcode
        self.__status = 'PENDING'
        self.__transaction_id = None

    def process_payment(self, method):
        if method == 'credit card':
            return method
        else:
            return (f'Sorry we now have one method.')
            
    def discount_ccl(self, sc_type, sc_code, sc_list):
        for i in sc_list:
            if sc_type == i.get_type() and sc_code == i.get_code():
                divisor = int(i.get_discount()) / 100
                temp = self.__amount * divisor
                sum = self.__amount - temp
                self.__amount = str(sum)
                self.__specialcode = i
                return [(self.__amount),(self.__specialcode)]
            elif sc_code == '':
                self.__specialcode = ''
                return [(self.__amount),(self.__specialcode)]
        else:
            return 'F'

    def create_transaction(self):
        return str(uuid.uuid4())

    def get_member(self):
        return self.__member

    def get_status(self):
        return self.__status
    
    def set_status(self, newstatus):
        self.__status = newstatus

    def get_amount(self):
        return self.__amount

    def set_amount(self, newamount):
        self.__amount = newamount

    def get_method(self):
        return self.__method

    def set_method(self, newmethod):
        self.__method = newmethod
    
    def get_transaction_id(self):
        return self.__transaction_id
    
    def set_transaction_id(self, newtransaction_id):
        self.__transaction_id = newtransaction_id
    
    def get_creditcard(self):
        return self.__creditcard
    
    def set_creditcard(self, newcreditcard):
        self.__creditcard = newcreditcard
    
    def get_specialcode(self):
        return self.__specialcode
    
    def set_specialcode(self, newspecialcode):
        self.__specialcode = newspecialcode

    def __str__(self):
        return f"Payment details:\n"\
               f"Member: {self.__member}\n"\
               f"Amount: {self.__amount}\n"\
               f"Payment method: {self.__method}\n"\
               f"Credit card: {self.__creditcard}\n"\
               f"Special code: {self.__specialcode}\n"\
               f"Status: {self.__status}\n"\
               f"Transaction ID: {self.__transaction_id}"


class PaymentHistory:
    def __init__(self):
        self.__payment_history = []

    def add_pm_history(self, payment):
        self.__payment_history.append(payment)
        
    @property
    def pm_history(self):
        return self.__payment_history


class SpecialCode:
    def __init__(self, type='', code='', discount=''):
        self.__type = type # iata number, promo code, group code
        self.__code = code
        self.__discount = discount
        self.__sc_list = []
    
    def add_sc_list(self, sc):
        self.__sc_list.append(sc)
        
    def remove_sc(self, sc):
        self.__sc_list.remove(sc)
        
    def get_type(self):
        return self.__type
    
    def get_code(self):
        return self.__code
    
    def get_discount(self):
        return self.__discount
    
    def get_sc_list(self):
        return self.__sc_list


class CreditcardInfo:
    def __init__(self, card_number = '', cardholder_name = '', expiration_date = ''):
        self.__card_number = card_number
        self.__cardholder_name = cardholder_name
        self.__expiration_date = expiration_date
        
    def check_creditcard(self, card_number, cardholder_name, expiration_date):
        if len(card_number) != 16:
            return 'incorrect number'
        
        try:
            exp_date = datetime.datetime.strptime(expiration_date, '%m/%y')
        except ValueError:
            return 'error'
        
        current_date = datetime.datetime.now()
        if exp_date < current_date:
            return 'This card is expired'
        
        return 'success'