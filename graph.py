import json

class Unit():
    def __init__(self, name):
        self.name = name
        self.adjacent = {}
        #Key is a string, value is cfactor.

    def add_neighbor(self, neighbor, cfactor):
        self.adjacent[neighbor] = cfactor

    # def get_connections(self):
    #     return self.adjacent.keys()

    def get_cfactor(self, neighbor):
        return self.adjacent[neighbor]

class Graph():
    def __init__(self):
        self.unit_dict = {}
        # Key is a string, like 'inch', value is a Unit object

    def add_unit(self, name):
        new_unit = Unit(name)
        self.unit_dict[name] = new_unit

    def add_edge(self, frm, to, cfactor):
        if frm not in self.unit_dict:
            self.add_unit(frm)
        if to not in self.unit_dict:
            self.add_unit(to)

        self.unit_dict[frm].add_neighbor(self.unit_dict[to].name, cfactor)
        self.unit_dict[to].add_neighbor(self.unit_dict[frm].name, 1/cfactor)
        #This is key. Make sure you've inverted the correct cfactor.
        #I'm confident this is correct.

with open('conversions.json', 'r') as f:
    datastore = json.load(f)  #something about closing files after you're 
    #done... does "with" autoclose?

#Instantiates the Graph
g = Graph()

# #Adds units, edges, and cfactors (weights)
for conv in datastore:
    g.add_edge(conv[0], conv[1], conv[2])
#Instantiate the Graph

# g = Graph()

# #Add units and edges to Graph
# for conv in units:
#     g.add_edge(conv[0], conv[1], conv[2])

#Checks that units were added with correct cfactors
# for k, v in g.unit_dict.items():
#     for neighbor, cfactor in v.adjacent.items():
#         print('Unit: {}, Neighbor: {}, Cfactor: {}'.format(k, neighbor, cfactor))

# print(g.unit_dict['day'].adjacent.keys())