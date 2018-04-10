#!/usr/env/python3

import openmc
import matplotlib.pyplot as plt

def get_spectrum(tally,cell):
    mean = tally.get_values(scores=['flux'],filters=[openmc.CellFilter],filter_bins=[(cell,)])
    error = tally.get_values(scores=['flux'],filters=[openmc.CellFilter],filter_bins=[(cell,)],value='std_dev')

    mean = mean[:,0,0]
    error = error[:,0,0]

    return mean,error
    

sp = openmc.StatePoint('statepoint.10.h5')
tally = sp.get_tally(scores=['flux'])

energy = tally.find_filter(openmc.EnergyFilter).bins
energy = energy[1:]

tally_135,error_135 = get_spectrum(tally,135)
tally_158,error_158 = get_spectrum(tally,158)
tally_181,error_181 = get_spectrum(tally,181)
tally_204,error_204 = get_spectrum(tally,204)

plt.errorbar(energy, tally_135, error_135)
plt.errorbar(energy, tally_158, error_158)
plt.errorbar(energy, tally_181, error_181)
plt.errorbar(energy, tally_204, error_204)

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Energy (eV)')
plt.ylabel('Flux (n/cm^{-2})')
plt.show()
