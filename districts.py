import pandas
from data import Data


class District:
    def __init__(self, dataset):
        self.dataset = dataset

    def filter_districts(self, letters):
        self.dataset = self.dataset.set_districts_data(letters)


    def print_details(self, features, statistic_functions):
        outputs = []
        for feature in features:
            for function in statistic_functions:
                output = function(self.dataset.get(feature))
                outputs.append(str(output))
            print(f'{feature}: ' + ', '.join(outputs))


    def determine_day_type(self):
        self.dataset['day_type'] = []
        for i, (new, resigned) in enumerate(
                zip(self.dataset.get('new_positives'), self.dataset.get('resigned_healed'))):
            day_type = resigned - new
            if day_type > 0:
                self.dataset['day_type'].append(1)
            else:
                self.dataset['day_type'].append(0)
        return self.dataset


    def get_districts_class(self):
        good_days_count = [0] * 21
        for i, record in enumerate(self.dataset.get('day_type')):
            if self.dataset.get('day_type')[i]:
                good_days_count[i % 21] += 1

        districts_names = self.Data.get_all_districts(self.dataset)
        districts = dict(zip(districts_names, good_days_count))
        for i,count in enumerate(districts.values()):
            if count > 340:
                districts[i][count]='green'
            else:
                districts[i][count]='not green'
        return districts