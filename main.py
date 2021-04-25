import sys
import data
import districts
from statistics import mean, median


def main(argv):
    # data input phase
    path = argv[1]
    input_data = data.Data(path)

    # filtering the dictionary(first letter and features)
    selected_districts: districts.District = districts.District(input_data.data)  # a dictionary
    letters_set = {'L', 'S'}
    selected_districts.filter_districts(letters_set)

    print('Question 1:')
    statistic_functions = [mean, median]
    features_to_print = ['Distance', 'Flights', 'Passengers', 'Seats']
    selected_districts.print_details(features_to_print, statistic_functions)
    print('Question 2:')
    selected_districts.determine_day_type()
    good_or_bad_districts = selected_districts.get_districts_class()
    count = 0
    for string in good_or_bad_districts:
        if string == 'green':
            count += 1
    answer: str = "Yes" if count > 10 else "No"
    number_of_districts = len(input_data.get_all_districts())
    print("Number of districts: {}".format(number_of_districts))
    print("Number of not green districts: {}".format(number_of_districts - count))
    print("Will a lockdown be forced on whole of Italy? {}".format(answer))

    if __name__ == '__main__':
        main(sys.argv)
