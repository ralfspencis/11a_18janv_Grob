##	Izveidot Python programmu, kas nolasītu un izdrukātu tikai otrās kolonnas datus no CSV faila. (3 punkti)
import csv

def lasit_otro_kolonnu(csv_faila_nosaukums):
    try:
        with open(csv_faila_nosaukums, 'r', newline='') as csv_fails:
            csv_lasitajs = csv.reader(csv_fails)
            
            next(csv_lasitajs, None)
            
            print("Otrās kolonnas dati:")
            for rinda in csv_lasitajs:
                if len(rinda) > 1:
                    dati = rinda[1]
                    print(dati)
    except FileNotFoundError:
        print(f"Kļūda: Fails '{csv_faila_nosaukums}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

# Nolasām CSV faila nosaukumu,pēc kā to izprintēs
csv_faila_nosaukums = input("Ievadiet CSV faila nosaukumu: ")
lasit_otro_kolonnu(csv_faila_nosaukums)
