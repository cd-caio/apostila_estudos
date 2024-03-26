from funcionario import Funcionario

class Diretor(Funcionario):

    def __init__(self, user) -> None:
        super().__init__(user)

    # Metodo obrigatorio de se criar
    def primeiros_passos(self) -> None:
        valida = False
        while not valida:
            senha = input("Defina uma senha: ")
            valida = self.cadastrar_no_portal(senha)

    # Metodo privado (contem __ no comeco) isso significa que preferencialmente, este metodo so deve ser usado dentro da classe Diretor
    # o __ apenas dificulta o acesso mas NAO bloqueia totalmente de usar fora da classe.
    def __demite_pessoas(self) -> None:
        print("Posso demitir quem eu quiser, muhahaha")
        print("JAMES, demita alguém.")
    
    # Metodo privado (contem __ no comeco) isso significa que preferencialmente, este metodo so deve ser usado dentro da classe Diretor
    # o __ apenas dificulta o acesso mas NAO bloqueia totalmente de usar fora da classe.
    def __contrata_pessoas(self) -> None:
        print("Vou falar com o financeiro.")

    # Metodo proprio da classe Diretor
    def gere_pessoas(self) -> None:
        acao = input("O que quero fazer?")
        if acao.lower() == "demitir":
            self.__demite_pessoas()
        elif acao.lower() == "contratar":
            self.__contrata_pessoas()
        else: 
            print("Você só pode demitir e contratar")


