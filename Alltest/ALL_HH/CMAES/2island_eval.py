from __future__ import print_function
import re
import sys
import os
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import abc
import numpy as np
import xml.etree.ElementTree as ET
from operator import itemgetter

"""
NOTE: file formats used:
	-ind_file: 	generation, population size, (fitnes results), [resulting parameters]
	-final_archive_file: (fitnes results)
"""


class FileDoesNotExist(Exception):
    def __init__(self, missing_file, directory):
        message = "%s is not in %s" % (missing_file, directory)
        super(FileDoesNotExist, self).__init__(message)


class MetaOptimizationSettings:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_optimization_settings(self):
        raise NotImplementedError


class OptimizationSettings(MetaOptimizationSettings):
    '''
    Class for getting and storing the needed settings of the optimization process.
    '''

    def __init__(self, xml_file, directory):
        self.LAST_ELEMENT_INDEX = -1

        self.directory = directory

        try:
            self.xml = ET.parse(directory + '_settings.xml')
        except IOError:
            raise FileDoesNotExist(xml_file, self.directory)

        self.get_optimization_settings()
        self.number_of_objectives = len(self.features)

    def get_optimization_settings(self):
        root = self.xml.getroot()

        for child in root:
            if child.tag == "evo_strat":
                self.algorithm_name = child.text
            if child.tag == "model_path":
                self.model_name = child.text.split('/')[self.LAST_ELEMENT_INDEX]
                self.model_name = self.model_name[:-4]
            if child.tag == "max_evaluation":
                self.number_of_generations = int(float(child.text))
            if child.tag == "pop_size":
                self.population_size = int(float(child.text))
            if child.tag == "num_params":
                self.number_of_parameters = int(child.text)
            if child.tag == "num_islands":
                self.number_of_islands = int(float(child.text))
            if child.tag == "feats":
                self.features = child.text.split(", ")
            if child.tag == "weights":
                self.weights = map(self._float_or_int, child.text.strip().lstrip("[").rstrip("]").split(","))

    @staticmethod
    def _float_or_int(value):
        try:
            integer = int(value)
            return integer
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return str(value.strip("u").strip('\''))

    def get_params(self):
        print(self.__dict__.keys())


class RawMultiObjectiveOptimizationResult(OptimizationSettings):
    '''
    Class for getting and storing the result of the optimization procces.
    '''

    def __init__(self, xml_file, directory, ind_file):
        OptimizationSettings.__init__(self, xml_file, directory)
        self.ind_file = directory + ind_file
        self.individuals = []
        self.generations = []
        self.stats = []
        self.minimums = []
        self.parse_individual_file()
        self.calc_stat()

    def parse_individual_file(self):
        with open(self.ind_file, 'rb') as f:
            current_generation = []
            for individual in iter(f):
                if individual == b'COST - PARAMETERS - RENORMALIZED PARAMETERS\n':
                    continue
                individual = individual.decode("utf-8") 
                individual = individual[:-2].strip()

                self.individuals.append(self.split_values_of_individuals(individual))

        self.individuals = sorted(self.individuals , key=itemgetter(0, 2))
        gen = []
        print(len(self.individuals))
        for ind in self.individuals :
            gen.append(ind)
            if self.is_end_of_generation(len(gen)):
                self.generations.append(gen)
                gen = []


    @staticmethod
    def remove_unwanted_characters(element):
        remove_these_chars = ['(', ')', '[', ']', ',', ' ', '\n']
        for char in remove_these_chars:
            if char in element:
                element = element.replace(char, '')

        return element

    def split_values_of_individuals(self, new_individual):

        return [float(self.remove_unwanted_characters(value)) for value in new_individual.split() if self.remove_unwanted_characters(value)]

    def is_end_of_generation(self, length_of_generation):
        return length_of_generation == self.population_size * self.number_of_islands

    def save_generation(self, new_generation):
        self.generations.append(new_generation)

    def print_untouched_generations(self):
        self.print_given_generations(self.generations)

    def calc_stat(self):
        for i, gen in enumerate(self.generations):
            stat = []
            costs = [ind[2] for ind in gen]
            minim = min(costs)
            stat.append(minim)
            self.smooth_minimums(minim)
            stat.append(np.median(costs))
            stat.append(max(costs))
            self.stats.append(stat)

    def smooth_minimums(self, current_minimum):
        try:
            current_best = min(self.minimums)
        except ValueError:
            self.minimums.append(current_minimum)
            return current_minimum
        if current_minimum < current_best:
            self.minimums.append(current_minimum)
            return current_minimum
        else:
            self.minimums.append(current_best)
            return current_best

    @staticmethod
    def print_given_generations(generations):
        for generation in generations:
            print(*generation, sep='\n')





class GeneralPlotter(object):
    def __init__(self, algorithm_name='', model_name='', directory='', features=''):
        self.algorithm_name = algorithm_name
        self.model_name = model_name
        self.directory = directory
        self.features = features

    def create_generation_plot(self, statistics, title='', directory=''):
        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax.plot([row[0] for row in statistics], 'r.-', label="max", linewidth=1.5)
        ax.plot([row[1] for row in statistics], 'r--', label="min", linewidth=1.5)
        ax.plot([row[2] for row in statistics], 'r', label="median", linewidth=1.5)

        ax.set_xlim(0, len(statistics))

        fig.suptitle('{0}{1}_on_{2}'.format(title, self.algorithm_name, self.model_name))
        plt.xlabel('generations')
        plt.ylabel('score value')
        plt.yscale('log')

        plt.legend(loc='best', fontsize=14, ncol=1)
        plt.savefig(directory + 'island.png', format='png')
        plt.close()

    def create_min_plot_of_all_runs(self, all_minimums_of_all_runs, title=''):
        number_of_runs = len(all_minimums_of_all_runs)
        fig = plt.figure()
        ax = fig.add_subplot(111)

        for run in range(number_of_runs):
            ax.plot(all_minimums_of_all_runs[run], label=str(run))
        ax.set_xlim(0, len(all_minimums_of_all_runs[0]))

        plt.xlabel('generations')
        plt.ylabel('score value')
        plt.legend(loc='best')

        plt.savefig(
            self.directory + '{0}{1}_runs_of_{2}_on_{3}.png'.format(title,number_of_runs, self.algorithm_name, self.model_name),
            format='png')
        plt.close()

    def create_pareto_plot(self, best_individuals, title="Pareto_Front"):
        number_of_objectives = len(self.features)
        OBJECTIVE_NUMBER = range(number_of_objectives)

        x = []
        y = []
        for individual in best_individuals:
            x.append(individual[OBJECTIVE_NUMBER[0]])
            y.append(individual[OBJECTIVE_NUMBER[1]])

        if number_of_objectives > 2:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            z = [row[OBJECTIVE_NUMBER[2]] for row in best_individuals]
            tuner_z = self.tune_limit(z)
            ax.scatter(x, y, z, color='b')
            ax.set_zlim(min(z) - tuner_z, max(z) + tuner_z)
            ax.set_zlabel(self.features[OBJECTIVE_NUMBER[2]])
        else:
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.scatter(x, y, color='b')

        tuner_x = self.tune_limit(x)
        tuner_y = self.tune_limit(y)
        ax.set_xlim(min(x) - tuner_x, max(x) + tuner_x)
        ax.set_ylim(min(y) - tuner_y, max(y) + tuner_y)
        fig.suptitle('{0}_of_{1}_on_{2}'.format(title, self.algorithm_name, self.model_name))
        ax.autoscale_view(True, True, True)

        ax.set_xlabel(self.features[OBJECTIVE_NUMBER[0]])
        ax.set_ylabel(self.features[OBJECTIVE_NUMBER[1]])
        plt.savefig(self.directory + '{0}_of_{1}_on_{2}.png'.format(title, self.algorithm_name, self.model_name),
                    format='png')
        plt.close()

    @staticmethod
    def tune_limit(values):
        return (max(values) - min(values)) / 100

def padding(all_minimums_of_all_runs):
    maximum_generations = max([len(run) for run in all_minimums_of_all_runs])
    new_all = []
    for run in all_minimums_of_all_runs:
        if len(run)<maximum_generations:
            run = run + [min(run)] * (maximum_generations-len(run))
        new_all.append(run)
    return new_all


def fill_statistics_for_all_runs(all_minimums_of_all_runs):
    all_statistics_of_all_runs = []
    for i in range(len(all_minimums_of_all_runs[0])):
        current_column = [column[i] for column in all_minimums_of_all_runs]
        all_statistics_of_all_runs.append(calculate_statistics(current_column))
    return all_statistics_of_all_runs


def calculate_statistics(data):
    maximum = max(data)
    minimum = min(data)
    median = np.median(data)
    return [maximum, minimum, median]


def get_directories(directory_base_name):
    regex = re.compile(directory_base_name + '_.')
    all_elements_in_cwd = [element for element in os.listdir(cwd) if os.path.isdir(element)]

    return [directory + '/' for directory in all_elements_in_cwd if re.match(regex, directory)]


def write_separate_statistics_to_separate_files(all_statistics_of_all_runs, cwd):
    STAT_TYPES = ["max","min", "median"]

    for index, stat_type in enumerate(STAT_TYPES):
        with open("{0}{1}.txt".format(results_directory, stat_type), "w") as f:
            for stats in all_statistics_of_all_runs:
                f.write('{0}\n'.format(stats[index]))

def write_separate_statistics(all_statistics_of_all_runs, cwd):


    with open(directory + "stat_file.txt", "w") as f:
        for stats in all_statistics_of_all_runs:
            f.write('{0}\n'.format(stats))

def write_statistics_to_file(directory, statistics, population_size):
    with open(directory + "all_stat_file.txt", "w") as f:
        for index, generation in enumerate(statistics):
            f.write('%d, %d, %s\n' % (index, population_size, ", ".join(map(str, generation))))

def create_directory_for_results(cwd):
    results_dir = cwd + '/results'
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    return results_dir + '/'

def save_best_costs(bests):
    import json
    with open('listfile.json', 'w') as filehandle:  
        json.dump({'costs': bests}, filehandle)

    with open('best_costs.txt', 'w') as f:
        for e in bests:
            f.write(str(e))
            f.write(' ')
            f.write(format(e, '.20f'))
            f.write('\n')

def save_lasts(directories):

    from bs4 import BeautifulSoup as bs
    import decimal

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
    start_time = time.time()
    INDEX_OF_MINIMUM = 1
    cwd = os.getcwd()
    results_directory = create_directory_for_results(cwd)

    # Parameters for every run (only initialized the variables)
    algorithm_name = ''
    population_size = 0
    model_name = ''

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

    all_minimums_of_all_runs = []
    all_smoothed_minimums_of_all_runs = []
    plotter = GeneralPlotter()
    algo_name = ''
    model_name = ''

    save_lasts(directories)

    for instance_index, directory in enumerate(directories):
        print(directory)
        sorted_result = RawMultiObjectiveOptimizationResult(xml_file='hh_pas_settings.xml', directory=directory, ind_file='island_inds.txt')
        write_separate_statistics(sorted_result.stats, directory)
        all_minimums_of_all_runs.append(sorted_result.minimums)
        plotter.create_generation_plot(sorted_result.stats, directory=directory)
        algo_name = sorted_result.algorithm_name
        model_name = sorted_result.model_name

    algo_name = algo_name.replace(' ', '_')
    all_statistics_of_all_runs = fill_statistics_for_all_runs(padding(all_minimums_of_all_runs))
    write_statistics_to_file((results_directory), all_statistics_of_all_runs, population_size)
    write_separate_statistics_to_separate_files(all_statistics_of_all_runs, results_directory)
    plotter = GeneralPlotter(algorithm_name=algo_name, model_name=model_name, directory=(results_directory))
    plotter.create_generation_plot(all_statistics_of_all_runs, title="Statistics_of_every_run_of_")
print("--- %s seconds ---" % (time.time() - start_time))
