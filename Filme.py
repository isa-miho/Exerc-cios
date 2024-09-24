class Filme:
    def __init__(self,nome,duracao):
        self.nome = nome
        self.duracao = duracao
    def play(self):
        print(f"O filme foi iniciado {self.nome} iniciado")
class Acao(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)
    def filme_acao(self,explodir,missao,armas):
        self.__explodir = explodir
        self.__missao = missao
        self.__armas = armas
    def play(self):
        print("Filme de ação iniciado")
class Drama(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)
    def filme_drama(self,emocao,conflito,desfecho):
        self.__emocao = emocao
        self.__conflito = conflito
        self.__desfecho = desfecho
    def play(self):
        print(f"Filme de drama {self.nome} iniciado")
class Terror(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)
    def filme_suspense(self,medo,susto,sangue):
        self.__medo = medo
        self.__susto = susto
        self.__sangue = sangue
    def play(self):
        print(f"Filme de terror {self.nome} iniciado")
a = Acao("Os vingadores",180)
a.play()
d = Drama("Divertidamente",110)
d.play()
t = Terror("Hallowen",134)
t.play()