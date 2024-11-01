class Anti_dyr:
  """
  Dum klasse for å lage dyr
  Parametre:
    x (str): Dyrets personlige navn
    y (str): Dyrets rase
    z (str): Dyrets farge
    w="Lang" (str): Beskrivelse av dyrets hale

  Intern variabel
    alder=0 (int): Dyrets alder i antall år. Endres med metoden aldring()
  """
  def __init__(s,x:str,y:str,z:str,w:str="Lang"):
    """
    Konstruktør
    """
    s.navn = x
    s.rase = y
    s.farge = z
    s.hale = w
    s.alder = 0

  def dyr_info(x):
    """
    Dum metode for utskrift
    """
    print(f"{x.navn} er en {x.farge.lower()} {x.rase.lower()}")
 


katt1 = Anti_dyr("Pus","Tibetansk nakenkatt","Lysebrun")

katt1.dyr_info()
