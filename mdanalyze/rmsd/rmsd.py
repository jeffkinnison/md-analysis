"""
mdanalyze.rmsd.rmsd

Author: Jeff Kinnison (jkinniso@nd.edu)
"""


import mdtraj.load
import mdtraj.rmsd
import numpy.savetxt


class AbstractRMSDCalculator(object):
    """
    Base class for RMSD calculation unit.

    Methods:
    calculate_and_store -- Calculate the RMSD and save it.
    calculate -- Calculate the RMSD.
    store -- Save the RMSD.
    """

    def __init__(self, topology, reference):
        """
        Create a new AbstractRMSDCalculator instance.
        (Yes, I'm aware that you shouldn't be able to instantiate abstact
        classes, but Python doesn't really have abstract classes)

        Arguments:
        topology -- the topology file for the model
        reference -- the reference model for RMSD calculation
        """
        self._topology = topology
        self._reference = reference

    def calculate_and_store(self, **kwargs):
        """
        Calculate the RMSD and save it.

        Override in subclasses.
        """
        self.calculate(**kwargs)
        self.store(**kwargs)

    def calculate(self):
        """
        Calculate the RMSD.
        """
        raise NotImplementedError()

    def store(self):
        """
        Save the RMSD.
        """
        raise NotImplementedError()


class MDTrajRMSDCalculator(object):
    """
    Calculate RMSD using MDTraj analysis functions.

    Inherits from AbstractRMSDCalculator.
    """
    def __init__(self, topology, reference, atom_select='all'):
        """

        """
        super(MDTrajRMSDCalculator, self).__init__(topology, reference)
        self._atom_select = atom_select

    def calculate(self, trajectory="trajectory.dcd"):
        """

        """
        pass

    def store(self, outfile="rmsd.csv"):
        """

        """
        pass
