# Quantum-inspired Tabu Search (QTS)

Quantum-inspired Tabu Search(QTS) is a metaheuristic algorithm which design was inspired by quantum characteristics. Quantum superposition is a fundamental principle which describes the ability of quantum system to be in multiple states before it was measured, while the chances of collapsing into one state when measured is the probability of each of the several eigenstates. In QTS, it shares the same mechanism, which each bit in the solution of the algorithm can be in, chosen or not chosen, 2 eigenstate. Whereas the sum of probability of the two states is 1.

## Beta-Matrix

Beta matrix is a matrix that holds the probability of every bit of solution. Every bit has only one value, which in this series of code, is the probability to be chosen. As each bit in solution only has 2 states, to calculate the probability the bit not to be chosen, simply minus the probability of chosen from 1.

## Best Solution

1. Current Best Solution: <br>
   In QTS, NQTS and ANQTS, the beta matrix is updated using current best solution, which is the best solution in each generation. However, there is a defect when update using the current best solution, that is, the algorithm converges slowly. In other words, the beta might be updated to different direction when current best solution is used. For example, in one generation, the current best known solution includes kth bit, but the next generation did not and the following generation includes again. In this situation, the probability of kth bit is not updated towards the required direction, it instead jumping forward and backward around the initial probability.
   
2. Global Best Solution: <br>
   In GQTS, GNQTS and ANGQTS, the beta matrix is updated using the global best solution or the current best known solution. In this case, the algorithm could efficiently updated towards the direction of current best known solution or the global best solution without drifting around.

Depends on the convergence need in every task, the best solution should be choose.

## Not Gate
Quantum not gate is a fundamental quantum feature. It is used to flip the probability of any bit when the probability in beta matrix is not consistent as the best solution. In other words, to avoid the algorithm stuck at local minima. 

Let’s explain this using an example. The best solution in all previous generation assumes that a good solution includes kth bit, which means a lot of previous generation’s solution prefer kth bit to be choose, and the probability of kth is updated to very high now. But in current generation, the algorithm finds that it is better not to include kth bit. In ordinary situation, the algorithm update the probability a step each generation, which takes a lot generation to get to low chosen probability of kth bit. 

To let the algorithm efficiently update the probability from chosen to not chosen or vice versa, here comes the not gate. The not gate minus the current probability from 1 to get the opposite probability, which takes only one generation.

## Adaptive angle
Adaptive angle is a feature to use different update step’s sizes according to the value of the beta-matrix. The adaptive angle is integrated in ANQTS and ANGQTS. The purpose of this design is to give the algorithm the ability to explore for potential solution when the probability to choose each stock or not is similar; and to precisely probe around the possible solution when the algorithm already have preferred solution. The adaptive angle, of course, is bounded in a range, which could be defined by user, or upper bounded to 0.00125 and lower bounded to 0.00045.

<br>

# Installation Guide
This is an unpublished package, the installation, therefore is different from installing a published package.

1. (Optional) **Create and activate virtual environment** <br>
It is always a good practice to create a virtual environment for a Python projects. As Python virtual environments give you the ability to isolate your Python development projects from your system installed Python and other Python environments, in order words, easier to manage between projects.  <br>
i. Create a project folder where you want your virtual environment to be. <br>
ii. Navigate to the project folder in terminal using cd.
```python
   > cd /path_to_project_folder/project_folder
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iii. Install python package for virtual environment: <br>
 ```python
    > pip install venv
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iv. Create virtual environment: <br>
```python
   > python -m venv virtual_environment_name
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iv. Activate virtual environment:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; For Windows:
```python
   > virtual_environment_name\Scripts\activate
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; For Linux:
```python
   > source virtual_environment_name/bin/activate
```
2. **Install QTS package** <br>
i. Download and unzip QTS package to your local computer. <br>
ii. In your virtual environment, navigate to downloaded QTS folder.
```python
   (virtual_environment_name) > cd path/to/QTS-master
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; iii. Install wheel.
```python
   (virtual_environment_name) > pip install wheel
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; iv. Install QTS package.
```python
  (virtual_environment_name) > pip install .
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; v. Test installation
```python
   (virtual_environment_name) > python
   >>> from QTS.GNQTS import GNQTS #if no error, the installation is successful
```
<br>
