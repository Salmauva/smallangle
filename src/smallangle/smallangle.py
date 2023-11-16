# Salma Abd Adin
# assignment about clicks

# import needed libraries
import click
import numpy as np
from numpy import pi
import pandas as pd


# make group of multible sub commdandos
@click.group()

def cmd_group():
    """Function that passes over other functions
    Args: 
        none
    """     
    pass


# sub commando for sin with right steps
@cmd_group.command()

# option for how many steps for tan
@click.option(
    "-n",
    "--count",
    default=1,
    help="Choose how many steps between 0 and 2pi you want",
    show_default=True,  # show default in help
)

def sin(count):
 
    """Function calculate sin between 0 and 2pi and give it as a list with length the given count
    
    Args: 
        count (int): give how many steps between 0 and 2pi you want
    """  
     
    x = np.linspace(0, 2 * pi, count)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)


# sub commando for tan with right steps
@cmd_group.command()

# option for how many steps for tan
@click.option(
    "-n",
    "--count",
    default=1,
    help="Choose how many steps between 0 and 2pi you want",
    show_default=True,  # show default in help
)

def tan(count): 

    """Function calculate tan between 0 and 2pi and give it as a list with length the given count
    
    Args: 
        count (int): give how many steps between 0 and 2pi you want
    """     
    x = np.linspace(0, 2 * pi, count)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

# do a command so you can call the name 'smallangle'
if __name__ == "__main__":
    cmd_group()
