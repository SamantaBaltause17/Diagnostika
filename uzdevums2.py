#Samanta Baltause 18.10.2024

Passwords = []

while True:
    Password = input("Enter the correct password: ")          # jaievada parole
    if Password.lower() == "python123" :                      # pareizā parole
          Passwords.append(Password)
          break
    elif Password.lower() != "python123":                     # pareizā parole
        print("Piekļuve liegta, ievadiet vēlreiz:")           # ja parole būs nepareiza izvadīs piekļuve leigta
        print("Piekļuve atļauta!")                            # ja parole būs pareiza izvadīts piekļuve atļauta