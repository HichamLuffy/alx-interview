# 0x0A-primegame


### Game Rules Recap
1. Maria and Ben take turns picking a prime number.
2. The chosen prime and all its multiples are removed from the set.
3. Maria always goes first.
4. The player who cannot make a move loses.

### Example Walkthrough
Let's take an example where \( n = 10 \).


#### Initial Set
\[ \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\} \]

1. **Maria's Turn**:
   - Maria picks the smallest prime, which is 2.
   - Remove 2 and its multiples (4, 6, 8, 10).

   Set after Maria's move:
   \[ \{1, 3, 5, 7, 9\} \]

2. **Ben's Turn**:
   - Ben picks the smallest remaining prime, which is 3.
   - Remove 3 and its multiples (9).

   Set after Ben's move:
   \[ \{1, 5, 7\} \]

3. **Maria's Turn**:
   - Maria picks the smallest remaining prime, which is 5.
   - Remove 5.

   Set after Maria's move:
   \[ \{1, 7\} \]

4. **Ben's Turn**:
   - Ben picks the only remaining prime, which is 7.
   - Remove 7.

   Set after Ben's move:
   \[ \{1\} \]

5. **Maria's Turn**:
   - There are no primes left for Maria to choose.
   - Maria loses this round.

### Analysis of Multiple Rounds

Consider \( x = 3 \) and \( \text{nums} = [4, 5, 1] \).

#### Round 1: \( n = 4 \)
- Initial Set: \[ \{1, 2, 3, 4\} \]
- Maria picks 2 (removes 2, 4), Set: \[ \{1, 3\} \]
- Ben picks 3 (removes 3), Set: \[ \{1\} \]
- Maria loses, Ben wins this round.

#### Round 2: \( n = 5 \)
- Initial Set: \[ \{1, 2, 3, 4, 5\} \]
- Maria picks 2 (removes 2, 4), Set: \[ \{1, 3, 5\} \]
- Ben picks 3 (removes 3), Set: \[ \{1, 5\} \]
- Maria picks 5 (removes 5), Set: \[ \{1\} \]
- Ben loses, Maria wins this round.

#### Round 3: \( n = 1 \)
- Initial Set: \[ \{1\} \]
- There are no primes for Maria to choose.
- Maria loses, Ben wins this round.

### Conclusion
- Ben wins 2 rounds (for \( n = 4 \) and \( n = 1 \)).
- Maria wins 1 round (for \( n = 5 \)).
- Overall winner is Ben.

