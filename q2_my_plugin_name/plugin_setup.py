# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
from q2_types.feature_data import FeatureData, Sequence
from q2_types.sample_data import AlphaDiversity, SampleData
from qiime2.plugin import Citations, Metadata, Plugin

import q2_my_plugin_name
from q2_my_plugin_name import __version__
from q2_my_plugin_name._action_params import (
    apply_statistics_param_descriptions,
    apply_statistics_params,
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
    output_descriptions={"out1": "Manipulated file."},
    name="Name that describes my plugin method",
    description="Sample function that can be used as a template.",
)

plugin.visualizers.register_function(
    function=q2_my_plugin_name.apply_visualizer.visualizer_function,
    inputs={"visualizer_input": SampleData[AlphaDiversity]},
    parameters={"metadata": Metadata},
    input_descriptions={"visualizer_input": "Input fpr yhr visualizer function."},
    parameter_descriptions={"metadata": "The sample metadata."},
    name="Alpha diversity comparisons",
    description=("Visually do something."),
)
