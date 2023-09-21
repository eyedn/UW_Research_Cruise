##############################################################################
#   University of Washington Research Cruise
#   Aydin Karatas
###############################################################################


from experiment import Experiment
from sys import argv

if __name__ == "__main__":
    my_parameters = argv[1]
    my_experiment = Experiment(my_parameters)
    my_experiment.get_concentrations()
    