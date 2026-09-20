from abc import ABC, abstractmethod


class IParams:
    pass

class abParams(IParams, ABC):

    @abstractmethod
    def to_dict(self) -> dict: ...

    @classmethod
    def create(cls, *args, **kwargs):
        return cls(*args, **kwargs)