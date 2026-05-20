import numpy as np

def print_step(matrix, step_name):
    print(f"\n{step_name}")
    for row in matrix:
        # Formats the augmented matrix with a bar | for the vector b
        matrix_part = "  ".join(f"{val:8.4f}" for val in row[:-1])
        result_part = f"{row[-1]:8.4f}"
        print(f"[ {matrix_part} | {result_part} ]")

def gauss_elimination(A, b):
    n = len(b)
    # Augment matrix A with vector b
    Ab = np.hstack([A.astype(float), b.astype(float).reshape(-1, 1)])

    print_step(Ab, "Initial Augmented Matrix")

    # Forward Elimination
    for i in range(n):
        # 1. Partial Pivoting
        max_row = i + np.argmax(np.abs(Ab[i:n, i]))
        
        if Ab[max_row, i] == 0:
            raise ValueError("Matrix is singular and cannot be solved.")
        
        if max_row != i: 
            Ab[[i, max_row]] = Ab[[max_row, i]]
            print_step(Ab, f"Step: Swapped Row {i+1} with Row {max_row+1} (Pivoting)")

        # 2. Elimination
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]
            print(f"\nEliminating Row {j+1}: Multiplier (m) = {Ab[j,i]} / {Ab[i,i]} = {factor:.4f}")
            print_step(Ab, f"Matrix after eliminating Column {i+1}, Row {j+1}")
            
    print("\nForward Elimination complete. Final Upper Triangular Matrix reached.")

    # 3. Back Substitution
    print("\nStarting Back Substitution")
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        # Calculation display for clarity
        sum_val = np.dot(Ab[i, i+1:n], x[i+1:n])
        x[i] = (Ab[i, -1] - sum_val) / Ab[i, i]
        print(f"Calculating x{i+1}: ({Ab[i, -1]:.4f} - {sum_val:.4f}) / {Ab[i, i]:.4f} = {x[i]:.4f}")
        
    return x

def main():
    print("NxN Matrix")
    try:
        n = int(input("Enter the size of the matrix (N): "))
        
        print(f"Enter the elements of the {n}x{n} matrix A:")
        A_data = []
        for i in range(n):
            row = list(map(float, input(f"Row {i+1}: ").split()))
            A_data.append(row)
        A = np.array(A_data)

        print(f"Enter the {n} elements of vector b:")
        b = np.array(list(map(float, input().split())))

        solution = gauss_elimination(A, b)
        
        print("\n")
        print("Final Solution:")
        for i, val in enumerate(solution):
            print(f"x{i+1} = {val:.4f}")
        print("\n")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
