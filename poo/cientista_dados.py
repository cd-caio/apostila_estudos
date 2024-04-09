import time
from analista_dados import AnalistaDados

# A classe se chama CientistaDados e esta herdando a classe AnalistaDados
class CientistaDados(AnalistaDados):
    
    def __init__(self, user, curso_machine_learning, curso_analise_dados) -> None:
        # Chamando o construtor da classe mae (AnalistaDados)
        super().__init__(user, curso_analise_dados)
        # Atributo de uma classe
        self.curso_machine_learning = curso_machine_learning

    # Metodo proprio da classe cientista dados
    def treina_modelo(self):
        print("Treinando modelo...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("Vixi, ficou ruim... Vou mudar a seed...")
        time.sleep(2)
        print("Agora sim, modelo treinado!")

    # Metodo herdado e sobrescrevido (Polimorfismo)
    def estuda_modelo(self):
        print("Estudando modelo...")
        print("Hum... não entendi nada, vou perguntar para o analista.")
