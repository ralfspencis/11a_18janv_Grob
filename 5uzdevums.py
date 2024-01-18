##5.	Izveidot Python programmu, kas ļauj lietotājam ievadīt savu vārdu terminālī. Ievadīto vārdu pēc tam ierakstīt 
# teksta failā (piemēram, "lietotajs.txt"). Programmai jābūt spējīgai apstrādāt kļūdas, piemēram, faila nepieejamību vai rakstīšanas
#  problēmas. Pēc ierakstīšanas izvadīt paziņojumu
#  par veiksmīgu darbību vai kļūdu gadījumā attiecīgu kļūdas ziņojumu. (8 punkti)

def kontroldarbs(vards, faila_nosaukums='lietotajs.txt'):
    try:
        with open(faila_nosaukums, 'w') as fails:
            fails.write(vards)
        print(f"Vārds '{vards}' veiksmīgi ierakstīts failā '{faila_nosaukums}'.")
    except PermissionError:
        print(f"Kļūda: Nav atļaujas rakstīt failā '{faila_nosaukums}'.")
    except FileNotFoundError:
        print(f"Kļūda: Fails '{faila_nosaukums}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

# Komanda, kura prasīs, kādu vārdu ierakstīt.
lietotaja_vards = input("Ievadiet savu vārdu: ")

# Ieraksta augša minēto vārdu failā.
kontroldarbs(lietotaja_vards)
