# Generate input files with a varying number of pallets to fill
# up a container up to a specified capacity using liquid logic.

from __future__ import division
import random
from collections import namedtuple
import datetime
import os

# Pallet Type Dimensions:
#    S  = 80x70
#    N  = 105x78
#    E  = 120x81
#    E2 = 80x60

PalletType = namedtuple("PalletType", "name length breadth area")

pallet_type_data = [('S', 80, 70), ('N', 105, 78), ('E', 120, 81), ('E2', 80, 60)]
pallet_types = {name: PalletType(name, length, breadth, length * breadth) for (name, length, breadth) in
                pallet_type_data}

default_pallet_weight = 250
default_pallet_height = 65
default_stackability = 1

container_area = 1203 * 235


# Return a dict of pallets that fill up a container up to the
# specified (percentage) capacity. Each pallet is generated
# with equal chance.
def fill_with_equal_probability(capacity):
    pallets = {name: 0 for name in pallet_types}
    max_area = capacity / 100 * container_area
    fill_area = 0
    total = 0

    while fill_area <= max_area:
        for pallet in pallets:
            if random.randint(0, 1):
                pallets[pallet] += 1
                fill_area += pallet_types[pallet].area
                total += 1

    return total, pallets


# Helper method to pad a numeric string with 0s on the left,
# to fill a field of specific width.
def rjust3(value):
    return str(value).zfill(3)


# Write a list of supplied pallets to an input file.
def create_output_file(pallets, total, capacity, filenum, prefix='input_', dir=None):
    cap = rjust3(capacity)  # used container capacity (liquid logic)
    fnum = rjust3(filenum)  # file number
    tot = rjust3(total)  # total number of pallets
    ftime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')  # current date and time

    filename = prefix + "c{}_{}_t{}_{}.txt".format(cap, fnum, tot, ftime)

    if dir is not None:
        # if a directory is specified, add it to the filename
        filename = dir + "/" + filename

        # if the directory doesn't exist, create it
        if not os.path.exists(dir):
            os.mkdir(dir)

    with open(filename, 'w') as ofile:
        plt_num = 1
        for pallet in pallets:
            for i in range(pallets[pallet]):
                pallet_num = "GRP/" + rjust3(plt_num)
                length = pallet_types[pallet].length
                breadth = pallet_types[pallet].breadth
                weight = default_pallet_weight
                height = default_pallet_height
                stackability = default_stackability
                ofile.write(
                    "{}\t{}\t{}\t{}\t{}\t{}\n".format(pallet_num, weight, length, breadth, height, stackability))
                plt_num += 1


def main():
    capacities = [60, 70, 80, 90, 100]
    num_of_files_per_capacity = 50

    for capacity in capacities:
        for fnum in range(1, num_of_files_per_capacity + 1):
            total, pallets = fill_with_equal_probability(capacity)
            create_output_file(pallets, total, capacity, fnum, dir='equal_chance')


if __name__ == '__main__':
    main()
