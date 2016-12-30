import uuid

# Funcao que gera um char "aleatório"
# Gera um sha1 hash usando the uuid4 e o nome passado
# Acredito que seja "aleatório" o suficiente para nosso problema (?)
# https://stackoverflow.com/questions/4306420/math-question-regarding-pythons-uuid4
def generateToken(name):
    identifier = uuid.uuid4()
    return uuid.uuid5(identifier, str(name)).hex
