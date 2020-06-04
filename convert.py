#!/usr/bin/env python

import click
from graph import g

def BFS_cfactor(start, stop, graph):
    '''Begins at one unit/vertex (start), finds the shortest path to the final
    unit/vertex (stop), and returns the conversion factor between those two
    units (the product of all the cfactors (weights) that were traversed).'''
    
    queue = [(start, 1)] 
    visited = set()

    while queue:
        #BFS finds the shortest path between the two units, and cfactor is constantly updated
        #with each movement between nodes.
        unit, cfactor = queue.pop(0)
        visited.add(unit)
        for node in graph[unit]:
        #For each tuple in the list that is the value pair to the key unit:
            if node[0] == stop:
                return cfactor * node[1]
            else:
                if node[0] not in visited:
                    visited.add(node[0])
                    queue.append((node[0], cfactor * node[1]))
    #If the queue empties...
    return False
    #Can I delete the line above, and have a None value below?

#CLI stuff
@click.command()
@click.option('--quantity', '-q', default=1, help='The quantity of original\
units to be converted to final units.')
@click.argument('original')
@click.argument('converted')
def convert(quantity, original, converted):
    '''Takes as arguments the unit to convert from (original), the amount of 
    that unit (quantity), and the unit to convert to (converted), and outputs 
    the amount of that final unit.'''
    final = quantity * BFS_cfactor(original, converted, g)
    valid = True
    if original not in g.keys():
        print("{} is not a valid input.".format(original))
        valid = False          # Should I move these to try and except stuff somewhere?
    if converted not in g.keys():
        print("{} is not a valid input.".format(converted))
        valid = False
    if not valid:
        return False
    if not final:
        click.echo('{} cannot be converted to {}'.format(original, converted))
    else:
        click.echo('There are {} {}(s) in {} {}(s).'.format(final, converted, quantity, original))

if __name__ == '__main__':
    convert()
