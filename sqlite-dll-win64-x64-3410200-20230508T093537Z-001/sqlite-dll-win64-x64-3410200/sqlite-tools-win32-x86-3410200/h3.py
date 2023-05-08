import sqlite3

def create_table():
    conn = sqlite3.connect('avinogradov.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS avinogradov(nimi TEXT, vanus INTEGER)')
    conn.commit()
    conn.close()
    
def auto_lisamine():
    name = input("Sisesta nimi: ")
    surname = input("Sisesta perekonnanimi: ")
    email = input("Sisesta e-posti aadress: ")
    car_make = input("Sisesta auto mark: ")
    car_model = input("Sisesta auto mudel: ")
    car_year = int(input("Sisesta auto aasta: "))
    price = int(input("Sisesta auto hind: "))

    conn.execute("""
        INSERT INTO cars (firs_name, last_name, email, car_make, car_model, car_year, car_price)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (first_name, last_name, email, car_make, car_model, car_year, price))
    conn.commit()
    conn.close()

    print("Auto lisatud edukalt!")

def lisa_kasutaja():
    nimi = input('Sisestage kasutaja nimi: ')
    vanus = int(input('Sisestage kasutaja vanus: '))
    conn = sqlite3.connect('avinogradov.db')
    c = conn.cursor()
    c.execute('INSERT INTO avinogradov VALUES(?,?)', (nimi, vanus))
    conn.commit()
    conn.close()
    
def auto_otsimine():
    # Ühendus andmebaasiga
    conn = sqlite3.connect('avinogradov.db')
    c = conn.cursor()

    # SQL päring
    c.execute("SELECT * FROM avinogradov WHERE car_year < 2000 ORDER BY car_year ASC LIMIT 20;")
    result = c.fetchall()
    
    for results in result:
        print(results)
    conn.close()
    
def loe_avinogradov():
    print("valisid 2")
    conn = sqlite3.connect('avinogradov.db')
    c = conn.cursor()
    c.execute('SELECT * FROM avinogradov')
    tulemused = c.fetchall()
    for tulemus in tulemused:
        print(tulemus)
    conn.close()

def otsi_kasutajat():
    nimi = input('Sisestage kasutaja nimi: ')
    conn = sqlite3.connect('avinogradov.db')
    c = conn.cursor()
    c.execute('SELECT * FROM avinogradov WHERE first_name = ?', (nimi,))
    tulemused = c.fetchall()
    for tulemus in tulemused:
        print(tulemus)
    conn.close()

def kustuta_kasutaja():
    nimi = input('Sisestage kasutaja nimi: ')
    conn = sqlite3.connect('avinogradov.db')
    c = conn.cursor()
    c.execute('DELETE FROM avinogradov WHERE first_name = ?', (nimi,))
    conn.commit()
    conn.close()

def valikud():
    print('Valige, mida soovite teha:')
    print('1. Lisa kasutaja')
    print('2. Loetle kõik avinogradov')
    print('3. Otsi kasutajat')
    print('4. Kustuta kasutaja')
    print('5. adnmed in one l line')
    print('6. Autod of "2000"')
    print('7. Välju programmist')

def main():
    create_table()
    while True:
        valikud()
        valik = input('Sisestage valiku number: ')
        if valik == '1':
            lisa_kasutaja()
        elif valik == '2':
            loe_avinogradov()
        elif valik == '3':
            otsi_kasutajat()
        elif valik == '4':
            kustuta_kasutaja()
        elif valik == '5':
            auto_lisamine()
        elif valik == '6':
            auto_otsimine()        
        elif valik == '7':
            break
        else:
            print('Vale valik. Palun proovige uuesti.')

if __name__ == '__main__':
    main()
