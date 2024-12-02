import csv
import os
import sys

def make(fInput = "elenco.csv", fOutput = "elenco_sistemato.csv", c = ','):
    try:
        reader = csv.reader(open(os.path.join(sys.path[0], fInput), 'r'), delimiter = c)
        writer = csv.writer(open(os.path.join(sys.path[0], fOutput), 'w'), delimiter=',', lineterminator='\n')
    except FileNotFoundError as e:
        print(f"Il file: {e.filename} non esiste, sei sicuro in nome sia corretto?")
        return 1

    rows = []
    for row in reader:
        if len(row) < 2: return 2
        rows.append([f"{row[0]} {row[1]}",''.join([row[2], row[3]])])

    rows[0] = "COGNOME NOME,Classe"
    writer.writerows(rows)
    return fOutput

#inizializzazione
print("""Benvenuto in questo programma per adattare l'elenco degli studenti fornito dalla segreteria agli standard del sito per le assemblee d'istituto, procediamo:
per prima cosa assicurati che il file Excel sia nel formato:

COGNOME | NOME  | ANNO | SEZIONE
--------------------------------
Rossi   | Mario | 1    | CS

successivamente apri excel e vai su file --> esporta --> cambia tipo di file: CSV e rinomina il file "elenco.csv" infine copialo nella stessa cartella di questo programma.

Quando hai fatto premi INVIO""")
input()

status = 0
try: 
    while str(status).isnumeric():
        status = make()
        
        if status == 1: status = make(name = input("Se hai creato il file ti chiedo di scrivere qui in nome corretto e premere INVIO: "))
        elif status == 2: status = make(c = input("C'è un problema con il file, prova ad aprire il file che hai appena creato con blocco note e vedere al suo interno quale carattere divide i vari nomi, in seguito digitalo qui e premi INVIO: "))

    #fine
    print(f"""
    Il tuo file: '{status}' è pronto per essere caricato sul sito delle assemblee!!!


    ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
    Credits: Alberto Zarpellon
    Codice sorgente: https://github.com/Albe-05/Student-list-adapter""")
    input()
except Exception:
    print("Più di qualcosa è andato storto, riavvia il programma e presta attenzione alle indicazioni, altrimenti prova a contattarmi: https://github.com/Albe-05/Student-list-adapter")
    input()    
