# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.core.type import Bool, Choices, Float, Int, List, Range, Str

apply_statistics_params = {
    "debug": Bool,
}
# fmt: off
apply_statistics_param_descriptions = {
    "debug": " Enable debug logging.",
}