import time
from analista_dados import AnalistaDados

class CientistaDados(AnalistaDados):
    def __init__(self, user, curso_machine_learning, curso_analise_dados) -> None:
        super().__init__(user, curso_analise_dados)
        self.curso_machine_learning = curso_machine_learning

    def treina_modelo(self):
        print("Treinando modelo...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("Vixi, ficou ruim... Vou mudar a seed...")
        time.sleep(2)
        print("Agora sim, modelo treinado!")

    def estuda_modelo(self):
        print("Estudando modelo...")
        print("Hum... não entendi nada, vou perguntar para o analista.")
