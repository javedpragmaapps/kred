class SalesAndMarketplaceModel:
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
            self._name = value
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
            raise ValueError('count must be a int')

class AuctionsModel:
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
            raise ValueError('count must be a int')


class MarketplaceModel:
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
            self._name = value
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
            raise ValueError('count must be a int')


class SellModel:
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
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        if isinstance(value,float):
            self._price=value
        else:
            raise ValueError('price must be a float')

class Auction:
    def __init__(self):
        pass

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self,value):
        if isinstance(value,str):
            self._mode=value
        else:
            raise ValueError('mode must be a str')

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
    def reserve(self):
        return self._reserve

    @reserve.setter
    def reserve(self, value):
        if isinstance(value, float):
            self._reserve = value
        else:
            raise ValueError('reserve must be a float')

    @property
    def maximum(self):
        return self._maximum

    @maximum.setter
    def maximum(self,value):
        if isinstance(value,float):
            self._maximum =value
        else:
            raise  ValueError('Maximum must be a float')

    @property
    def minimum(self):
        return self._minimum

    @minimum.setter
    def minimum(self, value):
        if isinstance(value, float):
            self._minimum = value
        else:
            raise ValueError('Minimum must be a float')

    @property
    def start(self):
        return  self._start

    @start.setter
    def start(self,value):
        if isinstance(value,int):
            self._start=value
        else:
            raise ValueError('Start must be a int')

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        if isinstance(value, int):
            self._end = value
        else:
            raise ValueError('End must be a int')

class ShowcaseAndUnshowcaseModel:
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
        if isinstance(value, int):
            self._sequence = value
        else:
            raise ValueError('sequence must be a int')

    @property
    def text(self):
        return  self._text

    @text.setter
    def text(self,value):
        if isinstance(value,str):
            self._text=value
        else:
            raise ValueError('Text must be a str')

class TagModel:
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
        if isinstance(value, int):
            self._sequence = value
        else:
            raise ValueError('sequence must be a int')

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self,value):
        if isinstance(value,str):
            self.tags= value
        else:
            raise ValueError('tags must be a str')

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        if isinstance(value, str):
            self._mode = value
        else:
            raise ValueError('mode must be a str')

class LockAndUnlockModel:
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
        if isinstance(value, int):
            self._sequence = value
        else:
            raise ValueError('sequence must be a int')

    @property
    def text(self):
        return  self._text

    @text.setter
    def text(self,value):
        if isinstance(value,str):
            self._text=value
        else:
            raise ValueError('Text must be a str')

class HideAndShow:
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
        if isinstance(value, int):
            self._sequence = value
        else:
            raise ValueError('sequence must be a int')

    @property
    def request(self):
        return self._request

    @request.setter
    def request(self, value):
        if isinstance(value, int):
            self._request = value
        else:
            raise ValueError('Request must be a int')


    @property
    def text(self):
        return  self._text

    @text.setter
    def text(self,value):
        if isinstance(value,str):
            self._text=value
        else:
            raise ValueError('Text must be a str')











