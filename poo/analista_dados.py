from funcionario import Funcionario
import time

class AnalistaDados(Funcionario):

    # Metodo construtor do AnalistaDados
    def __init__(self, user, curso_analise_dados) -> None:
        # Contrutor da classe mae
        super().__init__(user)
        # Atributo da classe AnalistaDados
        self.curso_analise_dados = curso_analise_dados
    
    # Metodo proprio da classe AnalistaDados
    def analisa_dados(self) -> None:
        print("Analisando os dados...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("Dados analisados!")

    # Metodo obrigatorio de se criar
    def primeiros_passos(self) -> None:
        valida = False
        while not valida:
            senha = input("Defina uma senha: ")
            valida = self.cadastrar_no_portal(senha)
        
    # Metodo proprio da classe AnalistaDados
    def estuda_modelo(self):
        print("Estudando modelo...")
        print("hum... então é assim que funciona.")