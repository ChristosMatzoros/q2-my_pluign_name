# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.core.type import Bool, Choices, Float, Int, List, Range, Str

apply_statistics_params = {
    "cpus": Int % Range(1, None),
    "debug": Bool,
    "seed": Int % Range(0, None),
}
# fmt: off
apply_statistics_param_descriptions = {
    "cpus": "Number of cpus to use.",
    "debug": " Enable debug logging.",
    "seed": "Seed for all the random number generators.",
}