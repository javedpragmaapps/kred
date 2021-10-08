import json

# Python Mint class to illustrate the Modules


class BundleModels:

    def __init__(self):
        pass
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if isinstance(value,str):
            self._name = value
        else:
            raise ValueError('name must be a str')

    @property
    def max_subscribers(self):
        return self._max_subscribers

    @max_subscribers.setter
    def max_subscribers(self,value):
        if isinstance(value,int):
            self._max_subscribers=value
        else:
            raise  ValueError('max subscribers must be a int')

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self,value):
        if isinstance(value,str):
            self._channel=value
        else:
            raise  ValueError('channel must be str')


class ListModels:
    def __init__(self):
        pass

    @property
    def line(self):
        return self._line
    @line.setter
    def line(self,value):
        if isinstance(value,int):
            self._line=value
        else:
            raise ValueError('line should be a int')

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self,value):
        if isinstance(value,str):
            self._status=value
        else:
            raise  ValueError('status should be a str')

    @property
    def batches(self):
        return self._batches

    @batches.setter
    def batches(self,value):
        if isinstance(value,str):
            self._batches=value
        else:
            raise ValueError('batches should be a str')

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self,value):
        if isinstance(value,str):
            self._method=value
        else:
            raise  ValueError('methods should be a str')

    @property
    def odds(self):
        return self._odds

    @odds.setter
    def odds(self,value):
        if isinstance(value,int):
            self._odd=value
        else:
            raise  ValueError('odds should be a int')










