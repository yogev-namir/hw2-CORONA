import pandas


class Data:

    def __init__(self, path):
        self.path = path
        df = pandas.read_cvs(path)  # import the path to df
        self.data = df.to_dict(orient="list")  # converting the cvs to dictionary

    def get_all_districts(self):
        list = [name for name in self.data.keys()]
        return list

    def set_districts_data(self, districts):
        filtered_dict = {}
        for key in self.data.keys():
            if key in districts:
                filtered_dict.update({key: self.data.get(key)})

        values_of_feature = [1 if a in districts else 0 for a in data.get("denominazione_region")]
        for key in self.data.keys():
            d1_key_value = []  # above threshold
            for i in range(len(values_of_feature)):
                # checks for each item which dictionary is appropriate for him
                if values_of_feature[i]:
                    d1_key_value.append(self.data.get(key)[i])
            filtered_dict.update({key: d1_key_value})
        self.data = filtered_dict

dicty = {'a': [1], 'b': [123]}
print(DataTest.get_all_districts(dicty))
