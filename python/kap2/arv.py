class Dyr:
  def __init__(self,navn,rase,farge):
    self.navn = navn
    self.rase = rase
    self.farge = farge

  def dyr_info(self):
    print(self.navn,"er en",self.farge.lower(),self.rase.lower())


class Katt(Dyr):
  def __init__(self,navn,rase,farge,liv):
    super().__init__(navn,rase,farge)
    self.liv = liv
  
  def snakk(self):
    print(self.navn,'sier "Mjau"')

  def antall_liv(self):
    self.liv += 1
    print(self.navn,"har nå",self.liv,"liv.")


class Hund(Dyr):
  def __init__(self,navn,rase,farge):
    super().__init__(navn,rase,farge)
  
  def snakk(self):
    print(self.navn,'sier "Voff"')



mine_dyr = [
  Katt("Silkesvarten","Norsk skogkatt","Svart",2),
  Katt("Tigergutt","Norsk skogkatt","Stripete grå-svart",1),
  Hund("Kaisa","Labrador retriever","Svart")
]

mine_dyr[0].snakk()
mine_dyr[2].snakk()
mine_dyr[1].dyr_info()
mine_dyr[0].antall_liv()
mine_dyr[0].antall_liv()
mine_dyr[0].antall_liv()