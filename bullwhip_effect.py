import random

un_1 = 0
on_2 = 0
ivn_1 = 15

ivn = 0
un = 0
on = 15


def calc_ivn(on_2, ivn_1, cn, un_1):
	ivn = on_2 + ivn_1 - cn - un_1
	if ivn < 0:
		return 0
	return ivn


def calc_un(un_1, cn, ivn):
	un = un_1 + cn - ivn
	if un < 0:
		return 0
	return un


def change_in_orders(ivn, un):
	if un == 0 & 0 <= ivn < 10:
		return 0
	elif 0 < un <= 5:
		return 5
	elif un > 5:
		return 10
	elif ivn >= 10:
		return -5


i = 0
for x in range(51):
	# sets the numbers for last week n-1
	ivn_1 = ivn
	un_1 = un
	on_1 = on

	if i % 2 == 0:
		on_2 = on

	# random variable from 0 to 100 that tells us the customers we get
	r = random.randint(0, 100)
	if r <= 7:
		cn = 9
	elif 7 < r <= 92:
		cn = 15
	else:
		cn = 21

	# calculates inventory for week n
	ivn = calc_ivn(on_2, ivn_1, cn, un_1)

	# unfilled orders for week n
	un = calc_un(un_1, cn, ivn)

	# number of orders we should put in
	on = on_1 + change_in_orders(ivn, un)

	print("week ", i," \ninventory: ", ivn, "\nunfilled: ", un, "\norders: ", on, "\n\n")
	i += 1




