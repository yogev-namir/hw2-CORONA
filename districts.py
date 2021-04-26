class District:
    def __init__(self, dataset):
        self.dataset = dataset

    def filter_districts(self, letters):
        # only those how starts with the letters L or S
        names = self.dataset.get_all_districts()
        desired_districts = []
        for name in names:
            if name[0] in letters:
                desired_districts.append(name)
        self.dataset.set_districts_data(desired_districts)
        # print(self.dataset['denominazione_region'])

    def print_details(self, features, statistic_functions):
        outputs = []
        for feature in features:
            for function in statistic_functions:
                output = function(self.dataset[feature])
                outputs.append(str(output))
            print(f'{feature}: ' + ', '.join(outputs))
            outputs.clear()

    def determine_day_type(self):
        # day_type = []
        day_type = {'day_type': []}
        for new, resigned in zip(self.dataset['new_positives'], self.dataset['resigned_healed']):
            difference = resigned - new
            if difference > 0:
                # day_type.append(1)
                day_type['day_type'].append(1)
            else:
                # day_type.append(0)
                day_type['day_type'].append(0)
        # self.dataset.update(**{"day_type": day_type})
        self.dataset.update(**day_type)
        # print(self.dataset['day_type'])
        return self.dataset


    def get_districts_class(self):
        good_days_count = [0] * 21
        for i, record in enumerate(self.dataset.__getitem__('day_type')):
            if record:
                good_days_count[i % 21] += 1
        districts_names = self.dataset.get_all_districts()
        green_or_not = []
        for count in good_days_count:
            if count > 340:
                green_or_not.append('green')
            else:
                green_or_not.append('not green')
        districts = dict(zip(districts_names, green_or_not))
        return districts


    def keys(self):
        return self.dataset.keys()

    def values(self):
        return self.dataset.values()

    def __getitem__(self, key):
        if key in self.dataset:
            return self.dataset[key]
        if hasattr(self.__class__, "__missing__"):
            return self.__class__.__missing__(self, key)