---
source_id: "SRC-ai-055"
title: "NVIDIA Isaac Lab binary installation documentation"
source_type: "product_documentation"
publisher: "NVIDIA Isaac Lab"
source_date: "2026"
url: "https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/binaries_installation.html"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-07-07T01:22:36+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/a
aliases:
  - SRC-ai-055
---
# NVIDIA Isaac Lab binary installation documentation

## Installation using Isaac Sim Pre-built Binaries

The following steps first installs Isaac Sim from its pre-built binaries, then Isaac Lab from source code.

## Installing Isaac Sim

### Verifying the Isaac Sim installation

To avoid the overhead of finding and locating the Isaac Sim installation directory every time, we recommend exporting the following environment variables to your terminal for the remaining of the installation instructions:

```bash
# Isaac Sim root directory
export ISAACSIM_PATH="${HOME}/isaacsim"
# Isaac Sim python executable
export ISAACSIM_PYTHON_EXE="${ISAACSIM_PATH}/python.sh"
```

```batch
:: Isaac Sim root directory
set ISAACSIM_PATH="C:\isaacsim"
:: Isaac Sim python executable
set ISAACSIM_PYTHON_EXE="%ISAACSIM_PATH:"=%\python.bat"
```

Check that the simulator runs as expected:

```bash
# note: you can pass the argument "--help" to see all arguments possible.
${ISAACSIM_PATH}/isaac-sim.sh
```

```batch
:: note: you can pass the argument "--help" to see all arguments possible.
%ISAACSIM_PATH%\isaac-sim.bat
```

Check that the simulator runs from a standalone python script:

```bash
# checks that python path is set correctly
${ISAACSIM_PYTHON_EXE} -c "print('Isaac Sim configuration is now complete.')"
# checks that Isaac Sim can be launched from python
${ISAACSIM_PYTHON_EXE} ${ISAACSIM_PATH}/standalone_examples/api/isaacsim.core.api/add_cubes.py
```

```batch
:: checks that python path is set correctly
%ISAACSIM_PYTHON_EXE% -c "print('Isaac Sim configuration is now complete.')"
:: checks that Isaac Sim can be launched from python
%ISAACSIM_PYTHON_EXE% %ISAACSIM_PATH%\standalone_examples\api\isaacsim.core.api\add_cubes.py
```

> [!caution] Caution
> If you have been using a previous version of Isaac Sim, you need to run the following command for the *first* time after installation to remove all the old user data and cached variables:
>
> ```bash
> ${ISAACSIM_PATH}/isaac-sim.sh --reset-user
> ```
>
> ```batch
> %ISAACSIM_PATH%\isaac-sim.bat --reset-user
> ```

If the simulator does not run or crashes while following the above instructions, it means that something is incorrectly configured. To debug and troubleshoot, please check Isaac Sim [documentation](https://docs.omniverse.nvidia.com/dev-guide/latest/linux-troubleshooting.html) and the [Isaac Sim Forums](https://docs.isaacsim.omniverse.nvidia.com/latest/common/feedback.html).

## Installing Isaac Lab

### Cloning Isaac Lab

> [!note] Note
> We recommend making a [fork](https://github.com/isaac-sim/IsaacLab/fork) of the Isaac Lab repository to contribute to the project but this is not mandatory to use the framework. If you make a fork, please replace `isaac-sim` with your username in the following instructions.

Clone the Isaac Lab repository into your project’s workspace:

```bash
git clone git@github.com:isaac-sim/IsaacLab.git --branch main
cd IsaacLab
```

```bash
git clone https://github.com/isaac-sim/IsaacLab.git --branch main
cd IsaacLab
```

We provide a helper executable [isaaclab.sh](https://github.com/isaac-sim/IsaacLab/blob/main/isaaclab.sh) and [isaaclab.bat](https://github.com/isaac-sim/IsaacLab/blob/main/isaaclab.bat) for Linux and Windows respectively that provides utilities to manage extensions.

```
./isaaclab.sh --help

usage: isaaclab.sh [-h] [-i] [-f] [-p] [-s] [-t] [-o] [-v] [-d] [-n] [-c] -- Utility to manage Isaac Lab.

optional arguments:
   -h, --help           Display the help content.
   -i, --install [LIB]  Install the extensions inside Isaac Lab and learning frameworks (rl_games, rsl_rl, sb3, skrl) as extra dependencies. Default is 'all'.
   -f, --format         Run pre-commit to format the code and check lints.
   -p, --python         Run the python executable provided by Isaac Sim or virtual environment (if active).
   -s, --sim            Run the simulator executable (isaac-sim.sh) provided by Isaac Sim.
   -t, --test           Run all python pytest tests.
   -o, --docker         Run the docker container helper script (docker/container.sh).
   -v, --vscode         Generate the VSCode settings file from template.
   -d, --docs           Build the documentation from source using sphinx.
   -n, --new            Create a new external project or internal task from template.
   -c, --conda [NAME]   Create the conda environment for Isaac Lab. Default name is 'env_isaaclab'.
   -u, --uv [NAME]      Create the uv environment for Isaac Lab. Default name is 'env_isaaclab'.
```

```
isaaclab.bat --help

usage: isaaclab.bat [-h] [-i] [-f] [-p] [-s] [-v] [-d] [-n] [-c] -- Utility to manage Isaac Lab.

optional arguments:
   -h, --help           Display the help content.
   -i, --install [LIB]  Install the extensions inside Isaac Lab and learning frameworks (rl_games, rsl_rl, sb3, skrl) as extra dependencies. Default is 'all'.
   -f, --format         Run pre-commit to format the code and check lints.
   -p, --python         Run the python executable provided by Isaac Sim or virtual environment (if active).
   -s, --sim            Run the simulator executable (isaac-sim.bat) provided by Isaac Sim.
   -t, --test           Run all python pytest tests.
   -v, --vscode         Generate the VSCode settings file from template.
   -d, --docs           Build the documentation from source using sphinx.
   -n, --new            Create a new external project or internal task from template.
   -c, --conda [NAME]   Create the conda environment for Isaac Lab. Default name is 'env_isaaclab'.
   -u, --uv [NAME]      Create the uv environment for Isaac Lab. Default name is 'env_isaaclab'.
```

### Creating the Isaac Sim Symbolic Link

Set up a symbolic link between the installed Isaac Sim root folder and `_isaac_sim` in the Isaac Lab directory. This makes it convenient to index the python modules and look for extensions shipped with Isaac Sim.

```bash
# enter the cloned repository
cd IsaacLab
# create a symbolic link
ln -s ${ISAACSIM_PATH} _isaac_sim

# For example:
# Option 1: If pre-built binaries were installed:
# ln -s ${HOME}/isaacsim _isaac_sim
#
# Option 2: If Isaac Sim was built from source:
# ln -s ${HOME}/IsaacSim/_build/linux-x86_64/release _isaac_sim
```

```batch
:: enter the cloned repository
cd IsaacLab
:: create a symbolic link - requires launching Command Prompt with Administrator access
mklink /D _isaac_sim %ISAACSIM_PATH%

:: For example:
:: Option 1: If pre-built binaries were installed:
:: mklink /D _isaac_sim C:\isaacsim
::
:: Option 2: If Isaac Sim was built from source:
:: mklink /D _isaac_sim C:\IsaacSim\_build\windows-x86_64\release
```

### Setting up a Python Environment (optional)

> [!note] Attention
> This step is optional. If you are using the bundled Python with Isaac Sim, you can skip this step.

Creating a dedicated Python environment for Isaac Lab is **strongly recommended**, even though it is optional. Using a virtual environment helps:

- **Avoid conflicts with system Python** or other projects installed on your machine.
- **Keep dependencies isolated**, so that package upgrades or experiments in other projects do not break Isaac Sim.
- **Easily manage multiple environments** for setups with different versions of dependencies.
- **Simplify reproducibility** — the environment contains only the packages needed for the current project, making it easier to share setups with colleagues or run on different machines.

You can choose different package managers to create a virtual environment.

- **UV**: A modern, fast, and secure package manager for Python.
- **Conda**: A cross-platform, language-agnostic package manager for Python.

Once created, you can use the default Python in the virtual environment (*python* or *python3*) instead of *./isaaclab.sh -p* or *isaaclab.bat -p*.

> [!caution] Caution
> The Python version of the virtual environment must match the Python version of Isaac Sim.
>
> - For Isaac Sim 5.X, the required Python version is 3.11.
> - For Isaac Sim 4.X, the required Python version is 3.10.
>
> Using a different Python version will result in errors when running Isaac Lab.

To install conda, please follow the instructions [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). You can create the Isaac Lab environment using the following commands.

We recommend using [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main/), since it is light-weight and resource-efficient environment management system.

```bash
# Option 1: Default environment name 'env_isaaclab'
./isaaclab.sh --conda  # or "./isaaclab.sh -c"
# Option 2: Custom name
./isaaclab.sh --conda my_env  # or "./isaaclab.sh -c my_env"
```

```bash
# Activate environment
conda activate env_isaaclab  # or "conda activate my_env"
```

```batch
:: Option 1: Default environment name 'env_isaaclab'
isaaclab.bat --conda  :: or "isaaclab.bat -c"
:: Option 2: Custom name
isaaclab.bat --conda my_env  :: or "isaaclab.bat -c my_env"
```

```batch
:: Activate environment
conda activate env_isaaclab  # or "conda activate my_env"
```

To install `uv`, please follow the instructions [here](https://docs.astral.sh/uv/getting-started/installation/). You can create the Isaac Lab environment using the following commands:

```bash
# Option 1: Default environment name 'env_isaaclab'
./isaaclab.sh --uv  # or "./isaaclab.sh -u"
# Option 2: Custom name
./isaaclab.sh --uv my_env  # or "./isaaclab.sh -u my_env"
```

```bash
# Activate environment
source ./env_isaaclab/bin/activate  # or "source ./my_env/bin/activate"
```

> [!warning] Warning
> Windows support for UV is currently unavailable. Please check [issue #3483](https://github.com/isaac-sim/IsaacLab/issues/3438) to track progress.

Once you are in the virtual environment, you do not need to use `./isaaclab.sh -p` or `isaaclab.bat -p` to run python scripts. You can use the default python executable in your environment by running `python` or `python3`. However, for the rest of the documentation, we will assume that you are using `./isaaclab.sh -p` or `isaaclab.bat -p` to run python scripts.

### Installation

- Install dependencies using `apt` (on Linux only):
	```bash
	# these dependency are needed by robomimic which is not available on Windows
	sudo apt install cmake build-essential
	```
- Run the install command that iterates over all the extensions in `source` directory and installs them using pip (with `--editable` flag):
	```bash
	./isaaclab.sh --install # or "./isaaclab.sh -i"
	```
	```batch
	isaaclab.bat --install :: or "isaaclab.bat -i"
	```
	By default, the above will install **all** the learning frameworks. These include `rl_games`, `rsl_rl`, `sb3`, `skrl`, `robomimic`.
	If you want to install only a specific framework, you can pass the name of the framework as an argument. For example, to install only the `rl_games` framework, you can run:
	```bash
	./isaaclab.sh --install rl_games  # or "./isaaclab.sh -i rl_games"
	```
	```batch
	isaaclab.bat --install rl_games :: or "isaaclab.bat -i rl_games"
	```
	The valid options are `all`, `rl_games`, `rsl_rl`, `sb3`, `skrl`, `robomimic`, and `none`. If `none` is passed, then no learning frameworks will be installed.

### Verifying the Isaac Lab installation

To verify that the installation was successful, run the following command from the top of the repository:

```bash
# Option 1: Using the isaaclab.sh executable
# note: this works for both the bundled python and the virtual environment
./isaaclab.sh -p scripts/tutorials/00_sim/create_empty.py

# Option 2: Using python in your virtual environment
python scripts/tutorials/00_sim/create_empty.py
```

```batch
:: Option 1: Using the isaaclab.bat executable
:: note: this works for both the bundled python and the virtual environment
isaaclab.bat -p scripts\tutorials\00_sim\create_empty.py

:: Option 2: Using python in your virtual environment
python scripts\tutorials\00_sim\create_empty.py
```

The above command should launch the simulator and display a window with a black viewport. You can exit the script by pressing `Ctrl+C` on your terminal. On Windows machines, please terminate the process from Command Prompt using `Ctrl+Break` or `Ctrl+fn+B`.

![Simulator with a black window.](https://isaac-sim.github.io/IsaacLab/main/_images/verify_install.jpg)

Simulator with a black window.

If you see this, then the installation was successful! 🎉

> [!note] Note
> If you see an error `ModuleNotFoundError: No module named 'isaacsim'`, please ensure that the virtual environment is activated and `source _isaac_sim/setup_conda_env.sh` has been executed (for uv as well).

### Train a robot!

You can now use Isaac Lab to train a robot through Reinforcement Learning! The quickest way to use Isaac Lab is through the predefined workflows using one of our **Batteries-included** robot tasks. Execute the following command to quickly train an ant to walk! We recommend adding `--headless` for faster training.

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py --task=Isaac-Ant-v0 --headless
```

```batch
isaaclab.bat -p scripts/reinforcement_learning/rsl_rl/train.py --task=Isaac-Ant-v0 --headless
```

… Or a robot dog!

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py --task=Isaac-Velocity-Rough-Anymal-C-v0 --headless
```

```batch
isaaclab.bat -p scripts/reinforcement_learning/rsl_rl/train.py --task=Isaac-Velocity-Rough-Anymal-C-v0 --headless
```

Isaac Lab provides the tools you’ll need to create your own **Tasks** and **Workflows** for whatever your project needs may be. Take a look at our [How-to Guides](https://isaac-sim.github.io/IsaacLab/main/source/how-to/index.html#how-to) guides like [Adding your own learning Library](https://isaac-sim.github.io/IsaacLab/main/source/how-to/add_own_library.html#how-to-add-library) or [Wrapping Environments](https://isaac-sim.github.io/IsaacLab/main/source/how-to/wrap_rl_env.html#how-to-env-wrappers) for details.

![Idle hands...](https://isaac-sim.github.io/IsaacLab/main/_images/isaac_ants_example.jpg)

Idle hands...
