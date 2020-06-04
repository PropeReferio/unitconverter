#!/usr/bin/env python

import click
from graph import g

@click.command() #I think I can remove click from this file.
def main():
    print('\n The following units are available: \n')
    for unit in g.keys():
        print(unit)
    print('\n')

if __name__ == '__main__':
    main()