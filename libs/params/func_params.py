from libs.params.params import abParams


class FuncParams(abParams):

    def __init__(self, is_reload: bool = False):
        self.is_reload = is_reload

    def to_dict(self) -> dict:
        return {
            'is_reload': self.is_reload,
        }

    @classmethod
    def create(cls, is_reload: bool = False):
        return cls(
            is_reload=is_reload
        )
