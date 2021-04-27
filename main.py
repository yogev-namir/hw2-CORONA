import sys
import data
import districts
from statistics import mean, median


def main(argv):

    # data input phase
    path = argv[1]
    input_data_1 = data.Data(path)  # for Question 1, is going to be filtered
    input_data_2 = data.Data(path)  # for Question 2, not filtered
    # filtering the dictionary(first letter and features)
    selected_districts = districts.District(input_data_1)  # dictionary
    letters_set = {'L', 'S'}
    selected_districts.filter_districts(letters_set)
    print('Question 1:')

    statistic_functions = [mean, median]
    features_to_print = ['hospitalized_with_symptoms', 'intensive_care', 'total_hospitalized', 'home_insulation']
    selected_districts.print_details(features_to_print, statistic_functions)
    ###########################################################
    print('Question 2:')
    all_districts = districts.District(input_data_2)  # dictionary
    all_districts.determine_day_type()
    green_or_not_districts = all_districts.get_districts_class()
    count = 0
    for string in green_or_not_districts.values():
        if string == 'green':
            count += 1
    answer: str = "Yes" if count > 10 else "No"
    number_of_districts = len(input_data_2.get_all_districts())
    print("Number of districts: {}".format(number_of_districts))
    print("Number of not green districts: {}".format(number_of_districts - count))
    print("Will a lockdown be forced on whole of Italy? {}".format(answer))
    ##########################################################################


if __name__ == '__main__':
    main(sys.argv)
