import json

class CountriesClass:
    def __init__(self, json):
        self.json = json
        self.current_list_index = 0
        self.items_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        current_list = self.json[self.current_list_index]
        self.current_list_index +=1
        if self.current_list_index == len(self.json):
            raise StopIteration
        return  current_list


if __name__ == '__main__':
    with open(f'Countries.json') as f:
        json_data = json.load(f)

    for i in CountriesClass(json_data):
        country = (i['name']['common'])
        print(country ,'-','https://en.wikipedia.org/wiki/'+country.replace(' ', '_'))