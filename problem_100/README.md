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
P(BB) = (b / n) * ((b-1) / (n - 1))
```


### solution strategy part 1 - brute force:


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

Given a candidate value of `n`, th
