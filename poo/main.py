from analista_dados import AnalistaDados
from cientista_dados import CientistaDados

user = input("Qual o seu nome? ")
analista_dados: AnalistaDados = AnalistaDados(user=user, curso_analise_dados="Alura")
analista_dados.primeiros_passos()
analista_dados.estuda_modelo()
analista_dados.analisa_dados()

# user = input("Qual o seu nome? ")
# cientista_dados: CientistaDados = CientistaDados(user=user, curso_machine_learning="Udemy", curso_analise_dados="Alura")
# cientista_dados.primeiros_passos()
# cientista_dados.analisa_dados()
# cientista_dados.estuda_modelo()
# cientista_dados.treina_modelo()

