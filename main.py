from clean import cleanData
from extract import extractAverageNumberOfPeopleAtEveryHour
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    originalDataSet: pd.DataFrame = pd.read_csv('./gymDataSet.csv')
    cleanedDataSet: pd.DataFrame = cleanData(originalDataSet)
    averageNumberOfPeopleAtEveryHour: pd.DataFrame = extractAverageNumberOfPeopleAtEveryHour(
        cleanedDataSet
    )

    hour: list[int] = averageNumberOfPeopleAtEveryHour['hour'].tolist()
    numberOfPeople: list[float] = averageNumberOfPeopleAtEveryHour['numberOfPeople'].tolist()

    polynomialCoefficients = np.polyfit(hour, numberOfPeople, 3)
    polynomialFunction = np.poly1d(polynomialCoefficients)

    evenlySpacedHourSamples = np.linspace(hour[0], hour[-1], 100)
    populationBasedOnPolynomial = polynomialFunction(evenlySpacedHourSamples)

    print(f"Polynomial model: \n {polynomialFunction}")

    plt.plot(hour, numberOfPeople, 'o')
    plt.plot(evenlySpacedHourSamples, populationBasedOnPolynomial, label='curve of best fit')
    plt.legend(loc="upper left")
    plt.title('Gym Population VS. Time')
    plt.xlabel('Hour (military time)')
    plt.ylabel('Number of People')

    plt.show()


main()
