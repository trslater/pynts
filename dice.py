"""Monte Carlo simulation to calculate the chance of a number of dice being
greater than some value
"""


import sys
import random
import functools


try:
	DEBUG = sys.argv[1].lower() == "debug"

except IndexError:
	DEBUG = False


def main():
	order = 5
	print(p(1, 6, 6, 10**order))
	print(p(2, 6, 12, 10**order))
	print(p(3, 6, 18, 10**order))


def p(min_target_rolls, target_value, num_dice, num_trials, num_sides=6):
	debug(
		f"Simulation: what is the chance that the value of {min_target_rolls} "
		f"in {num_dice} dice is greater than {target_value}?")

	num_successes = 0

	debug("Run trials...")
	for i in range(num_trials):
		rolls = random.choices(range(1,num_sides+1), k=num_dice)
		succeeded = rolls.count(target_value) >= min_target_rolls

		debug("Trial #{trial_num}: {rolls} ... {result}".format(
			trial_num=i+1,
			rolls=rolls,
			result="succeeded" if succeeded else "failed"))

		if succeeded:
			num_successes += 1

	debug("Trials done.")

	debug(f"Num succeeded: {num_successes}/{num_trials}")
	debug(f"Success rate: {100*num_successes/num_trials}%")

	return num_successes/num_trials


def debug(*msg):
	if DEBUG:
		print(*msg)


if __name__ == "__main__":
	main()
