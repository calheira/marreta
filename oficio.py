class Oficio(object):
    """Gerencia Oficio"""
    def __init__(self, processo):
        self.processo = processo
        print(f"... Iniciando criação\n... \nProcesso {self.processo}")

    def assunto(self, texto):
        self.texto = texto.upper()
        print(f"Assunto: {self.texto}")

    def corpo(self, texto):
        pass

    def assinatura(self, texto):
        pass
