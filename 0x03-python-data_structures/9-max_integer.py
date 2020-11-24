#!/usr/bin/python3


def max_integer(my_list=[]):
	if my_list == []:
		return None

	max = sorted(my_list)[-1]

	return max
