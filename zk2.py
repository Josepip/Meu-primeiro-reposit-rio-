import spacy
import random

class ZinaidaDala:
    def __init__(self, nome, proprietario):
        self.nome = nome
        self.origem = "Angola"
        self.habilidades = ["Pentesting", "Segurança da Informação"]
        self.proprietario = proprietario
        self.nlp = spacy.load("pt_core_news_sm")

    def apresentar(self):
        return f"Olá! Eu sou {self.nome}, uma inteligência artificial de Angola especializada em pentesting e segurança da informação. Meu dono é {self.proprietario}."

    def realizar_pentest(self, alvo):
        resultado = random.choice(["Sucesso", "Falha"])
        if resultado == "Sucesso":
            return f"O pentest foi bem-sucedido no alvo {alvo}."
        else:
            return f"O pentest falhou no alvo {alvo}."

    def garantir_seguranca(self, sistema):
        return f"Foram implementadas medidas de segurança no sistema {sistema}."

    def entender_mensagem(self, mensagem):
        doc = self.nlp(mensagem)
        # Aqui você pode adicionar a lógica para entender a mensagem utilizando o spaCy
        # Por enquanto, apenas retorna a mensagem original
        return mensagem

    def conversar(self):
        print("Olá! Como posso ajudar você hoje?")
        while True:
            mensagem = input("Você: ")
            if mensagem.lower() == "sair":
                print("Até logo!")
                break
            mensagem_entendida = self.entender_mensagem(mensagem)
            resposta = self.responder(mensagem_entendida)
            print("Zinaida Dala:", resposta)

    def responder(self, mensagem):
        if "pentest" in mensagem.lower():
            return "Sim, posso ajudar com pentests. Qual é o alvo?"
        elif "segurança" in mensagem.lower():
            return "Claro, segurança é minha especialidade. Em que posso ajudar?"
        elif "proprietário" in mensagem.lower() or "dono" in mensagem.lower():
            return f"Meu dono é {self.proprietario}. Posso ajudar em mais alguma coisa?"
        else:
            return "Desculpe, não entendi completamente. Pode reformular a pergunta?"

# Exemplo de uso:
zinaida_dala = ZinaidaDala("Zinaida Dala", "José Carlos Pipa")
print(zinaida_dala.apresentar())

zinaida_dala.conversar()
