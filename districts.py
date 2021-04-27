class District:
    def __init__(self, dataset):
        self.dataset = dataset

    def filter_districts(self, letters):
        """
        fetch only districts that starts with first letters {L,S}
        :param letters: a set of letters
        :return: dictionary with the desire districts in the "denominazione_region" key
        """
        names = self.dataset.get_all_districts()
        desired_districts = []
        for name in names:
            if name[0] in letters:
                desired_districts.append(name)
        self.dataset.set_districts_data(desired_districts)

    def print_details(self, features, statistic_functions):
        """
        prints mean and median measures of the desire features
        :param features: a list of strings
        :param statistic_functions: a list of methods
        :return: prints the statistics methods output of each feature
        """
        outputs = []
        for feature in features:
            for function in statistic_functions:
                output = function(self.dataset[feature])
                outputs.append(str(output))
            print(f'{feature}: ' + ', '.join(outputs))
            outputs.clear()

    def determine_day_type(self):
        """
        appends a binary key to the dictionary. zero for "not green" day and one for "green"
        :return: the self dictionary with the new "day_type" key added
        """
        day_type_values = []
        for new, resigned in zip(self.dataset['new_positives'], self.dataset['resigned_healed']):
            difference = resigned - new  # good if positive, bad if negative
            if difference > 0:
                day_type_values.append(1)
            else:
                day_type_values.append(0)
        self.dataset["day_type"] = day_type_values  # appends the new key to the dictionary
        return self.dataset

    def get_districts_class(self):
        """
        count how many districts are green(over 340 green days)
        :return: a dictionary, represent the "good\bad" status of each district
        """
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

    """
    def keys(self):
        return self.dataset.keys()

    def values(self):
        return self.dataset.values()
    
    def __getitem__(self, key):
        if key in self.dataset:
            return self.dataset[key]
        if hasattr(self.__class__, "__missing__"):
            return self.__class__.__missing__(self, key)
    
    def __missing__(self, key):
        self.dataset[key] = None
    """
