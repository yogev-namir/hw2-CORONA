import pandas


class Data:

    def __init__(self, path):
        self.path = path
        df = pandas.read_cvs(path)  # import the path to df
        self.data = df.to_dict(orient="list")  # converting the cvs to dictionary

    def get_all_districts(self):
        list = [name for name in self.data[]]
        return list

    def set_districts_data(self, districts):
        filtered_dict = {}
        for key in self.data.keys():
            if key in districts:
                data.update({key: self.data.keys(key)})
        self.data = data

        return filtered_dict


dicty = {'a': [1], 'b': [123]}
print(DataTest.get_all_districts(dicty))
