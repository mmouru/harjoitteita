class Node: 
    def __init__(self, name, address, number, n = None):
        self.name = name
        self.address = address
        self.number = number
        self.next_node = n

class LinkedList (object):
    def __init__ (self, head = None):
        # Alusta lista
        self.head = head
        self.length = 0
    def delete_all (self):
        while (self.head != None):
            temp = self.head
            self.head = self.head.next_node
            temp = None
    def add (self, name, address, number):
        # Lisää uusi linkki ja kytke se headiin.
        new_node = Node (name, address, number, self.head)
        self.head = new_node
        self.length += 1
    def print(self):
        # tyhjä res merkkijono
        res = ""
        # Pointteri listan päähän
        ptr = self.head 
        # Kun pointteri vielä osoittaa johonkin jäseneen, lisää jäsenen tiedot merkkijonoon
        while ptr:
            res += "[" + str(ptr.name) + " : " + str(ptr.address) + " : " + str(ptr.number) + "]"
            res += " -> "
            ptr = ptr.next_node
        res += "NULL"
        if self.length == 0:
            print("########################################")
            return "Lista on tyhja!"
        else:
            print("########################################")
            print("Listassa on seuraavat alkiot: ")
            return res

myList = LinkedList()

valinta = 5
while(valinta):
    print("Mita tehdaan seuraavaksi?")
    print("1 = Henkilotiedon lisays")
    print("2 = Henkilotietojen tulostus")
    print("3 = Kaikkien henkilotietojen poisto")
    print("0 = Lopetus")
    try:
        valinta = int(input("Valintasi: ")) 
        if ( valinta < 0 or valinta > 3):
            print("########################################")
            print("Valinnan tulee olla valilta 0 -3")
            print("########################################")  
    except ValueError:
        print("########################################")
        print("Valinnan tulee olla kokonaisluku!")
        print("########################################")
    if (valinta == 1):
        nimi = input("Anna henkilon nimi: ")
        osoite = input("Anna henkilon osoite: ")
        puhelinnumero = input("Anna henkilon puhelinnumero: ")
        myList.add(nimi, osoite, puhelinnumero)
    elif (valinta == 2):
        print(myList.print())
        print("########################################")
    elif (valinta == 3):
        myList.delete_all()
    
