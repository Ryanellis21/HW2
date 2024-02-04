import math


def Probability(PDF, args, c, GT=True):
    mu, sigma = args

    def simpsons_13_rule(a, b, n):
        h = (b - a) / n
        x = a
        integral = 0

        for i in range(n + 1):
            if i == 0 or i == n:
                weight = 1
            elif i % 2 == 1:
                weight = 4
            else:
                weight = 2

            integral += weight * PDF((x, mu, sigma))
            x += h

        integral *= h / 3
        return integral

    if GT:
        lower_limit = mu - 5 * sigma
        probability = simpsons_13_rule(lower_limit, c, 1000)
    else:
        probability = 1 - simpsons_13_rule(mu - 5 * sigma, c, 1000)

    return probability


def PDF_gaussian(args):
    x, mu, sigma = args
    exponent = -(x - mu) ** 2 / (2 * sigma ** 2)
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(exponent)


def main():
    # P(x < 105 | N(100, 12.5))
    probability_1 = Probability(PDF_gaussian, (100, 12.5), 105, GT=False)

    # P(x > μ + 2σ | N(100, 3))
    probability_2 = Probability(PDF_gaussian, (100, 3), 100 + 2 * 3, GT=True)

    print(f"P(x < 105 | N(100, 12.5)) = {probability_1:.2f}")
    print(f"P(x > μ + 2σ | N(100, 3)) = {probability_2:.2f}")


if __name__ == "__main__":
    main()