# Statistics and graphics for friendly football betting

In my family we have a tradition of doing a friendly bet whenever there is a football (soccer) cup.

The rules are simple; prior to the group stage everyone:

  * Guess the outcome and scoreline for each game in the group stage
  * Guess the final cup winner

For each correctly guessed outcome (home team won/tie/away team won) you are awarded `1` point, if you also guessed the correct scoreline then you are awarded another `3` points.

## Data files

Only thing needed is a `.csv`-file, with the following columns:

| Day | Result |  A  |  B  | ... |
|:---:|:------:|:---:|:---:|:---:|
|  1  | 1-0    | 0-0 | 1-0 | ... |
|  2  | 2-3    | 1-2 | 2-0 | ... |
|  3  | 4-0    | 4-0 | 1-1 | ... |
| ... | ...    | ... | ... | ... |


## Accuracy distribution

To compute the accuracy I used the simplest distribution I could come up with:

$$acc(x_1,x_2,y_1,y_2) = \left(\frac{1}{1 + |x_1-y_1|}\right)\left(\frac{1}{1 + |x_2-y_2|}\right)$$

... where "$x_1$-$x_2$" is the guessed scoreline and "$y_1$-$y_2$" is the actual result.

A distribution is used instead of ratios because:

  * Zero-scores results in zero accuracy or divide-by-zero
  * A difference in a smaller scoreline gives a worse ratio than a similar difference in a larger scoreline
