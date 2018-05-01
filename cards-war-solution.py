# Cards War
#
# Alice and Bob are playing a game called Cards War. Both players have one deck
# containing N cards each. The hierarchy of card values is as follows:
# ace(marked with the symbol A), king(K), queen(Q), jack(J), ten(T)
# and from nine to two(9−2).
#
# The game is played in turns. In every turn, each player draws one card from
# the top of their deck. The player who draws the higher card wins the current
# turn. If both players draw the same card, nobody wins and they proceed to the
#  next turn. After each turn, the drawn cards are put aside and not used again
#  in the current game.
#
# Let's consider a single game, where: Alice's deck consists
# of(from top to bottom): ace, five, eight, six, queen, king
# Bob's deck consists of(from top to bottom): jack, jack, six, five, three, king.
#
# Alice wins the first, third, fourth and fifth turns. Bob wins the second turn.
# Note that nobody wins the last turn since both players draw the same card(king).
#
# Write a function that, given two non - empty strings A, B consisting of N card
# symbols(representing Alice's and Bob's decks, respectively), returns the number of turns that Alice will win.
#
# For example, given "A586QK" and "JJ653K", your function should return 4, as
# explained above.
#
# Given "23A84Q" and "K2Q25J", your function should also return 4, since Alice
# wins the second, third, fourth and sixth turns.
#
# Assume that N is an integer within the range[1..1, 000]
# strings A and B consist only of the following characters: 2 - 9, T, J, Q, K and / or A
# strings A and B are of equal length.


def solution(cardsA, cardsB):

    cardValue = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    ans = 0
    N = len(cardsA)

    alice = 0
    bob = 0
    for i in range(N):
        if cardsA[i] not in cardValue:
            alice = int(cardsA[i])
        else:
            alice = cardValue[cardsA[i]]
        if cardsB[i] not in cardValue:
            bob = int(cardsB[i])
        else:
            bob = cardValue[cardsB[i]]
        if alice > bob:
            ans+=1;
    return ans


# print(solution("23A84Q", "K2Q25J"))
# print(solution("KKKKK", "KKKKK"))
# print(solution("A586QK", "JJ653K"))
