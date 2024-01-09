def ChoixNonDisponible():
    Choix = input(
        "7777. Menu principal \n"
        "9999. Quitter \n"
    )
    if Choix == "7777":
        MenuPrincipal()
    else:
        print("Bye \n")



def MenuPrincipal():
    MenuOption = input(
        "Bienvenue sur SJITranslate \n"
        "En quelle langue est votre texte ? \n"
        "1. Français-fr \n"
        "2. Anglais-en \n"
        "3. Espagnol-spa \n"
        "4. Allemand-de \n"
        "5. Mandarin-zh \n"
         )
    if MenuOption == "1":
        print("En quelle langue souhaitez-vous le traduire \n")
        LangueOption = input(
        "1. Anglais- en \n"
        "2. Espagnol- spa \n"
        "3. Allemand- de \n"
        "4. Mandarin- zh \n"
         )
        if LangueOption == "1" :
            LangueOption="en"
        elif LangueOption == "2" :
            LangueOption="spa"
        elif LangueOption == "3" :
            LangueOption="de"
        elif LangueOption == "4" :
            LangueOption="zh"
        else:
            print(" La langue choisie ne figure pas dans notre serveur")
        print("Entrez le texte à traduire \n")
        Texte = input(" ")
        trad = Translator(from_lang="fr", to_lang=LangueOption)
        Texte = trad.translate(Texte)
        print(Texte)

    elif MenuOption == "2":
        print("En quelle langue souhaitez-vous le traduire \n")
        LangueOption = input(
            "1. Français- fr \n"
            "2. Espagnol- spa \n"
            "3. Allemand- de \n"
            "4. Mandarin- zh \n"
        )
        if LangueOption == "1":
            LangueOption = "fr"
        elif LangueOption == "2":
            LangueOption = "spa"
        elif LangueOption == "3":
            LangueOption = "de"
        elif LangueOption == "4":
            LangueOption = "zh"
        else:
            print(" La langue choisie ne figure pas dans notre serveur")
        print("Entrez le texte à traduire \n")
        Texte = input(" ")
        trad = Translator(from_lang="en", to_lang=LangueOption)
        Texte = trad.translate(Texte)
        print(Texte)

    elif MenuOption == "3":
        print("En quelle langue souhaitez-vous le traduire \n")
        LangueOption = input(
            "1. Français- fr \n"
            "2. Anglais- en \n"
            "3. Allemand- de \n"
            "4. Mandarin- zh \n"
        )
        if LangueOption == "1":
            LangueOption = "fr"
        elif LangueOption == "2":
            LangueOption = "en"
        elif LangueOption == "3":
            LangueOption = "de"
        elif LangueOption == "4":
            LangueOption = "zh"
        else:
            print(" La langue choisie ne figure pas dans notre serveur")
        print("Entrez le texte à traduire \n")
        Texte = input(" ")
        trad = Translator(from_lang="spa", to_lang=LangueOption)
        Texte = trad.translate(Texte)
        print(Texte)

    elif MenuOption == "4":
        print("En quelle langue souhaitez-vous le traduire \n")
        LangueOption = input(
            "1. Français- fr \n"
            "2. Anglais- en \n"
            "3. Espagnol- spa \n"
            "4. Mandarin- zh \n"
        )
        if LangueOption == "1":
            LangueOption = "fr"
        elif LangueOption == "2":
            LangueOption = "en"
        elif LangueOption == "3":
            LangueOption = "spa"
        elif LangueOption == "4":
            LangueOption = "zh"
        else:
            print(" La langue choisie ne figure pas dans notre serveur")
        print("Entrez le texte à traduire \n")
        Texte = input(" ")
        trad = Translator(from_lang="de", to_lang=LangueOption)
        Texte = trad.translate(Texte)
        print(Texte)

    elif MenuOption == "5":
        print("En quelle langue souhaitez-vous le traduire \n")
        LangueOption = input(
            "1. Français- fr \n"
            "2. Anglais- en \n"
            "3. Espagnol- spa \n"
            "4. Allemand- de \n"
        )
        if LangueOption == "1":
            LangueOption = "fr"
        elif LangueOption == "2":
            LangueOption = "en"
        elif LangueOption == "3":
            LangueOption = "spa"
        elif LangueOption == "4":
            LangueOption = "de"
        else:
            print(" La langue choisie ne figure pas dans notre serveur")
        print("Entrez le texte à traduire \n")
        Texte = input(" ")
        trad = Translator(from_lang="zh", to_lang=LangueOption)
        Texte = trad.translate(Texte)
        print(Texte)

    else :
        print (" Choix non disponible")
        ChoixNonDisponible()

def ConfirmUSSD():
    ussd = input(" Entrez le code USSD : ")
    if ussd == "#732#":
        MenuPrincipal()
    else:
        print(
            "Code USSD invalide \n"
            "Réessayez \n"
            )
        ConfirmUSSD()

ConfirmUSSD()
