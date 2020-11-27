#!/bin/bash
lex fig09_14.l
yacc fig09_16.y
gcc fig09_09.c fig09_20.c y.tab.c -o sl1

cat fig09_06.SL1 | ./sl1

cat fig09_02.SL0 | ./sl1 > SL0bySL1.txt 
cat fig09_02.SL0 | ./sl0 > SL0bySL0.txt 
diff SL0bySL1.txt SL0bySL10.txt
