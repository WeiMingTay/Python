# user_input = input("Wert zur Prüfung eingeben: ")
user_input = "False"

def is_it_bool(wert):
    return bool(wert)

output = is_it_bool(user_input)
print(output)
print(f"'input()' generiert immer einen String. Jede Eingabe, außer ' ' wäre somit True. Somit ist auch eine Eingabe von zB '0' Wahr.")

# Mögliche Lösung: Die False-Werte abfangen mit einer if-Abfrage
# Mögliche Gefahr: ALLES außer die Werte in der Liste sind True
def if_its_bool(wert):
    # entfernt mögliche Leerzeichen am Anfang und Ende und macht Kleinbuchstaben
    wert_clean = wert.strip().lower()
    
    if wert_clean in ["false", "0", "nein", "falsch", "no"]:
        return False
    else:
        return True
    
output_if = if_its_bool(user_input)
print(output_if)