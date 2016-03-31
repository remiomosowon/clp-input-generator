#!/bin/bash

# for each input file in the directory, run the program
# using the different supplied entropy weightings.
for fn in *.txt; do
    for w in 0 0.5 0.9 0.95 0.96 0.97 0.98 0.99 1; do
        mono ContainerLoader.exe "$fn" $w 1 600
    done
done

