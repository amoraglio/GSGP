
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

TINY_GSHCGP.py: 
===============

An Implementation of Geometric Semantic *Hill Climber* Genetic Programming Using Higher-Order Functions and Memoization

Author: Alberto Moraglio (albmor@gmail.com)

Features:

- Same as TINY_GSGP.py, substituting the evolutionary algorithm with a hill-climber.

- The fitness landscape seen by Geometric Semantic operators is always unimodal. A hill climber can reach the optimum.

- Offspring functions call parent functions rather than embed their definitions (no grwoth, implicit ancestry trace).

- Even if offspring functions embedded parent function definition, the growth is linear in the number of generation (not exponential as with crossover). 

- Memoization of individuals turns time complexity of fitness evalutation from linear to constant (not exponential to constant as with crossover).

- Implicit ancestry trace and memoization not strictly necessary with hill-climber for efficent implementation.

- The final solution is a compiled function. It can be extracted using the ancestry trace to reconstruct its 'source code'. 

This implementation is to evolve Boolean expressions. It can be easily adapted to evolve arithmetic expressions or classifiers.

TINY_GSHCGP.nb:
===============

An Implementation of Geometric Semantic *Hill Climber* Genetic Programming in Mathematica Using Algebraic Simplification.

Author: Alberto Moraglio (albmor@gmail.com)

Features:

- The fitness landscape seen by Geometric Semantic operators is always unimodal. A hill-climber can reach the optimum.

- Mutation embeds parent expression in the offspring expression.

- Algebraic simplification of offspring.

- Offspring size growth without simplification is linear in the number of generation (simplification is not strictly needed for space efficiency).

- Final solution short and understandable.

TINY_GSHCGP _ARIT.nb: 
=====================

Geometric Semantic Hill Climber Genetic Programming in Mathematica for *Arithmetic Expressions*.

Author: Alberto Moraglio (albmor@gmail.com)

Features:

- It searches the space of arithmentic expressions (polynomials or fractional polynomials if division is used).

- Fithess is based on a training set (not on all inputs as for Boolean expressions). 

- Algebraic simplification of offspring.

- Generalisation test (on unseen examples).

TINY_GSGP _ARIT.nb: 
===================

Geometric Semantic Genetic Programming in Mathematica for *Arithmetic Expressions*.

Author: Alberto Moraglio (albmor@gmail.com)

Features:

- It evolves arithmentic expressions (polynomials or fractional polynomials if division is used).

- Fithess is based on a training set (not on all inputs as for Boolean expressions).

- Algebraic simplification of offspring.

- Generalisation test (on unseen examples).
 

