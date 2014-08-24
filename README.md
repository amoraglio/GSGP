
TINY_GSGP.py: 
=============

A Tiny and Efficient Implementation of Geometric Semantic Genetic Programming Using Higher-Order Functions and Memoization

Author: Alberto Moraglio (albmor@gmail.com) 

Features:

- Individuals are represented directly as Python (anonymous) functions.

- Crossover and mutation are higher-order functions.

- Offspring functions call parent functions rather than embed their definitions (no grwoth, implicit ancestry trace).

- Memoization of individuals turns time complexity of fitness evalutation from exponential to constant.

- The final solution is a compiled function. It can be extracted using the ancestry trace to reconstruct its 'source code'. 

This implementation is to evolve Boolean expressions. It can be easily adapted to evolve arithmetic expressions or classifiers.

TINY_GSGP.nb: 
=============

A Tiny Implementation of Geometric Semantic Genetic Programming in Mathematica Using Algebraic Simplification.

Author: Alberto Moraglio (albmor@gmail.com)

This is a reimplementation of TINY_GSGP.py in Mathematica to compare the effect of simplification of offsrping. 

Features:

- Individuals are represented using symbolic expressions (Boolean expressions).

- Uniform initialisation/generation of random expressions.

- Crossover and mutation embed parent expressions in the offspring expression.

- Algebraic simplification of offspring prevents exponential growth.

- The final solution is short and understandable (no black-box).

