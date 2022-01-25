#! /usr/bin/env python
import csv
import argparse
from os import path 
import datetime




def main(argv=None):
    # check arguments given are valid 
    argument_values = check_argument_validity(argv)
    file_path = argument_values[0]
    target_date = argument_values[1]

    # get list of cookies from target date
    cookies_on_target_date = get_cookies_list_on_target_date(file_path, target_date)

    # get most frequent cookie(s) - depending on if there is a tie or not 
    most_frequent_cookies = get_most_frequent_cookies(cookies_on_target_date)

    # print most frequent cookie(s)     
    for cookie in most_frequent_cookies:
        print(cookie)




def get_cookies_list_on_target_date(file_path, target_date):

    # list to store all the cookies given on the target date 
    cookies_on_target_date = []
    # read cookie log file 
    with open(file_path) as cookie_log:

        csv_reader = csv.reader(cookie_log, delimiter=',')
        # iterate through each row in the cookie log CSV file 
        for row in csv_reader: 
            timestamp = row[1]
            # if date is found in the timestamp, then we will add the cookie 
            # to the list of cookies 
            if target_date in timestamp: 
                cookie = row[0]
                cookies_on_target_date.append(cookie)

    # if there are no cookies found on target date witihin the given cookies log 
    # raise error 
    if not bool(cookies_on_target_date):
        raise Exception("No available cookies found for target date")
    # return list of cookies on target date 
    return cookies_on_target_date




def get_most_frequent_cookies(cookies_on_target_date):
    # return the most cookie with the highest frequency in cookies_on_target_date list 
    cookies_dict = {}
    most_frequent_cookies = []
    max_count = 0
    # make a new dictionary where the key are the cookies, and the values are the number
    # of occurences 
    for cookie in cookies_on_target_date:

        if cookie not in cookies_dict:
            cookies_dict[cookie] = 0
        cookies_dict[cookie] += 1

    # store the max cookie frequency
    max_count = max(cookies_dict.values())

    # retrive the most frequent cookie (or cookies - depending on if there is a tie for
    # number of occurences
    for key in cookies_dict:
        if cookies_dict[key] == max_count:
            most_frequent_cookies.insert(0, key)

    # return list of most frequent cookies 
    return most_frequent_cookies




def check_argument_validity(argv):

    # parse command line into Python data types 
    argparser = argparse.ArgumentParser(description="Find the most active cookie given a cookie log file and a date")
    argparser.add_argument(dest="file_path", help="File path to cookie log CSV")
    argparser.add_argument('-d', dest="target_date", help="Target date to find cookie")

    # save file arguments into variables
    args = argparser.parse_args()
    file_path = args.file_path
    target_date = args.target_date
    
    # check for csv

    # test if all necessary arguments (file path and target date) are input by the user
    # if not, raise necessary exceptions to show an error has occured 
    if not path.exists(file_path):
        raise Exception("Invalid file path")
    if target_date == None:
        raise Exception("Please input a target date as argument")
    # check if file is a CSV file 
    if not file_path.split(".")[1] == "csv" :
        raise Exception("File is not a valid CSV file")
    # validate the target date argument using datetime library
    try:
        datetime.datetime.strptime(target_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")
    
    # return file_path and target_date to be used in main function
    return [file_path, target_date]


if __name__ == "__main__":
    main()

