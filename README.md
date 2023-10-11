# q2-my_plugin
QIIME 2 plugin for (meta)genome my_plugin.

## Installation
To install _q2-my_plugin_, follow the installation steps described below.

```shell
mamba create -yn q2-shotgun \
  -c https://packages.qiime2.org/qiime2/2022.8/tested \
  -c bioconda -c conda-forge -c default q2-my_plugin q2cli

conda activate q2-shotgun
```

Refresh cache and check that everything worked:
```shell
qiime dev refresh-cache
qiime info
```

## Functionality


## Dev environment
This repository follows the _black_ code style. To make the development slightly easier
there are a couple of pre-commit hooks included here that will ensure that your changes
follow that formatting style. Before you start working on the code, please
install the hooks by executing `make dev` in your conda environment. From then on,
they will be run automatically every time you commit any changes.
