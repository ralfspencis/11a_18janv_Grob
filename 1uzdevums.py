## Izveidot Python programmu, kas nolasītu un izdrukātu visu teksta faila saturu (txt formātā). (3 punkti)
# izveidojam komandu, lai varētu nolasīt no teksta faila visus datus.
def lasit_failu(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r') as fails:
            saturs = fails.read()
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Kļūda: Fails '{faila_nosaukums}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")
# augšējas rindas paziņos par kļūdam, ja fails ir nepareizi uzrasktits, deļ kā vinu nevarētu atrast.

# izveidojam komandu, kura precizē kuru failu vēlamies nolasit, ja tāds eksistē tad nolasa.
faila_nosaukums=input("Ievadiet teksta faila nosaukumu (ar paplasinājumu .txt): ")
lasit_failu(faila_nosaukums)

