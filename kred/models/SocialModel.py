class PostModel:


    def __init__(self):
        pass

    @property
    def nft(self):
        return self._nft

    @nft.setter
    def nft(self,value):
        if isinstance(value,int):
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
        if isinstance(value,int):
            self._sequence = value
        else:
            raise ValueError('sequence must be a int')

    @property
    def grab(self):
        return self._grab

    @grab.setter
    def grab(self, value):
        if isinstance(value, str):
            self._grab = value
        else:
            raise ValueError('grab must be a str')

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if isinstance(value, str):
            self._text = value
        else:
            raise ValueError('text must be a str')

class  ReplyAndCommentModel:


    def __init__(self):
        pass

    @property
    def nft(self):
        return self._nft

    @nft.setter
    def nft(self,value):
        if isinstance(value,int):
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
            raise ValueError('name must be a str')

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        if isinstance(value,int):
            self._sequence = value
        else:
            raise ValueError('sequence must be a int')

    @property
    def grab(self):
        return self._grab

    @grab.setter
    def grab(self, value):
        if isinstance(value, str):
            self._grab = value
        else:
            raise ValueError('grab must be a str')

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        if isinstance(value, str):
            self._message = value
        else:
            raise ValueError('message must be a str')

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if isinstance(value, str):
            self._text = value
        else:
            raise ValueError('text must be a str')

class  RemoveModel:


    def __init__(self):
        pass

    @property
    def nft(self):
        return self._nft

    @nft.setter
    def nft(self,value):
        if isinstance(value,int):
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
            raise ValueError('name must be a str')

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        if isinstance(value,int):
            self._sequence = value
        else:
            raise ValueError('sequence must be a int')

    @property
    def grab(self):
        return self._grab

    @grab.setter
    def grab(self, value):
        if isinstance(value, str):
            self._grab = value
        else:
            raise ValueError('grab must be a str')

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        if isinstance(value, str):
            self._message = value
        else:
            raise ValueError('message must be a str')

class Messages:
    class RemoveModel:

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
                raise ValueError('name must be a str')

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
        def count(self):
            return self._count

        @count.setter
        def count(self,value):
            if isinstance(value,int):
                self._count=value
            else:
                raise ValueError('count must be int')

        @property
        def page(self):
            return self._page

        @page.setter
        def page(self,value):
            if isinstance(value,int):
                self._page=value
            else:
                raise  ValueError('page must be int')

class LikeAndUnlike:
    def __init__(self):
        pass

    @property
    def nft(self):
        return self._nft

    @nft.setter
    def nft(self,value):
        if isinstance(value,int):
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
            raise ValueError('name must be a str')

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        if isinstance(value,int):
            self._sequence = value
        else:
            raise ValueError('sequence must be a int')

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        if isinstance(value, str):
            self._message = value
        else:
            raise ValueError('message must be a str')

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if isinstance(value, int):
            self._text = value
        else:
            raise ValueError('text must be a str')


class BanAndUnBan:
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
            raise ValueError('nft must be a int')

    @property
    def nft(self):
        return self._nft

    @nft.setter
    def nft(self,value):
        if isinstance(value,int):
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
            raise ValueError('name must be a str')

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        if isinstance(value,int):
            self._sequence = value
        else:
            raise ValueError('sequence must be a int')

    @property
    def grab(self):
        return self._grab

    @grab.setter
    def grab(self, value):
        if isinstance(value, str):
            self._grab = value
        else:
            raise ValueError('grab must be a str')

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if isinstance(value, int):
            self._text = value
        else:
            raise ValueError('text must be a str')








