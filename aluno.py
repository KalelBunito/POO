class Aluno:
    def __init__(self, nome, idade, periodo):
        self.nome = nome
        self.idade = idade
        self.periodo = periodo
    def exibir_detalhes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Período: {self.periodo}")