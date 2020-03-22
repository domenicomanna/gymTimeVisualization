import pandas as pd


def extractAverageNumberOfPeopleAtEveryHour(gymDataFrame: pd.DataFrame) -> pd.DataFrame:
    averageNumberOfPeopleAtEveryHour = gymDataFrame.groupby(['hour'], as_index=True).agg(
        numberOfPeople=('number_people', 'mean')
    ).reset_index()
    return averageNumberOfPeopleAtEveryHour
