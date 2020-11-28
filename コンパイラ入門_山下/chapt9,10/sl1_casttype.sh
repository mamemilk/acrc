#!/bin/bash
lex fig09_14.l
yacc fig09_16_ct.y
gcc fig09_09.c fig09_20.c y.tab.c  tab10_01.c fig10_01.c fig10_03.c tab10_03.c -o sl1_ct

cat fig09_06.SL1 | ./sl1_ct

