# Matrix Gauss Elimination Solver (with Partial Pivoting)

## Aim
To solve a system of $N \times N$ linear equations $Ax = b$ using Gaussian Elimination with partial pivoting and back substitution.

## Theory
Gaussian elimination is a direct method for solving systems of linear equations. It operates in two major phases:
1. **Forward Elimination**: Converts the system into an upper triangular matrix ($Ux = y$). To maintain numerical stability and avoid division by zero or very small numbers, **Partial Pivoting** is employed:
   - At each step $i$, the algorithm searches for the row with the largest absolute value in the pivot column $i$ (from row $i$ to $N$).
   - It swaps that row with the current row $i$ to ensure the pivot element $A[i, i]$ is as large as possible.
2. **Back Substitution**: Solves the triangular system starting from the bottom ($x_N$) up to the top ($x_1$).

## File Structure
- `Matrix Gauss Elimination.py` - The primary solver featuring stepwise printouts of pivoting and elimination steps.
- `v0.py` - An alternative/simplified version of the Gauss Elimination algorithm.
- `output.txt` - Step-by-step printed output logs showing intermediate augmented matrices.

## How to Run
Ensure you have Python 3 and NumPy installed:
```bash
pip install numpy
python "Matrix Gauss Elimination.py"
```

### Input Format
- Enter the matrix size $N$ (e.g., `3`).
- Enter the elements of matrix $A$ row-by-row (e.g., `2 1 -1`).
- Enter the $N$ elements of vector $b$ space-separated.
