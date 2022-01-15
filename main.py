from Modele.Zamowienie import Zamowienie
from Modele.Developer import Developer
from Modele.Dom import Dom
from Modele.Mieszkanie import Mieszkanie

developerDomu = Developer(4, 'polna 7', '223-234-324', 'Firma 1')
developerMieszkania = Developer(7, 'polna 9', '123-234-324', 'Firma 1')
dom1 = Dom(3, developerDomu, 'polna 2', 250, 6000, 2)
mieszkanie = Mieszkanie(4, developerMieszkania, 'polna 3', 50, 10000, 5)

zamowienie = Zamowienie(8, [dom1, mieszkanie], 'Polska', 'Kowalski')
print(zamowienie)
