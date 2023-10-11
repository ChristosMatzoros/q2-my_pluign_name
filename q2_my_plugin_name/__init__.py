# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from ._version import get_versions
from .apply_statistics import apply_statistics

__version__ = get_versions()["version"]
del get_versions

__all__ = ["apply_statistics"]
