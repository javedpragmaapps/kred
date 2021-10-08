# from helpers import *
import json

# Python Mint class to illustrate the Modules


class MintModels:
    def __init__(self):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError('name must be a int')

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
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if isinstance(value, str):
            self._type = value
        else:
            raise ValueError('type must be a str')

    @property
    def layout(self):
        return self._layout

    @layout.setter
    def layout(self, value):
        if isinstance(value, str):
            self._layout = value
        else:
            raise ValueError('layout must be a str')

    @property
    def front(self):
        return self._front

    @front.setter
    def front(self, value):
        if isinstance(value, str):
            self._layout = value
        else:
            raise ValueError('front must be a str')

    @property
    def back(self):
        return self._back

    @back.setter
    def back(self, value):
        if isinstance(value, str):
            self._back = value
        else:
            raise ValueError('back must be a str')



    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if isinstance(value, str):
            self._color = value
        else:
            raise ValueError('color must be a str')

    @property
    def pattern(self):
        return self._pattern


    @pattern.setter
    def pattern(self, value):
        if isinstance(value, str):
            self._pattern = value
        else:
            raise ValueError('pattern must be a str')

    @property
    def pattern_color(self):
        return self._pattern_color

    @pattern_color.setter
    def pattern_color(self, value):
        if isinstance(value, str):
            self._pattern_color = value
        else:
            raise ValueError('pattern_color must be a str')

    @property
    def text_color(self):
        return self._text_color

    @text_color.setter
    def text_color(self, value):
        if isinstance(value, str):
            self._text_color = value
        else:
            raise ValueError('text_color must be a str')

    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, value):
        if isinstance(value, str):
            self._payload= value
        else:
            raise ValueError('payload must be a str')

    @property
    def wrapper(self):
        return self._wrapper

    @payload.setter
    def wrapper(self, value):
        if isinstance(value, str):
            self._wrapper = value
        else:
            raise ValueError('wrapper must be a str')

    @property
    def mesh(self):
        return self._mesh

    @mesh.setter
    def mesh(self, value):
        if isinstance(value, bool):
            self._mesh = value
        else:
            raise ValueError('mesh must be a bool')

    @property
    def nsfw(self):
        return self._nsfw

    @nsfw.setter
    def nsfw(self, value):
        if isinstance(value, bool):
            self._nsfw= value
        else:
            raise ValueError('nsfw must be a bool')

class DaftModel:

    def __init__(self):
        pass

    @property
    def draft(self):
        return self._draft

    @draft.setter
    def draft(self, value):
        if isinstance(value, int):
            self._draft = value
        else:
            raise ValueError('draft must be a int')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError('name must be a int')

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
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if isinstance(value, str):
            self._type = value
        else:
            raise ValueError('type must be a str')

    @property
    def layout(self):
        return self._layout

    @layout.setter
    def layout(self, value):
        if isinstance(value, str):
            self._layout = value
        else:
            raise ValueError('layout must be a str')

    @property
    def front(self):
        return self._front

    @front.setter
    def front(self, value):
        if isinstance(value, str):
            self._layout = value
        else:
            raise ValueError('front must be a str')

    @property
    def back(self):
        return self._back

    @back.setter
    def back(self, value):
        if isinstance(value, str):
            self._back = value
        else:
            raise ValueError('back must be a str')

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if isinstance(value, str):
            self._color = value
        else:
            raise ValueError('color must be a str')

    @property
    def pattern(self):
        return self._pattern

    @pattern.setter
    def pattern(self, value):
        if isinstance(value, str):
            self._pattern = value
        else:
            raise ValueError('pattern must be a str')

    @property
    def pattern_color(self):
        return self._pattern_color

    @pattern_color.setter
    def pattern_color(self, value):
        if isinstance(value, str):
            self._pattern_color = value
        else:
            raise ValueError('pattern_color must be a str')

    @property
    def text_color(self):
        return self._text_color

    @text_color.setter
    def text_color(self, value):
        if isinstance(value, str):
            self._text_color = value
        else:
            raise ValueError('text_color must be a str')

    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, value):
        if isinstance(value, str):
            self._payload = value
        else:
            raise ValueError('payload must be a str')

    @property
    def wrapper(self):
        return self._wrapper

    @payload.setter
    def wrapper(self, value):
        if isinstance(value, str):
            self._wrapper = value
        else:
            raise ValueError('wrapper must be a str')

    @property
    def mesh(self):
        return self._mesh

    @mesh.setter
    def mesh(self, value):
        if isinstance(value, bool):
            self._mesh = value
        else:
            raise ValueError('mesh must be a bool')

    @property
    def nsfw(self):
        return self._nsfw

    @nsfw.setter
    def nsfw(self, value):
        if isinstance(value, bool):
            self._nsfw = value
        else:
            raise ValueError('nsfw must be a bool')


class EditModel:

    def __init__(self):
        pass

    @property
    def batch(self):
        return self._batch

    @batch.setter
    def batch(self, value):
        if isinstance(value, int):
            self._batch = value
        else:
            raise ValueError('batch must be a int')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError('name must be a int')

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
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if isinstance(value, str):
            self._type = value
        else:
            raise ValueError('type must be a str')

    @property
    def layout(self):
        return self._layout

    @layout.setter
    def layout(self, value):
        if isinstance(value, str):
            self._layout = value
        else:
            raise ValueError('layout must be a str')

    @property
    def front(self):
        return self._front

    @front.setter
    def front(self, value):
        if isinstance(value, str):
            self._layout = value
        else:
            raise ValueError('front must be a str')

    @property
    def back(self):
        return self._back

    @back.setter
    def back(self, value):
        if isinstance(value, str):
            self._back = value
        else:
            raise ValueError('back must be a str')

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if isinstance(value, str):
            self._color = value
        else:
            raise ValueError('color must be a str')

    @property
    def pattern(self):
        return self._pattern

    @pattern.setter
    def pattern(self, value):
        if isinstance(value, str):
            self._pattern = value
        else:
            raise ValueError('pattern must be a str')

    @property
    def pattern_color(self):
        return self._pattern_color

    @pattern_color.setter
    def pattern_color(self, value):
        if isinstance(value, str):
            self._pattern_color = value
        else:
            raise ValueError('pattern_color must be a str')

    @property
    def text_color(self):
        return self._text_color

    @text_color.setter
    def text_color(self, value):
        if isinstance(value, str):
            self._text_color = value
        else:
            raise ValueError('text_color must be a str')

    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, value):
        if isinstance(value, str):
            self._payload = value
        else:
            raise ValueError('payload must be a str')

    @property
    def wrapper(self):
        return self._wrapper

    @payload.setter
    def wrapper(self, value):
        if isinstance(value, str):
            self._wrapper = value
        else:
            raise ValueError('wrapper must be a str')

    @property
    def mesh(self):
        return self._mesh

    @mesh.setter
    def mesh(self, value):
        if isinstance(value, bool):
            self._mesh = value
        else:
            raise ValueError('mesh must be a bool')

    @property
    def nsfw(self):
        return self._nsfw

    @nsfw.setter
    def nsfw(self, value):
        if isinstance(value, bool):
            self._nsfw = value
        else:
            raise ValueError('nsfw must be a bool')

class NftModel:
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

class NftsModel:
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if isinstance(value, int):
            self._user = value
        else:
            raise ValueError('user must be a int')



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
    def batch(self):
        return self._batch

    @batch.setter
    def batch(self, value):
        if isinstance(value, int):
            self._batch = value
        else:
            raise ValueError('batch must be a int')

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
    def nft(self):
        return self._nft

    @nft.setter
    def nft(self, value):
        if isinstance(value, int):
            self._nft = value
        else:
            raise ValueError('nft must be a int')

    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        if isinstance(value, str):
            self._creator = value
        else:
            raise ValueError('creator must be a str')

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        if isinstance(value, str):
            self._domain = value
        else:
            raise ValueError('domain must be a str')

    @property
    def wallet(self):
        return self._wallet

    @wallet.setter
    def wallet(self, value):
        if isinstance(value, int):
            self._wallet = value
        else:
            raise ValueError('wallet must be a int')

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        if isinstance(value, int):
            self._currency= value
        else:
            raise ValueError('currency must be a int')

    @property
    def market(self):
        return self._market

    @market.setter
    def market(self, value):
        if isinstance(value, int):
            self._market = value
        else:
            raise ValueError('market must be a int')

    @property
    def hidden(self):
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        if isinstance(value, bool):
            self._hidden = value
        else:
            raise ValueError('hidden must be a bool')

    @property
    def nsfw(self):
        return self._nsfw

    @nsfw.setter
    def nsfw(self, value):
        if isinstance(value, bool):
            self._nsfw = value
        else:
            raise ValueError('nsfw must be a bool')

    @property
    def flagged(self):
        return self._flagged

    @flagged.setter
    def flagged(self, value):
        if isinstance(value, bool):
            self._flagged = value
        else:
            raise ValueError('flagged must be a bool')

    @property
    def held(self):
        return self._held

    @held.setter
    def held(self, value):
        if isinstance(value, bool):
            self._held = value
        else:
            raise ValueError('held must be a bool')

    @property
    def showcase(self):
        return self._showcase

    @showcase.setter
    def showcase(self, value):
        if isinstance(value, bool):
            self._showcase= value
        else:
            raise ValueError('showcase must be a bool')

    @property
    def onsale(self):
        return self._onsale

    @onsale.setter
    def onsale(self, value):
        if isinstance(value, bool):
            self._onsale = value
        else:
            raise ValueError('onsale must be a bool')

    @property
    def batched(self):
        return self._batched

    @batched.setter
    def batched(self, value):
        if isinstance(value, bool):
            self._batched = value
        else:
            raise ValueError('batched must be a bool')

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
    def all_tags(self):
        return self._all_tags

    @all_tags.setter
    def all_tags(self, value):
        if isinstance(value, str):
            self._all_tags = value
        else:
            raise ValueError('all_tags must be a str')

    @property
    def any_tags(self):
        return self._any_tags

    @any_tags.setter
    def any_tags(self, value):
        if isinstance(value, str):
            self._any_tags = value
        else:
            raise ValueError('any_tags must be a str')

    @property
    def search(self):
        return self._search

    @search.setter
    def search(self, value):
        if isinstance(value, str):
            self._search = value
        else:
            raise ValueError('search must be a str')

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
            self._page= value
        else:
            raise ValueError('page must be a int')
