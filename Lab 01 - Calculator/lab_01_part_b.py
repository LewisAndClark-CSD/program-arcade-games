#!/usr/bin/env python3
# Lab B Chapter 1
#Bethany DuMontelle
#1 November 2017

print('Area of a trapezoid')
trap_height = int(input("Enter the height of the trapezoid: "))
trap_bbase = int(input('Enter the ength of the bottom base: '))
trap_tbase = int(input('Enter the length of the top base: '))

trap_area = 1/2(( (trap_bbase) + (trap_tbase) ) * (trap_height))

print(str(trap_area))