import numpy as np


# Defining the function GaussSiedel

def GaussSiedel(Aug, x, Niter=15):


# Getting the shape of Aug

    (m, n) = Aug.shape

# Initialising x0

    x0 = np.empty(shape=n - 1)

    for i in range(n - 1):

        x0[i] = x[i]

# Getting the matrix a and b from Aug

    a = Aug[:m, :n - 1]

    b = Aug[:m, n - 1].reshape(m)

# Defining new value of n

    (m, n) = a.shape

# Initialising the solution

    x = np.zeros(shape=n)

# Initialising the iteration number

    k = 1

    while k <= Niter:

        for i in range(n):

            s = 0

            for j in range(i):

                if (i == j):

                    continue

                else:

                    s += a[i][j] * x[j]

            for j in range(i + 1, n):

                if (i == j):

                    continue

                else:

                    s += a[i][j] * x0[j]

            x[i] = (-s + b[i]) / (a[i][i])

# Updating the number of iterations

        k += 1

# Updating the parameters

        for i in range(n):

            x0[i] = x[i]

# Returning the solution
    return x

# Writing the main function

if __name__ == "__main__":

# Part (i)


# Defining the Aug matrix

    Aug = np.array([[3, 1, -1, 2], [1, 4, 1, 12], [2, 1, 2, 10]])

# Defining intial x

    x = np.zeros(shape=Aug.shape[0])

# calling the function

    x = GaussSiedel(Aug, x)

# Displaying the solution

    print("Solution of Part (i) is ")

    print(x)

# Part (ii)

# Defining the Aug matrix

    Aug = np.array([[9, 2, 3, 4, 21], [1, -10, 2, 4, 2], [-1, 2, 7, 3, 37],[3, 1, 4, 12, 12]])

# Defining intial x

    x = np.zeros(shape=Aug.shape[0])

# calling the function

    x = GaussSiedel(Aug, x)

# Displaying the solution

    print("\nSolution of Part (ii) is ")

    print(x)