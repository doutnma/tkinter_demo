while True:
    try:
        vstup = int(input())
        file = open("file neexistuje, sad", "r")
        a = 3 + vstup
    except ValueError:
        print("Zadej číslo, dik dik")

    except Exception as e:
        print("Kámo, máš tam chybu")
        print(e)
    else:
        print("Pohoda :D")
    """
    finally:
        file.close()
    """