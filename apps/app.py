from libs.params.func_params import FuncParams
from libs.params.params import IParams


def process(params: IParams):
    print(f"params: {params}")
    print(f"params.is_reload: {params.is_reload}")

    dict = params.to_dict()
    print(f"dict: {dict}")
    print(f"dict['is_reload']: {dict['is_reload']}")


if __name__ == '__main__':
    params = FuncParams.create(is_reload=True)
    process(params)

