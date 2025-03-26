#!/usr/bin/python3

# QUESTO CODICE È STATO CREATO DA ALESSANDRO CATTI
# IL CODICE È STATO PUBBLICATO SU GITHUB A ANCHE SCOPO DIDATTICO
# È POSSIBILE RIUTILLIZZARE IL CODICE :-)

# BREVE DESCRIZIONE DELLO SCRIPT:
# script per sommare una lista di numeri interi attraverso una funzione "somma" scritta manualmente


# DICHIARAZIONE DELLA FUNZIONE:
def somma(nums, s=0):
    # ciclo che ad ogni iterazione somma ogni numero contenuto nella lista "nums"
    for num in nums:
        s += num # la somma viene aggiornata aggiungendo "num" a "s"
    return s

# ESEMPIO DI UTILIZZO:

# creo una lista che dovrà contenere i numeri da sommare
nums = list()

# variabile "flag" per il ciclo while
inserimento = True

# inizializzo la variabile che contiene un singolo numero
num = 0

# ciclo che serve a popolare la lista dei numeri "nums"
while inserimento:
    
    # uso un "try except" per gestire eventuali errori di digitazione e di input
    try:
        # l'input inserito dovrà essere un numero intero
        num = int(input("Inserisci un numero [0 per terminare]: "))
        
        # se il numero inserito corrisponde a 0, viene interrotto il ciclo
        if num == 0:
            inserimento = False
            
        # la lista viene popolata usando la funzione di "append"
        nums.append(num)
        
    # gestione delle eccezioni, tipo errori di digitazione o tipo di dato diverso da un numero
    except:
        # stampo a schermo un messaggio di errore e resetto "num" per evitare problemi
        print("ERRORE DI DIGITAZIONE, RIPROVA!")
        num = 0
        
# la funzione è pronta per essere utilizzata
s = somma(nums)
# RISULTATO FINALE
print("SOMMA NUMERI:", s)

