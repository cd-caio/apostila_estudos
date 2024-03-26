from funcionario import Funcionario

class Diretor(Funcionario):

    def __init__(self, user) -> None:
        super().__init__(user)

