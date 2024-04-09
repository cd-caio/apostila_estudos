from abc import ABC, abstractmethod

# Classe funcionario que herda a classe ABC
class Funcionario(ABC):
    def __init__(self, user:str) -> None:
        # Senha padrão, deve ser alterada depois. Todos esses atributos podem ser acessados por qualquer classe que herde a classe Funcionario.
        self.senha = 1234
        self.user = user

    # Metodo padrão que todos devem herdar
    def cadastrar_no_portal(self, senha:str) -> bool:
        valido = False
        if senha.isalpha() or senha.isdigit():
            print("A senha deve conter letras e números.")
        else:
            print("Senha criada com sucesso.")
            self.senha = senha
            valido = True

        return valido

    # Metodo abstrato que toda classe que herdar Funcionario devera criar.
    @abstractmethod
    def primeiros_passos(self) -> None:
        pass
