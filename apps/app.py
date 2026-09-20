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

if __name__ == '__main__':
    params = FuncParams.create(is_reload=True)
    print(f"params: {params}")
    print(f"params.is_reload: {params.is_reload}")

    dict = params.to_dict()
    print(f"dict: {dict}")
    print(f"dict['is_reload']: {dict['is_reload']}")

