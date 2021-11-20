class ToolBox:
    """Boite à outils"""
    def __init__(self):
        self.outils = set()
    def ajouter(self, outil):
        self.outils.append(outil)
    def enlever(self, outil):
        self.outils.pop(outil)

class Hammer:
    """Marteau"""
    def __init__(self):
        self.couleur = "red"
    def planter_clou():
        pass
    def retirer_clou():
        pass

class Screwdriver:
    """Tournevis"""
    def __init__(self):
        self.taille = 5
    def serrer_vis():
        pass
    def desserrer_vis():
        pass
