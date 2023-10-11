# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
import importlib

import qiime2.plugin

from q2_types.feature_data import FeatureData, Sequence
from q2_types.feature_table import FeatureTable, Frequency

from q2_types_genomics.per_sample_data._type import AlignmentMap
from qiime2.plugin import Citations, Plugin, Str

import q2_my_plugin_name
from q2_my_plugin_name import __version__
from q2_my_plugin_name._action_params import (
    apply_statistics_param_descriptions,
    apply_statistics_params
)

citations = Citations.load("citations.bib", package="q2_my_plugin_name")

plugin = Plugin(
    name="my_plugin",
    version=__version__,
    website="https://github.com/bokulich-lab/q2-my_plugin",
    package="q2_my_plugin_name",
    description=(
        "QIIME 2 plugin for (meta)genome my_plugin and " "quality control thereof."
    ),
    short_description="QIIME 2 plugin for (meta)genome my_plugin.",
)

plugin.methods.register_function(
    function=q2_my_plugin_name.apply_statistics.stats,
    inputs={"seqs": FeatureData[Sequence]},
    parameters=apply_statistics_params,
    outputs=[
            ("out1", FeatureData[Sequence]),
        ],
    input_descriptions={
        "seqs": "Input (Input_FeatureDataSequence) of type FeatureData[Sequence] "
    },
    parameter_descriptions=apply_statistics_param_descriptions,
    output_descriptions={
        "out1": "Manipulated file."
    },
    name="Name that describes my plugin method",
    description="This sample function can be used as a template for a plugin method implementation.",
    citations=[citations["Gourle2019"]],
)

"""
plugin.visualizers.register_function(
    function=q2_my_plugin_name.apply_statistics.myPluginVisualization,
    inputs={'distance_matrix': DistanceMatrix},
    parameters={'metadata': Metadata},
    input_descriptions={
        'distance_matrix': 'Matrix of distances between pairs of samples.'
    },
    parameter_descriptions={
        'metadata': 'The sample metadata.'
    },
    name='bioenv',
    description=("Find the subsets of variables in metadata whose Euclidean "
                 "distances are maximally rank-correlated with distance "
                 "matrix. All numeric variables in metadata will be "
                 "considered, and samples which are missing data will be "
                 "dropped. The output visualization will indicate how many "
                 "samples were dropped due to missing data, if any were "
                 "dropped."),
    citations=[citations['clarke1993method']]
)
"""