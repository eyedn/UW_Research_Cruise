###############################################################################
#   University of Washington Research Cruise
#   Aydin Karatas
###############################################################################


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
                solvent = int(f.readline())
                solute = int(f.readline())
                self.DF = solvent / solute
            else:
            # DF set to 1 when no DF is given to make self.DF inconsequential
                self.DF = 1

            # initialize concentrations as None
            self.conc_labs = ["Chlorophyll A", "Phaeopigment"]
            self.chla: float = None
            self.phaeo: float = None

    def get_chla(self) -> float:
        conc = self.K * (self.Fm / (self.Fm - 1)) * \
            (self.Fo - self.Fa) * self.Ex / self.Filt * self.DF
        self.chla = conc

    def get_phaeo(self) -> float:
        conc = self.K * (self.Fm / (self.Fm - 1)) * \
            ((self.Fm * self.Fa) - self.Fo) * self.Ex / self.Filt * self.DF
        self.phaeo = conc
    
    def get_formatted_conc(self) -> None:
        for i, conc in enumerate([self.chla, self.phaeo]):
            conc_str = str(conc)
            truncated_str = conc_str[:conc_str.index('.') + 4]
            truncated_conc = float(truncated_str)
            print(f"{self.conc_labs[i]} (µg/L) = {truncated_conc:.3f}")
    