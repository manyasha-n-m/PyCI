# This file is part of PyCI.
#
# PyCI is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# PyCI is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyCI. If not, see <http://www.gnu.org/licenses/>.

r"""PyCI RDM Conditions module."""

import numpy as np

__all__ = [
    "find_closest_sdp",
]

def find_closest_sdp():
    r"""
    Projection onto a semidefinite constraint.

    Parameters
    ----------
    dm : np.ndarray
        Density matrix.
    constraint : function
        Positive semidefinite constraint, linear mapping.

    """