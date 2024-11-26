neki_broj = int(5)
neki_dec_broj = float(3.4)
neki_tekst = str("Ovo je neki tekst")

print(neki_tekst.upper()) #funkcije unutar klase su metode,
                          #upper je metoda klase string (lower..)
#sad mi pravimo nasu klasu
class pravougaonik:
    def __init__(self, a, b):
        self.stranica_a = a
        self.stranica_b = b

    def povrsina(self):
        return self.stranica_a * self.stranica_b

    def obim(self):
        return (self.stranica_a * self.stranica_b) * 2

soba1 = pravougaonik(4, 3)
print(f"povrsina: {soba1.povrsina()}")
print(f"obim: {soba1.obim()}")

soba1.stranica_a = 5
soba1.stranica_b = 4
soba1.dijagonala = 6

print(f"dijagonala: {soba1.dijagonala}")


