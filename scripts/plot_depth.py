#!/usr/bin/env python3
"""Reads a DynSLAM depth evaluation CSV and plots relevant plots."""

import click
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


@click.group()
def cli():
    """Entry point for all subcommands."""
    pass

@cli.command()
@click.argument('input', type=click.File('r')) # CSV file produced by DynSLAM in evaluation mode.
def plot(input: click.File):
    click.echo("Will plot stuff from file {}".format(input.name))
    frame = pd.read_csv(input)
    print("{} rows".format(frame.shape[0]))
    print(frame.columns.values)

    acum = frame.sum()

    accs = []
    delta_maxes = range(1, 8)
    for i in delta_maxes:
        total = acum[1 + i * 4]
        error = acum[1 + i * 4 + 1]
        missing = acum[1 + i * 4 + 2]
        correct = acum[1 + i * 4 + 3]
        acc = correct * 1.0 / (total - missing)
        print(total, error+missing+correct)
        print()

        accs.append(acc)

    # TODO look for best practices for mpl figures and use them
    plt.plot(delta_maxes, accs)
    plt.xlabel(r"$\delta_{\text{max}}$")
    plt.ylabel(r"")
    plt.show()






if __name__ == '__main__':
    cli()

