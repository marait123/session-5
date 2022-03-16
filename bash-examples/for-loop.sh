#!/bin/bash

echo "===================================="
# generate a sequence of numbers from 0 to 10 increase by 2
seq 0 2 10

echo "===================================="
zero=0;
for i in $(seq 1 1 10)
    do 
       
        # echo $i;
        if [ `expr $i % 2` -eq 0 ]; then
            echo $i "divided by 2"
        elif [ $i -le 5 ]; then
            echo $i "is not divided 0 and less than or equal 5"

        else\
            echo $i "is not divided 0 and greater than 5"
        fi

    done

#  files 
# remove directory
rm -r folder
# mk directory
mkdir folder
# create 10 files
for i in $(seq 1 1 10)
    do
        echo "this is file " $i > ./folder/file$i.txt 
    done

# display files contents
for i in ./folder/*
    do
        echo "===================================================="
        echo "for file "  $i " contents are => "
        cat $i 
        echo "===================================================="
    done
