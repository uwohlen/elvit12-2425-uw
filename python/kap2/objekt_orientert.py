class Dyr:
  def __init__(self,navn,rase,farge):
    self.navn = navn
    self.rase = rase
    self.farge = farge

  def dyr_info(self):
    print(self.navn,"er en",self.farge.lower(),self.rase.lower())

mine_dyr = [
  Dyr("Silkesvarten","Norsk skogkatt","Svart"),
  Dyr("Tigergutt","Norsk skogkatt","Stripete grå-svart"),
  Dyr("Kaisa","Labrador retriever","Svart")
]

mine_dyr[1].dyr_info()

