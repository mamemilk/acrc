#!/bin/bash
lex fig09_10.l
gcc fig09_09.c fig09_12_cs.c fig09_20.c tab10_01.c fig10_01.c -o sl0_cs
cat fig09_02.SL0 | ./sl0_cs