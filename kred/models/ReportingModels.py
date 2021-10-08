class HistoryModel:
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
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if isinstance(value, str):
            self._user = value
        else:
            raise ValueError('user must be a str')

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        if isinstance(value, str):
            self._action = value
        else:
            raise ValueError('action must be a str')

    @property
    def sale(self):
        return self._sale

    @sale.setter
    def sale(self, value):
        if isinstance(value, int):
            self._sale = value
        else:
            raise ValueError('sale must be a int')

    @property
    def auction(self):
        return self._auction

    @auction.setter
    def auction(self, value):
        if isinstance(value, int):
            self._auction = value
        else:
            raise ValueError('auction must be a int')

    @property
    def request(self):
        return self._request

    @request.setter
    def request(self, value):
        if isinstance(value, int):
            self._request = value
        else:
            raise ValueError('request must be a int')

    @property
    def bid(self):
        return self._bid

    @bid.setter
    def bid(self, value):
        if isinstance(value, int):
            self._bid = value
        else:
            raise ValueError('bid must be a int')

    @property
    def hold(self):
        return self._hold

    @hold.setter
    def hold(self, value):
        if isinstance(value, int):
            self._auction = value
        else:
            raise ValueError('hold must be a int')

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self,value):
        if isinstance(value,int):
            self._source = value
        else:
            raise ValueError('source must be a int')

    @property
    def dest(self):
        return self._dest

    @dest.setter
    def dest(self,value):
        if isinstance(value,int):
            self._dest= value
        else:
            raise ValueError('dest must be int')

    @property
    def show_NFTS(self):
        return self._show_NFTs

    @show_NFTS.setter
    def show_NFTS(self,value):
        if isinstance(value,int):
            self._show_NFTS = value
        else:
            raise ValueError('show_NFTS must be int')

class Given:
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
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if isinstance(value, str):
            self._user = value
        else:
            raise ValueError('user must be a str')

    @property
    def sale(self):
        return self._sale

    @sale.setter
    def sale(self, value):
        if isinstance(value, int):
            self._sale = value
        else:
            raise ValueError('sale must be a int')

    @property
    def auction(self):
        return self._auction

    @auction.setter
    def auction(self, value):
        if isinstance(value, int):
            self._auction = value
        else:
            raise ValueError('auction must be a int')

    @property
    def request(self):
        return self._request

    @request.setter
    def request(self, value):
        if isinstance(value, int):
            self._request = value
        else:
            raise ValueError('request must be a int')

    @property
    def bid(self):
        return self._bid

    @bid.setter
    def bid(self, value):
        if isinstance(value, int):
            self._bid = value
        else:
            raise ValueError('bid must be a int')

    @property
    def hold(self):
        return self._hold

    @hold.setter
    def hold(self, value):
        if isinstance(value, int):
            self._auction = value
        else:
            raise ValueError('hold must be a int')

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        if isinstance(value, int):
            self._source = value
        else:
            raise ValueError('source must be a int')

    @property
    def dest(self):
        return self._dest

    @dest.setter
    def dest(self, value):
        if isinstance(value, int):
            self._dest = value
        else:
            raise ValueError('dest must be int')

    @property
    def show_NFTS(self):
        return self._show_NFTs

    @show_NFTS.setter
    def show_NFTS(self, value):
        if isinstance(value, int):
            self._show_NFTS = value
        else:
            raise ValueError('show_NFTS must be int')

class LeadersModel:
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
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        if isinstance(value, str):
            self._tag = value
        else:
            raise ValueError('tag must be a str')

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if isinstance(value, str):
            self._tags = value
        else:
            raise ValueError('tags must be a str')

    @property
    def all_tag(self):
        return self._all_tag

    @all_tag.setter
    def all_tag(self, value):
        if isinstance(value, str):
            self._all_tag = value
        else:
            raise ValueError('all_tag must be a str')

    @property
    def all_tags(self):
        return self._all_tags

    @all_tags.setter
    def all_tags(self, value):
        if isinstance(value, str):
            self._all_tags = value
        else:
            raise ValueError('all_Tag must be a str')

    @property
    def any_tags(self):
        return self._any_tags

    @any_tags.setter
    def any_tags(self, value):
        if isinstance(value, str):
            self._any_tags = value
        else:
            raise ValueError('any_Tag must be a str')

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        if isinstance(value, int):
            self._count = value
        else:
            raise ValueError('count must be int')

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        if isinstance(value, int):
            self._page = value
        else:
            raise ValueError('page must be int')
