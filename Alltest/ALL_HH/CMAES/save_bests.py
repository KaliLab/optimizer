from bs4 import BeautifulSoup as bs
import decimal
import sys
import os
import re
import numpy as np

def get_directories(directory_base_name):
    regex = re.compile(directory_base_name + '_.')
    all_elements_in_cwd = [element for element in os.listdir(cwd) if os.path.isdir(element)]

    return [directory + '/' for directory in all_elements_in_cwd if re.match(regex, directory)]


def create_directory_for_results(cwd):
    results_dir = cwd + '/results'
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    return results_dir + '/'


def save_lasts(directories):


    for idx, directory in enumerate(directories):
        for file in os.listdir(directory):
            if file.endswith(".html"):
                html_file = os.path.join(directory, file)

        soup = bs(open(html_file), 'html.parser')
        #finding all table html elemnts
        elem = soup.findAll('table')
        #finding all the td html elements in the first table which contains the parameter combinations
        table = elem[0].findAll('td')
        #finding all centers
        centers = soup.findAll('center')
        #second center tag and second b tag contain fitnes
        fitnes = centers[1].findAll('b')[1]
        
        #finding the parameters
        params = table[3::4]

        D = decimal.Decimal
        #dirty way of stripping first and last brackets
        fitnes = D(fitnes.getText()[1:-1])
        #removing html tags and converting to decimal
        for i in range(len(params)):
            params[i] = D(params[i].getText())
        lasts = [fitnes] + params


        #finding the parameters for the csv file as headers
        if idx == 0:
            headers = table[0::4]
            for i in range(len(headers)):
                headers[i] = str(headers[i].getText())
            headers.insert(0,"Cost")
            #adding headers
            np.savetxt('last.csv', [lasts], delimiter=',', header = ','.join(headers), fmt="%.20g", newline='\n')
        #no header + appending to existing file
        else:
            with open('last.csv','ab') as f:
                np.savetxt(f, [lasts], delimiter=',', fmt="%.20g", newline='\n')


if __name__ == '__main__':
    cwd = os.getcwd()
    results_directory = create_directory_for_results(cwd)

    # Parameters for every run (only initialized the variables)

    # This must be give to the script by hand: what is the base directory name of the results
    try:
        base_directory = sys.argv[1]
    except IndexError:
        print('No default directory was given.')
        exit()

    directories = get_directories(base_directory)

    if not directories:
        print("--------Wrong bas directory name--------")
        exit()

    save_lasts(directories)