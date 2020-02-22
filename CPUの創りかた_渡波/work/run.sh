#!/bin/bash 

iverilog -g2005-sv ../src/cpu_decoder.v ../src/cpu_rom.v ../src/cpu_top.v ; 
./a.out;
