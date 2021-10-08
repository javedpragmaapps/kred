
class SendModel:
    def __init__(self):
        pass

    @property
    def nft(self):
        return self._nft

    @nft.setter
    def nft(self, value):
        if isinstance(value, int):
            self._nft = value
        else:
            raise ValueError('nft must be a int')

    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        if isinstance(value, str):
            self._uuid = value
        else:
            raise ValueError('uuid must be a str')

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        if isinstance(value, str):
            self._symbol = value
        else:
            raise ValueError('symbol must be a str')

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        if isinstance(value, str):
            self._sequence = value
        else:
            raise ValueError('sequence must be a int')

    @property
    def request(self):
        return self._request

    @request.setter
    def request(self, value):
        if isinstance(value, str):
            self._request = value
        else:
            raise ValueError('request must be a str')

    @property
    def wallet(self):
        return self._wallet

    @wallet.setter
    def wallet(self, value):
        if isinstance(value, str):
            self._wallet = value
        else:
            raise ValueError('request must be a str')

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if isinstance(value, str):
            self._text = value
        else:
            raise ValueError('request must be a str')

class HoldModel:
    def __init__(self):
        pass

    @property
    def nft(self):
        return self._nft

    @nft.setter
    def nft(self, value):
        if isinstance(value, int):
            self._nft = value
        else:
            raise ValueError('nft must be a int')

    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        if isinstance(value, str):
            self._uuid = value
        else:
            raise ValueError('uuid must be a str')

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        if isinstance(value, str):
            self._symbol = value
        else:
            raise ValueError('symbol must be a str')

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        if isinstance(value, str):
            self._sequence = value
        else:
            raise ValueError('sequence must be a str')

    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        if isinstance(value, str):
            self._platform = value
        else:
            raise ValueError('platform must be a str')

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if isinstance(value, str):
            self._address = value
        else:
            raise ValueError('address must be a str')

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):
        if isinstance(value, int):
            self._hours = value
        else:
            raise ValueError('hours must be a int')



    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if isinstance(value, str):
            self._text = value
        else:
            raise ValueError('request must be a str')

class RequestModel:
    def __init__(self):
        pass

    @property
    def nft(self):
        return self._nft

    @nft.setter
    def nft(self, value):
        if isinstance(value, str):
            self._nft = value
        else:
            raise ValueError('nft must be a str')

    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        if isinstance(value, str):
            self._uuid = value
        else:
            raise ValueError('uuid must be a str')

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        if isinstance(value, str):
            self._symbol = value
        else:
            raise ValueError('symbol must be a str')

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        if isinstance(value, str):
            self._sequence = value
        else:
            raise ValueError('sequence must be a str')

    @property
    def wallet(self):
        return self._wallet

    @wallet.setter
    def wallet(self,value):
        if isinstance(value,float):
            self._wallet=value
        else:
            raise ValueError('Wallet must be a float')

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if isinstance(value, str):
            self._text = value
        else:
            raise ValueError('text must be a str')



class RequestsModel:
    def __init__(self):
        pass

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if isinstance(value, str):
            self._user = value
        else:
            raise ValueError('user must be a str')

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, value):
        if isinstance(value, str):
            self._sender = value
        else:
            raise ValueError('sender must be a str')

    @property
    def nft(self):
        return self._nft

    @nft.setter
    def nft(self, value):
        if isinstance(value, int):
            self._nft = value
        else:
            raise ValueError('nft must be a int')

    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        if isinstance(value, str):
            self._uuid = value
        else:
            raise ValueError('uuid must be a str')

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        if isinstance(value, str):
            self._symbol = value
        else:
            raise ValueError('symbol must be a str')

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        if isinstance(value, str):
            self._sequence = value
        else:
            raise ValueError('sequence must be a str')

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        if isinstance(value, str):
            self._currency = value
        else:
            raise ValueError('currency must be a str')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name= value
        else:
            raise ValueError('name must be a str')

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        if isinstance(value, int):
            self._count = value
        else:
            raise ValueError('count must be a int')

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        if isinstance(value, int):
            self._page = value
        else:
            raise ValueError('page must be a int')
