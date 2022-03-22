while True:
    try:
        vstup = int(input())
        file = open("file neexistuje", "r")
        a = 3 + vstup
    except ValueError:
        print("Zadejte číslo, dik dik")

    except Exception as e:
        print("Nastala chyba, bohužel")
        print(e)
    else:
        print("Vše v pořádku :D")

    finally:
        file.close()