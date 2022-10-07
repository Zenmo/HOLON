# Experiments module

The experiments module allows you to define your experiment in a config file and run one or
multiple experiments sequentially. No more adjusting classes! Based on the existing scripts.


## Starting up

Go to the `config` folder and copy the `config.yml` file to `config.local.yml`. Specify
your secret API key to connect to the AnyLogic Cloud there.

Next define your experiments in the `experiments.yml` file. There is an example there to help you.

## Running the module

The base code for the module is in the `experiments` folder. But you can easily call the module
from the script `run_experiments` in the `scripts` folder. Here you can run one experiment by
specifying its name or all experiments by using the keyword `ALL`.

## Pipenv support

There is also support for pipenv now for the ones that are interested. There is a shortcut to
run the experiments: `pipenv run experiments {experiment_name}`.



Happy experimenting!
