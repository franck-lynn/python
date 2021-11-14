# https://docs.python.org/3/library/typing.html

# 类型声明使用前需要导入进来
from typing import List


def greeting(name: str) -> str:
    return 'hello ' + name


#  类型别名
Vector = List[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# typechecks; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
print(new_vector)

# 类型别名
from typing import Dict, Tuple
from collections.abc import Sequence

ConnectionOptions = Dict[str, str]
Address = Tuple[str, str]
Server = Tuple[Address, ConnectionOptions]

def broadcast_message(message: str, servers: Server) -> None:
    print(message)






