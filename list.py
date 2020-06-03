import click
from graph import g

@click.command()
def main():
    for unit in g.unit_dict.keys():
        print(unit)

if __name__ == '__main__':
    main()