#Comienza con una semilla

semilla = "a"
generaciones = 9

print semilla

def lsystem(generaciones, semilla):
        for x in range(generaciones):
                #Para imprimir semilla previa
                semilla_pre = semilla
                #Convierte la semilla a lista
                unigram = []
                for y in semilla:
                        unigram.append(y)

                #Aplicacion de reglas A->AB, B->A
                for i in range(len(unigram)):
                        if unigram[i] == 'a':
                                unigram[i] = 'ab'
                        if unigram[i] == 'b':
                                unigram[i] = 'a'

                #Convertir lista a str
                semilla = "".join(unigram)
                print semilla_pre + " -> " + semilla

lsystem(generaciones, semilla)
