class Cake:
    
    def __init__(self, flavor):
        self.flavor = flavor

    def cut_in_part(self):
        print("Le gateau est coupé en 4 !")

class ToolBox:
    
    def __init__(self):
        self.tools=[]
    def add_tool(self, tool):
        self.tools.append(tool)
        print("Un outil à été ajouté à la boite")
    def remove_tool(self,tool):
        self.tools.remove(tool)
        print("Un outil à été enlevé")

class Hammer:
    def __init__(self,color="red"):
        self.color = color
    def hammer_in(self, nail):
        print ("Vous planté un clou")
    def remove(self, nail):
        print("Vous avez retiré un clou")
    def paint(self,color):
        self.color = color
        print("Vous avez repeint votre marteau en" + color)

class Screwdriver:
    def __init__(self, size):
        self.size = size
    def tighten(self, screw):
        print("La vis est maintenant serrée")
    def loosen(self, screw):
        print("La vis est maintenant desserrer")
