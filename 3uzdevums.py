##	Izveidot Python programmu, kas nolasītu un izdrukātu trešās teksta faila rindas saturu. (3 punkti)
def lasam_rindu(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r') as fails:
            rindas = fails.readlines()
            
            if len(rindas) >= 3:
                tresa_rinda = rindas[2]
                print("Trešās rindas saturs:")
                print(tresa_rinda)
            else:
                print("Kļūda: Failā ir mazāk par trim rindām.")
    except FileNotFoundError:
        print(f"Kļūda: Fails '{faila_nosaukums}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

# Nolasam faila nosakumu, ja tads eksistē, tad to izprintē
faila_nosaukums = input("Ievadiet teksta faila nosaukumu: ")
lasam_rindu(faila_nosaukums)
