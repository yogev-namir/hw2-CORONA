import pandas


class Data:

    def __init__(self, path):
        self.path = path
        df = pandas.read_csv(path)  # import the path to df
        self.data = df.to_dict(orient="list")  # converting the cvs to dictionary

    def get_all_districts(self):
        districts = []
        for i in range(21):
            districts.append(self.data['denominazione_region'][i])
        return districts

    def set_districts_data(self, districts):
        filtered_dict = {}
        records = self.data["denominazione_region"]
        values_of_feature = [1 if record in districts else 0 for record in records]
        for key in self.data.keys():
            d1_key_value = []  # value's district is in the districts list
            for i in range(len(values_of_feature)):
                # checks for each item which dictionary is appropriate for him
                if values_of_feature[i]:
                    d1_key_value.append(self.data[key][i])
            filtered_dict.update({key: d1_key_value})
        self.data = filtered_dict

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        if hasattr(self.__class__, "__missing__"):
            return self.__class__.__missing__(self, key)


    def values(self):
        return self.data.values()


    def keys(self):
        return self.data.keys()

    def update(self, dict=None, **kwargs):
        if dict is None:
            pass
        elif isinstance(dict, UserDict):
            self.data.update(dict.data)
        elif isinstance(dict, type({})) or not hasattr(dict, 'items'):
            self.data.update(dict)
        else:
            for k, v in dict.items():
                self[k] = v
        if len(kwargs):
            self.data.update(kwargs)