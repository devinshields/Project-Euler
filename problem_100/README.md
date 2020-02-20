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
I don't have a strong hunch as to an analytical solution, but all the neurons
I've trained to recognize integer sequences are signaling at maximum frequency.

The valid value sequences for `n` and `b` (shown above) are:

* `n: 4, 21, 120, 697, 4060, 23661, 137904, 803761, 4684660, 27304197`
* `b: 3, 15, 85, 493, 2871, 16731, 97513, 568345, 3312555, 19306983`


A [search at oeis.org](https://oeis.org/search?q=4%2C+21%2C+120%2C+697%2C+4060%2C+23661%2C+137904%2C+803761%2C+4684660%2C+27304197&language=english&go=Search) for valid values of `n` returns...


## A Hit, Captain!

![image](https://user-images.githubusercontent.com/1356969/74901283-6427e480-5370-11ea-8db7-ba688a4bacdc.png)



### the solution


* assuming the only thing needed to generate a valid solution is [integer sequence `A046090`](https://oeis.org/A046090):


```
>>> from solve_100 import blue_disks, prob_of_bb
>>> 
>>> n_candidates = [4, 21, 120, 697, 4060, 23661, 137904, 803761, 4684660, 27304197, 159140520, 927538921, 5406093004, 31509019101, 183648021600, 1070379110497, 6238626641380, 36361380737781, 211929657785304, 1235216565974041]
>>> 
>>> for n in n_candidates:
...     b = blue_disks(n)
...     if (prob_of_bb(n, b) == .5) and (n >= 10**12):
...         print('Project Euler Problem #100 Solution: {} blue disks'.format(b))
...         break
... 
Project Euler Problem #100 Solution: 756872327473 blue disks
```

### Bingo. and Rats

* Apparently this is the hardest Project Euler problem-solution you're allowed to share publicly without breaking the rules :-( . Thanks for reading!

![image](https://user-images.githubusercontent.com/1356969/74902176-3e500f00-5373-11ea-8f02-70cad29fb719.png)











