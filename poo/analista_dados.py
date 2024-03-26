from funcionario import Funcionario
import time

class AnalistaDados(Funcionario):
    def __init__(self, user, curso_analise_dados) -> None:
        super().__init__(user)
        self.curso_analise_dados = curso_analise_dados
    
    def analisa_dados(self) -> None:
        print("Analisando os dados...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("Dados analisados!")

    def primeiros_passos(self) -> None:
        valida = False
        while not valida:
            senha = input("Defina uma senha: ")
            valida = self.cadastrar_no_portal(senha)
        
    def estuda_modelo(self):
        print("Estudando modelo...")
        print("hum... então é assim que funciona.")