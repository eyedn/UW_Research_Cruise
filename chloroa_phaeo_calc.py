###############################################################################
#   University of Washington Research Cruise
#   Aydin Karatas
###############################################################################


from sys import argv
import typing

class Experiment:
    def __init__(self, data: typing.TextIO) -> None:
        with open(data) as f:
            self.K = float(f.readline())
            self.Fm = float(f.readline())
            self.Fo = float(f.readline())
            self.Fa = float(f.readline())
            self.Ex = float(f.readline())
            self.Filt = float(f.readline())

            # if a dilution factor is present, is_DF == 1
            is_DF = int(f.readline())
            if is_DF == 1:
                self.DF = float(f.readline())
            else:
            # DF set to 1 when no DF is given to make it inconsequential
                self.DF = 1

    def get_chla(self) -> float:
        conc = self.K * (self.Fm / (self.Fm - 1)) * \
            (self.Fo - self.Fa) * self.Ex / self.Filt * self.DF
        
        # truncate float for sig figs
        conc_str = str(conc)
        truncated_str = conc_str[:conc_str.index('.') + 4]
        truncated_conc = float(truncated_str)

        print(f"Chl a (µg/L) = {truncated_conc}")
        return truncated_conc

    def get_phaeo(self) -> float:
        conc = self.K * (self.Fm / (self.Fm - 1)) * \
            ((self.Fm * self.Fa) - self.Fo) * self.Ex / self.Filt * self.DF
        
        # truncate float for sig figs
        conc_str = str(conc)
        truncated_str = conc_str[:conc_str.index('.') + 4]
        truncated_conc = float(truncated_str)

        print(f"Phaeopigment (µg/L) = {truncated_conc:.3f}")
        return truncated_conc
    

if __name__ == "__main__":
    my_experiment = Experiment(argv[1])
    my_chla = my_experiment.get_chla()
    my_phaeo = my_experiment.get_phaeo()
