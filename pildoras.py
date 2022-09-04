

def run():
    
    while True: 
        email = input("introduce email: ")
        if "@" not in email:
            print("no tiene @")
        if (email.count("@")==1):
            if email[0]!="@" and email[(len(email)-1)]!="@":
                print("email correcto")
                break
            else:
                print("@ no puede estar al inicio o al final")
        else:
            print("solo puede tener un arroba")
            

if __name__ == '__main__':run()