# Reversing Coins
#
# There are N coins, each showing either heads or tails. We would like all the
# coins to show the same face. What is the minimum number of coins that must be reversed?
#
# Write a function that, given a zero-indexed array A consisting of N integers
# representing the coins, returns the minimum number of coins that must be reversed.
# Consecutive elements of array A represent consecutive coins and contain only a 0 (heads) or a 1 (tails).

# For example, given array A = [1, 0, 0, 1, 0, 0], there are four coins showing heads
# and two coins showing tails. The function should return 2, as after reversing
# two coins (in positions 0 and 3), all the coins will be showing the same face (heads).
#
# Assume that N is an integer within the range [1..100]; each element of array A
# is an integer that can have one of the following values: 0, 1.

def solution(coins):
	heads,tails=0,0;

	for i in coins:
		if i==0: heads+=1
		else: tails+=1
	return min(heads,tails)

# print(solution([]))
