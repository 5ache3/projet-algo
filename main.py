

class Colis:
    def __init__(self,id,priorite,poid,ordre,destination=None):
        self.id=id
        self.priorite=priorite
        self.poid=poid
        self.ordre=ordre
        self.destination=destination
    
    def json(self):
        return {
            'id':self.id,
            'priorite':self.priorite,
            'poids':self.poid,
            'ordre':self.ordre,
            'destinaton':self.destination
        }
    
    def aficher(self):
        print(f"""--------------
id : {self.id}
priorité : {self.priorite}
poids : {self.poid} kg
ordre : {self.ordre}
"""+f'destination : {self.destination}' if self.destination else ''
)



class File:
    def __init__(self):
        self.list=[]
        self.index=1

    def ajouter(self,priorite,poid,destination=None):
        coli=Colis(
            id=self.index,
            priorite=priorite,
            poid=poid,
            ordre=len(self.list)+1,
            destination=destination)
        
        self.list.append(coli)
        self.index+=1

    def defiler(self):
        p=self.list[0]
        new_list=[]
        for coli in self.list[1:]:
            new_list.append(
                Colis(
                    id = coli.id,
                    priorite = coli.priorite,
                    poid = coli.poid,
                    ordre = coli.ordre-1,
                    destination = coli.destination
                ))
        self.list=new_list
        return p
    
    def aficher(self):
        for coli in self.list:
            coli.aficher()

    def json(self):
        return [coli.json() for coli in self.list]
    
    def sort(self):
        n=len(self.list)
        for i in range(n):
            for j in range(n-1-i):
                if self.list[j+1].priorite>self.list[j].priorite:
                    self.list[j+1],self.list[j]=self.list[j],self.list[j+1]
class Pile:
    def __init__(self):
        self.list=[]
        

    def ajouter(self,coli):
        coli.ordre=len(self.list)+1
        self.list.append(coli)
        

    def depiler(self):
        return self.list.pop()
    
    def aficher(self):
        for coli in self.list:
            coli.aficher()

    def json(self):
        return [coli.json() for coli in self.list]
    
    def sort(self):
        n=len(self.list)
        for i in range(n):
            for j in range(n-1-i):
                if self.list[j+1].priorite < self.list[j].priorite:
                    self.list[j+1],self.list[j]=self.list[j],self.list[j+1]


def charger(file,pile):
    try:
        c=file.defiler()
        pile.ajouter(c)
    except:
        print("file est vide")

