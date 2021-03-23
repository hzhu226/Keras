import random
import math

def get_dataset():
    dataset = []
    dataset.append([1855, 118])
    dataset.append([1856, 151])
    dataset.append([1857, 121])
    dataset.append([1858, 96])
    dataset.append([1859, 110])
    dataset.append([1860, 117])
    dataset.append([1861, 132])
    dataset.append([1862, 104])
    dataset.append([1863, 125])
    dataset.append([1864, 118])
    dataset.append([1865, 125])
    dataset.append([1866, 123])
    dataset.append([1867, 110])
    dataset.append([1868, 127])
    dataset.append([1869, 131])
    dataset.append([1870, 99])
    dataset.append([1871, 126])
    dataset.append([1872, 144])
    dataset.append([1873, 136])
    dataset.append([1874, 126])
    dataset.append([1875, 91])
    dataset.append([1876, 130])
    dataset.append([1877, 62])
    dataset.append([1878, 112])
    dataset.append([1879, 99])
    dataset.append([1880, 161])
    dataset.append([1881, 78])
    dataset.append([1882, 124])
    dataset.append([1883, 119])
    dataset.append([1884, 124])
    dataset.append([1885, 128])
    dataset.append([1886, 131])
    dataset.append([1887, 113])
    dataset.append([1888, 88])
    dataset.append([1889, 75])
    dataset.append([1890, 111])
    dataset.append([1891, 97])
    dataset.append([1892, 112])
    dataset.append([1893, 101])
    dataset.append([1894, 101])
    dataset.append([1895, 91])
    dataset.append([1896, 110])
    dataset.append([1897, 100])
    dataset.append([1898, 130])
    dataset.append([1899, 111])
    dataset.append([1900, 107])
    dataset.append([1901, 105])
    dataset.append([1902, 89])
    dataset.append([1903, 126])
    dataset.append([1904, 108])
    dataset.append([1905, 97])
    dataset.append([1906, 94])
    dataset.append([1907, 83])
    dataset.append([1908, 106])
    dataset.append([1909, 98])
    dataset.append([1910, 101])
    dataset.append([1911, 108])
    dataset.append([1912, 99])
    dataset.append([1913, 88])
    dataset.append([1914, 115])
    dataset.append([1915, 102])
    dataset.append([1916, 116])
    dataset.append([1917, 115])
    dataset.append([1918, 82])
    dataset.append([1919, 110])
    dataset.append([1920, 81])
    dataset.append([1921, 96])
    dataset.append([1922, 125])
    dataset.append([1923, 104])
    dataset.append([1924, 105])
    dataset.append([1925, 124])
    dataset.append([1926, 103])
    dataset.append([1927, 106])
    dataset.append([1928, 96])
    dataset.append([1929, 107])
    dataset.append([1930, 98])
    dataset.append([1931, 65])
    dataset.append([1932, 115])
    dataset.append([1933, 91])
    dataset.append([1934, 94])
    dataset.append([1935, 101])
    dataset.append([1936, 121])
    dataset.append([1937, 105])
    dataset.append([1938, 97])
    dataset.append([1939, 105])
    dataset.append([1940, 96])
    dataset.append([1941, 82])
    dataset.append([1942, 116])
    dataset.append([1943, 114])
    dataset.append([1944, 92])
    dataset.append([1945, 98])
    dataset.append([1946, 101])
    dataset.append([1947, 104])
    dataset.append([1948, 96])
    dataset.append([1949, 109])
    dataset.append([1950, 122])
    dataset.append([1951, 114])
    dataset.append([1952, 81])
    dataset.append([1953, 85])
    dataset.append([1954, 92])
    dataset.append([1955, 114])
    dataset.append([1956, 111])
    dataset.append([1957, 95])
    dataset.append([1958, 126])
    dataset.append([1959, 105])
    dataset.append([1960, 108])
    dataset.append([1961, 117])
    dataset.append([1962, 112])
    dataset.append([1963, 113])
    dataset.append([1964, 120])
    dataset.append([1965, 65])
    dataset.append([1966, 98])
    dataset.append([1967, 91])
    dataset.append([1968, 108])
    dataset.append([1969, 113])
    dataset.append([1970, 110])
    dataset.append([1971, 105])
    dataset.append([1972, 97])
    dataset.append([1973, 105])
    dataset.append([1974, 107])
    dataset.append([1975, 88])
    dataset.append([1976, 115])
    dataset.append([1977, 123])
    dataset.append([1978, 118])
    dataset.append([1979, 99])
    dataset.append([1980, 93])
    dataset.append([1981, 96])
    dataset.append([1982, 54])
    dataset.append([1983, 111])
    dataset.append([1984, 85])
    dataset.append([1985, 107])
    dataset.append([1986, 89])
    dataset.append([1987, 87])
    dataset.append([1988, 97])
    dataset.append([1989, 93])
    dataset.append([1990, 88])
    dataset.append([1991, 99])
    dataset.append([1992, 108])
    dataset.append([1993, 94])
    dataset.append([1994, 74])
    dataset.append([1995, 119])
    dataset.append([1996, 102])
    dataset.append([1997, 47])
    dataset.append([1998, 82])
    dataset.append([1999, 53])
    dataset.append([2000, 115])
    dataset.append([2001, 21])
    dataset.append([2002, 89])
    dataset.append([2003, 80])
    dataset.append([2004, 101])
    dataset.append([2005, 95])
    dataset.append([2006, 66])
    dataset.append([2007, 106])
    dataset.append([2008, 97])
    dataset.append([2009, 87])
    dataset.append([2010, 109])
    dataset.append([2011, 57])
    dataset.append([2012, 87])
    dataset.append([2013, 117])
    dataset.append([2014, 91])
    dataset.append([2015, 62])
    dataset.append([2016, 65])
    dataset.append([2017, 94])
    dataset.append([2018, 86])
    dataset.append([2019, 70])
    return dataset

def print_stats(dataset):
    dataset = get_dataset()
    sum = 0
    inner = 0
    for i in range(len(dataset)):
        sum = sum + dataset[i][1]
    mean = sum / len(dataset)
    for i in range(len(dataset)):
        inner = inner + (dataset[i][1] - mean) ** 2
    standard_deviation = math.sqrt(inner / len(dataset) - 1)

    print(len(dataset))
    print('{:.2f}'.format(mean))
    print('{:.2f}'.format(standard_deviation))

def regression(beta_0, beta_1, dataset=get_dataset()):
    MSE = 0
    for x, y in dataset:
        f = beta_0 + (beta_1 * x)
        MSE = (f - y) * (f - y) + MSE
    MSE = MSE / len(dataset)
    return MSE

def gradient_descent(beta_0, beta_1, dataset=get_dataset()):
    partial_1 = 0
    for x, y in dataset:
        partial_1 = beta_0 + (beta_1 * x) - y + partial_1
    partial_1 = (2 * partial_1) / len(dataset)

    partial_2 = 0
    for x, y in dataset:
        partial_2 = (beta_0 + (beta_1 * x) - y) * x + partial_2
    partial_2 = (2 * partial_2) / len(dataset)

    return (partial_1, partial_2)

def iterate_gradient(T, eta, dataset=get_dataset()):
    beta_0 = 0
    beta_1 = 0

    for i in range(0, T):
        partial_1, partial_2 = gradient_descent(beta_0, beta_1, dataset)
        beta_0 = beta_0 - eta * partial_1
        beta_1 = beta_1 - eta * partial_2
        MSE = regression(beta_0, beta_1, dataset)
        print('{} {:.2f} {:.2f} {:.2f}'.format(i+1, beta_0, beta_1, MSE))

def compute_betas():
    dataset = get_dataset()
    sum_x = 0
    for i in range(len(dataset)):
        sum_x = sum_x + dataset[i][0]
    mean_x = sum_x / len(dataset)
    sum_y = 0
    for i in range(len(dataset)):
        sum_y = sum_y + dataset[i][1]
    mean_y = sum_y / len(dataset)

    sum_up = 0
    sum_down = 0
    for x, y in dataset:
        sum_up = sum_up + (x - mean_x) * (y - mean_y)
        sum_down = sum_down + (x - mean_x) * (x - mean_x)
    beta_1 = sum_up / sum_down
    beta_0 = mean_y - beta_1 * mean_x
    MSE = regression(beta_0, beta_1)

    return (beta_0, beta_1, MSE)

def predict(year):
    beta_0, beta_1, MSE = compute_betas()
    prediction = beta_0 + (beta_1 * year)
    return prediction

def iterate_normalized(T, eta):
    dataset = get_dataset()
    sum = 0
    inner = 0
    for i in range(len(dataset)):
        sum = sum + dataset[i][0]
    mean = sum / len(dataset)
    for i in range(len(dataset)):
        inner = inner + (dataset[i][0] - mean) ** 2
    standard_deviation = math.sqrt(inner / len(dataset) - 1)

    normalized = []
    for i in range(len(dataset)):
        normalized_x = (dataset[i][0] - mean) / standard_deviation
        normalized.append([normalized_x, dataset[i][1]])
    iterate_gradient(T, eta, dataset=normalized)

def sgd(T, eta):
    dataset = get_dataset()
    sum = 0
    inner = 0
    for i in range(len(dataset)):
        sum = sum + dataset[i][0]
    mean = sum / len(dataset)
    for i in range(len(dataset)):
        inner = inner + (dataset[i][0] - mean) ** 2
    standard_deviation = math.sqrt(inner / len(dataset) - 1)
    normalized = []
    for i in range(len(dataset)):
        normalized_x = (dataset[i][0] - mean) / standard_deviation
        normalized.append([normalized_x, dataset[i][1]])

    beta_0 = 0
    beta_1 = 0
    for i in range(0, T):
        j = random.choice(normalized)
        gradient_1 = 2 * (beta_0 + beta_1 * j[0] - j[1])
        gradient_2 = gradient_1 * j[0]
        beta_0 = beta_0 - eta * gradient_1
        beta_1 = beta_1 - eta * gradient_2
        MSE = regression(beta_0, beta_1, dataset=normalized)
        print('{} {:.2f} {:.2f} {:.2f}'.format(i+1, beta_0, beta_1, MSE))
