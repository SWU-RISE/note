#!/bin/bash

allfiles=`find . -name *.cpp `
INC="-I ../include -I ../poly/include -I ../util/include -I ../sdp/include -I ../psd/include"
LIB="-L ../lib -lutil -lsdp -lpsd -lpoly -lgtest -lpthread"

for ff in  $allfiles
do
    bname=${ff##*/}
    bbname=${bname%.cpp}
    echo $bbname

    g++ $ff $(echo $INC)  $(echo $LIB)   -o $bbname #usage 
    ./$bbname

done
