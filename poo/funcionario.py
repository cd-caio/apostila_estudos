from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, user:str) -> None:
        # Senha padrão, deve ser alterada depois
        self.senha = 1234
        self.user = user

    def cadastrar_no_portal(self, senha:str) -> bool:
        valido = False
        if senha.isalpha() or senha.isdigit():
            print("A senha deve conter letras e números.")
        else:
            print("Senha criada com sucesso.")
            self.senha = senha
            valido = True

        return valido

    @abstractmethod
    def primeiros_passos(self) -> None:
        pass
