##############################################################################
#   University of Washington Research Cruise
#   Aydin Karatas
###############################################################################


from experiment import Experiment
from sys import argv

if __name__ == "__main__":
    # experiment paramenters found in text file (argv[1])
    my_experiment = Experiment(argv[1])
    my_experiment.get_chla()
    my_experiment.get_phaeo()
    my_experiment.get_formatted_conc()
    