class __classgraph__():
    edges = []
    vertices = []
    def __init__(self,arquivo):
        with open(arquivo) as file:
            for line in file:
                line = line.strip('\n')
                line = line.split(',')
                for element in line:
                    if((element in self.__class__.vertices )==False):
                        self.__class__.vertices.append(element)
                line[0]=self.__class__.vertices.index(line[0])
                line[1]=self.__class__.vertices.index(line[1])
                self.__class__.edges.append(line)
    def edgesout(self):
        matriz=[]
        for i in range(0,len(self.__class__.vertices)):
            vertice=[]
            for x in self.__class__.edges:
                if i==x[0]:
                    vertice.append(x[1])
            matriz.append(vertice)
        return matriz   
    def edgesin(self):
        matriz=[]
        for i in range(0,len(self.__class__.vertices)):
            vertice=[]
            for x in self.__class__.edges:
                if i==x[1]:
                    vertice.append(x[0])
            matriz.append(vertice)
        return matriz