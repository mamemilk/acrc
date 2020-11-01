#!/bin/bash
lex fig09_10.l
gcc fig09_09.c fig09_12.c fig09_20.c -o sl0
cat fig09_02.SL0 | ./sl0