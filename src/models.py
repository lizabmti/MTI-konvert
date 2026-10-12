from abc import ABC, abstractmethod
from datetime import datetime


class Currency(ABC):
    def __init__(self,code,name,rate):
        self._code=code
        self._name=name
        self._rate=rate

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self,value):
        self._code=value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name=value

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self,value):
        self._rate=value

    @abstractmethod
    def get_info(self):
        pass

    def __eq__(self,other):
        return self._code==other._code

    def __repr__(self):
        return "Currency: "+self._code

    def __str__(self):
        return self._name


class Usd(Currency):
    def get_info(self):
        return self._name

    def __lt__(self,other):
        return self._rate<other._rate

    def __gt__(self,other):
        return self._rate>other._rate


class Session(ABC):
    def __init__(self,user):
        self._user=user
        self._time_in=datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        self._time_out=None

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self,value):
        self._user=value

    @property
    def time_in(self):
        return self._time_in

    @time_in.setter
    def time_in(self,value):
        self._time_in=value

    @property
    def time_out(self):
        return self._time_out

    @time_out.setter
    def time_out(self,value):
        self._time_out=value

    @abstractmethod
    def get_info(self):
        pass

    def close(self):
        self._time_out=datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    def __eq__(self,other):
        return self._user==other._user

    def __repr__(self):
        return "Session: "+self._user

    def __str__(self):
        return self._user


class UserSession(Session):
    def get_info(self):
        return self._user

    def __lt__(self,other):
        return self._user<other._user

    def __gt__(self,other):
        return self._user>other._user


class Mapper:
    def __init__(self):
        self.keys=[]
        self.values=[]

    def set(self,key,value):
        if key in self.keys:
            i=self.keys.index(key)
            self.values[i]=value
        else:
            self.keys.append(key)
            self.values.append(value)

    def get(self,key):
        if key in self.keys:
            i=self.keys.index(key)
            return self.values[i]
        else:
            return None

    def __eq__(self,other):
        return self.keys==other.keys

    def __repr__(self):
        return "Mapper"

    def __str__(self):
        return "Mapper"
