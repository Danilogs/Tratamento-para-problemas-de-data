class Diasinvalidos(Exception):
    def __init__(self,valor):
        self.valor = valor
    def __str__(self):
        return repr(self.valor)

class Anoinvalido(Exception):
    def __init__(self,valor):
        self.valor = valor
    def __str__(self):
        return repr(self.valor)

class AnoBissexto(Exception):
    def __init__(self,valor):
        self.valor = valor
    def __str__(self):
        return repr(self.valor)

class Ano_NBissexto(Exception):
    def __init__(self,valor):
        self.valor = valor
    def __str__(self):
        return repr(self.valor)

class Mesinvalido(Exception):
    def __init__(self,valor):
        self.valor = valor
    def __str__(self):
        return repr(self.valor)


def consulta(data):
    try:
        #A funcao pega a data com "/" e separa em dia,mes e ano
        data=data.split("/")
        dia=int(data[0])
        mes=int(data[1])
        ano=int(data[2])
        #Cria uma lista com todos os numeros de meses possiveis
        mes0=range(1,13)
        #Cria uma lista com todos os dias de um mes com 30 dias
        mes1=range(1,31)
        #Cria uma lista com todos os dias de um mes com 31 dias
        mes2=range(1,32)
        #Cria uma lista com todos os dias de Fevereiro de um ano NAO bissexto
        february1=range(1,29)
        #Cria uma lista com rodos os dias de Fevereiro de um ano bissexto
        february2=range(1,30)
        T=True
    except:
        return False
    if T==True:
        try:
            if len(str(ano))==2:
                if mes in mes0:
                    #Logica pra descobrir se o mes tem 31 dias ou 30 dias
                    if mes<=7 and (mes%2)!=0:
                        if dia in mes2:
                            G=True
                        else:
                            raise Diasinvalidos(dia)
                    elif mes<=7 and (mes%2)==0:
                        if mes==2:
                            #logica pra descobrir se o ano eh bissexto
                            teste1=ano%4
                            teste2=ano%100
                               
                            if teste1==0 and teste2!=0:
                                if dia in february2:
                                    G=True
                                        
                                else:
                                    raise AnoBissexto(dia)
                            else:
                                if dia in february1:
                                    G=True
                                        
                                else:
                                    raise Ano_NBissexto(dia)
                        else:
                            if dia in mes1:
                                G=True
                            else:
                                raise Diasinvalidos(dia)
                    elif mes>7 and (mes%2)!=0:
                        if dia in mes1:
                            G=True
                        else:
                            raise Diasinvalidos(dia)
                    elif mes>7 and (mes%2)==0:
                        if dia in mes2:
                            G=True
                        else:
                            raise Diasinvalidos(dia)
                else:
                    raise Mesinvalido(mes)
                            
            else:
                raise Anoinvalido(ano)

            if G==True:
                return True
            
        except Diasinvalidos as e:
            return ["dia",e.valor]
        except Anoinvalido as f:
            return ["ano",f.valor]
        except AnoBissexto as h:
            return ["bissexto",h.valor]
        except Ano_NBissexto as p:
            return ["n_bissexto",p.valor]
        except Mesinvalido as o:
            return ["mes",o.valor]
        
