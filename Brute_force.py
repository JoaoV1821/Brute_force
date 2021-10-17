from string import ascii_uppercase,  digits

class Brute_force:
    def __init__(self, senha):
        self.__tentativas = self.__quebra_senha(str(senha).upper())
    

    @staticmethod
    def __quebra_senha(senha):
        senha = senha.replace('', ' ').split()
        senha_quebrada = []
        
        caracteres = list(digits) + list(ascii_uppercase)

        tentativas = 0
        
        for c in range(0, len(senha)+1):
          for i in range(0, len(caracteres)):
            try:
                if caracteres[i] == senha[c]:
                  senha_quebrada.append(caracteres[i])
                  tentativas += 1
            except IndexError:
              break
  
        return tentativas


    @property
    def tentativas(self):
        return self.__tentativas
