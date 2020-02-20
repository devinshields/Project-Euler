## Project Euler, [Problem #100](https://projecteuler.net/problem=100)


### Arranged Probability


> If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.
> 
> The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.
>
> By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.



### definitions

* `n` - the total number of disks in the box
* `b` - blue disks in the box

* probability of drawing two blue disks:

```
P(BB) = (b / n) * ((b - 1) / (n - 1))
```


### solution strategy, part 1 (brute force):


* inspecting numeric values for each probability:

```
>>> 15/21
0.7142857142857143
>>> 14/20
0.7
```

* both are adjacent to (± a small delta) square root of 1/2 (obviously):

```
>>> 2**-.5
0.7071067811865476
```

Given a candidate value of `n`, the value of `b` that minimizes
`abs( P(BB) - 1/2 )` is:

```
b = int(n*2** - .5) + 1
```


So a brute force solution would look like:

```
for all values of n
    calculate b
    calculate P(BB)
    if ( P(BB) exactly equals 1/2 ) and (b >= 10**12)
        print(b)
        exit
```


### 1st roadblock: numerical precision error

* a naive implementation of `prob_of_bb(n, b)` fails its test cases:


```
def blue_disks(n):
    return int(n*2** - .5) + 1

def test_blue_disks():
    assert 15 == blue_disks(21)
    assert 85 == blue_disks(120)

def prob_of_bb(n, b):
    return (b / n) * ((b - 1) / (n - 1))

def test_prob_of_bb():
    assert .5 == prob_of_bb(21, 15)
    assert .5 == prob_of_bb(120, 85)
```

* as written, `prob_of_bb(n, b)` uses two `divide` and one `multiply` operations
* these extra operations return a rounding error:


```
>>> prob_of_bb(120, 85)
0.5000000000000001
```

* can we fix it by using fewer non-integer operations / a little algebra?
  * yes we can.

```
>>> def prob_of_bb(n, b):
...     return (b**2 - b) / (n**2 - n)
... 
>>> prob_of_bb(120, 85)
0.5
```


### 2nd roadblock: brute force isn't fast enough


* iterating over all candidate values of `n`,
* a simple `for` loop can test between 10^7 and 10^8 values
* in the [60 second window](https://projecteuler.net/about) for viable solutions


> ...an efficient implementation will allow a solution to be obtained on a modestly powered computer in less than one minute


```
(euler) localhost:problem_100 devinshields$ ./solve_100.py 
n: 4, b: 3, p: 0.5
n: 21, b: 15, p: 0.5
n: 120, b: 85, p: 0.5
n: 697, b: 493, p: 0.5
n: 4060, b: 2871, p: 0.5
n: 23661, b: 16731, p: 0.5
n: 137904, b: 97513, p: 0.5
n: 803761, b: 568345, p: 0.5
n: 4684660, b: 3312555, p: 0.5
n: 27304197, b: 19306983, p: 0.5
brute force solution up to max_n: 10**8, took: 77 seconds
```

<br/>


![must go faster](https://media1.giphy.com/media/7XsFGzfP6WmC4/giphy.gif)


<br/>


### solution strategy, part 2 (clever / efficient):


We're now quite sure that a guess-and-check strategy isn't viable for `n` >= 10^7.
Given prior experience with Project Euler, this problem is firing all my neurons
connected to the [On-Line Encyclopedia of Integer Sequences](https://oeis.org/).

The solution sequence above for `n` and `b` are:

* `n: `


















