#!/usr/bin/env python3
# lab_01_part_c.py
# Jared Rhodes
# 11/01/2017

""" This is the third part of Chapter 1 Lab Pygame """

print("Finding your current damage output")

attack_Speed = float(input("Please enter your current attack speed: "))
attack_Damage = float(input("Please enter your current attack damage: "))
critical_Chance = float(input("Please enter your current critical chance: "))

damage_Output = (attack_Speed * attack_Damage) * (1 + (critical_Chance * 1))

print('Your current damage per second is:', damage_Output)

