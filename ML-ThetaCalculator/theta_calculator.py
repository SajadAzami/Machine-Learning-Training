"""Created by Sajad Azami"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    matrix = np.loadtxt('data.txt', delimiter=',')
    theta_length_3 = [0, 0, 0]
    theta_length_3[0] = find_theta(matrix, 0, 3)[1]
    theta_length_3[1] = find_theta(matrix, 1, 3)[1]
    theta_length_3[2] = find_theta(matrix, 10, 3)[1]

    theta_length_6 = [0, 0, 0]
    theta_length_6[0] = find_theta(matrix, 0, 6)[1]
    theta_length_6[1] = find_theta(matrix, 1, 6)[1]
    theta_length_6[2] = find_theta(matrix, 10, 6)[1]
    print(theta_length_3)
    print(theta_length_6)

    # 4-B Answer
    plt.plot([0, 1, 10], theta_length_3, [0, 1, 10], theta_length_6)
    plt.xlabel('Lambda')
    plt.ylabel('Theta Length (D3 = Blue)(D6 = Green)')
    plt.show()

    # 4-C Answer
    t1 = np.arange(0, 10, 0.01)
    plt.plot(t1, f(t1, find_theta(matrix, 0, 3)[0], 3), 'k', matrix[:, 1], 'ro')
    plt.title('Degree = 3 , Lambda = 0')
    plt.show()

    plt.plot(t1, f(t1, find_theta(matrix, 1, 3)[0], 3), 'k', matrix[:, 1], 'ro')
    plt.title('Degree = 3 , Lambda = 1')
    plt.show()

    plt.plot(t1, f(t1, find_theta(matrix, 10, 3)[0], 3), 'k', matrix[:, 1], 'ro')
    plt.title('Degree = 3 , Lambda = 10')
    plt.show()

    plt.plot(t1, f(t1, find_theta(matrix, 0, 6)[0], 6), 'k', matrix[:, 1], 'ro')
    plt.title('Degree = 6 , Lambda = 0')
    plt.show()

    plt.plot(t1, f(t1, find_theta(matrix, 1, 6)[0], 6), 'k', matrix[:, 1], 'ro')
    plt.title('Degree = 6 , Lambda = 1')
    plt.show()

    plt.plot(t1, f(t1, find_theta(matrix, 10, 6)[0], 6), 'k', matrix[:, 1], 'ro')
    plt.title('Degree = 6 , Lambda = 10')
    plt.show()

    # 4-D Answer
    mse3 = [0, 0, 0]
    mse6 = [0, 0, 0]
    mse3[0] = find_mse(matrix[:, 0], matrix[:, 1], find_theta(matrix, 0, 3)[0], 3)
    mse3[1] = find_mse(matrix[:, 0], matrix[:, 1], find_theta(matrix, 1, 3)[0], 3)
    mse3[2] = find_mse(matrix[:, 0], matrix[:, 1], find_theta(matrix, 10, 3)[0], 3)
    mse6[0] = find_mse(matrix[:, 0], matrix[:, 1], find_theta(matrix, 0, 6)[0], 6)
    mse6[1] = find_mse(matrix[:, 0], matrix[:, 1], find_theta(matrix, 10, 6)[0], 6)
    mse6[2] = find_mse(matrix[:, 0], matrix[:, 1], find_theta(matrix, 10, 6)[0], 6)

    plt.plot(mse3, [0, 1, 10], 'ro')
    plt.title('MSE Error Of Degree 3')
    plt.show()

    plt.plot(mse6, [0, 1, 10], 'ro')
    plt.title('MSE Error Of Degree 6')
    plt.show()


def f(t, theta, degree):
    if degree == 3:
        return theta[0] + t * theta[1] + pow(t, 2) * theta[2] + pow(t, 3) * theta[3]
    if degree == 6:
        return theta[0] + \
               t * theta[1] + \
               pow(t, 2) * theta[2] + \
               pow(t, 3) * theta[3] + \
               pow(t, 4) * theta[4] + \
               pow(t, 5) * theta[5] + \
               pow(t, 6) * theta[6]


def find_mse(x, y, theta, degree):
    if degree == 3:
        sigma = 0
        for i in range(0, 10):
            sigma += pow(((theta[0] + x[i] * theta[1] + pow(x[i], 2) * theta[2] + pow(x[i], 3) * theta[3]) -
                          y[i]), 2)
        return (1.0 / 22.0) * sigma
    if degree == 6:

        sigma = 0
        for i in range(0, 10):
            sigma += pow(((theta[0] +
                           x[i] * theta[1] +
                           pow(x[i], 2) * theta[2] +
                           pow(x[i], 3) * theta[3] +
                           pow(x[i], 4) * theta[4] +
                           pow(x[i], 5) * theta[5] +
                           pow(x[i], 6) * theta[6]) - y[i]), 2)
        return (1.0 / 22.0) * sigma


# Find theta matrix for matrix of data, lambda_val and degree of equation with normal method
def find_theta(data, lambda_val, degree):
    x = data[:, 0]
    x = np.reshape(x, (11, 1))
    ones = np.ones((11, 1))
    powers2 = np.power(x, 2)
    powers3 = np.power(x, 3)
    powers4 = np.power(x, 4)
    powers5 = np.power(x, 5)
    powers6 = np.power(x, 6)

    if degree == 3:
        x = np.concatenate((ones, x), axis=1)
        x = np.concatenate((x, powers2, powers3), axis=1)
    if degree == 6:
        x = np.concatenate((ones, x), axis=1)
        x = np.concatenate((x, powers2, powers3, powers4, powers5, powers6), axis=1)

    y = data[:, 1]

    identity = np.identity(degree + 1)
    identity[0, 0] = 0
    theta = np.dot((np.linalg.inv((x.T.dot(x)) + (lambda_val * identity))), np.dot(x.T, y))
    length = np.linalg.norm(theta)

    print('For degree of {} and lambda value of {}, theta matrix is {}\nVector length of theta is :{}\n'
          .format(degree, lambda_val, theta, length))
    return theta, length


if __name__ == "__main__":
    main()
