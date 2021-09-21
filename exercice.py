#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	sous_total = 0
	for i in data:
		sous_total += i[1]*i[2]

	taxes = sous_total * 0.15
	total = sous_total + taxes

	facture = [
		("SOUS TOTAL", sous_total),
		("TAXES", taxes),
		("TOTAL", total)
	]

	print(name)
	fac = ""
	for k in facture:
		if k == facture[0]:
			foo = k[0] + "{:>10.2f}".format(k[1]) + " $" + "\n"
			fac += foo
		else:
			foo = k[0] + "{:>15.2f}".format(k[1]) + " $" + "\n"
			fac += foo
	return fac


def format_number(number, num_decimal_digits):
	string = ""
	round_number = round(number, num_decimal_digits)
	intnumber = int(round_number)
	for i in range(intnumber):
		while i < 4:
			for k in number:
				string += k
				return string

def get_triangle(num_rows):
	return ""


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
