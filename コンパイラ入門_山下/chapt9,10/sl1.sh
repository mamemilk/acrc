#!/bin/bash
lex fig09_14.l
yacc fig09_16.y
gcc fig09_09.c fig09_20.c y.tab.c -o sl1

cat fig09_06.SL1 | ./sl1


cat fig09_02.SL0 | ./sl1
cat fig09_02.SL0 | ./sl0
