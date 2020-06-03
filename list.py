#!/usr/bin/env python

import click
from graph import g

@click.command()
def main():
    print('\n The following units are available: \n')
    for unit in g.unit_dict.keys():
        print(unit)
    print('\n')

if __name__ == '__main__':
    main()