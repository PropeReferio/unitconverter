import json
from graph import Graph, Unit

with open('conversions.json', 'r') as f:
    datastore = json.load(f)  #something about closing files after you're 
    #done... does "with" autoclose?

#Instantiates the Graph
g = Graph()

#Adds units, edges, and cfactors (weights)
for conv in datastore:
    g.add_edge(conv[0], conv[1], conv[2])

#Print statements to check that it worked:
# for k, v in g.unit_dict.items():
#     for neighbor, cfactor in v.adjacent.items():
#         print('Unit: {}, Neighbor: {}, Cfactor: {}'.format(k, neighbor.name, cfactor))

def BFS_cfactor(start, stop, graph):
    '''Begins at one unit/vertex (start), finds the shortest path to the final
    unit/vertex (stop), and returns the conversion factor between those two
    units (the product of all the cfactors (weights) that were traversed).'''
    active = True
    if start not in graph.unit_dict.keys():
        print("{} is not a valid input.".format(start))
        active = False
    if stop not in graph.unit_dict.keys():
        print("{} is not a valid input.".format(stop))
        active = False
    if not active:
        return False #Or other error message of some kind.
    
    queue = [(start, 1)] 
    visited = set()

    while queue:
        unit, cfactor = queue.pop(0)
        visited.add(unit)
        for node in graph.unit_dict[unit].adjacent.keys(): #Need keys or items or something
            if node == stop:
                return cfactor * graph.unit_dict[unit].adjacent[stop]
            else:
                if node not in visited:
                    visited.add(node)
                    queue.append((node, cfactor * graph.unit_dict[unit].adjacent[node]))
    #If the queue empties...
    return 'No path found from {} to {}.'.format(start, stop)

# print(BFS_cfactor('mile', 'foot', g))

def convert(original: str, converted: str, n: int) -> int:
    '''Takes as arguments the unit to convert from (original), the amount of 
    that unit (n), and the unit to convert to (converted), and outputs the 
    amount of that final unit.'''
    return n * BFS_cfactor(original, converted, g)

print(convert('meter', 'centimeter', 15))

