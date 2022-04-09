# How to Debug for NLP Purposes Decently
This is a simple repo for demonstrating how to effectively debug python files.

This tutorial is a detailed version. If you already have relevant background knowledge, a simpler version is [here]()

You may try out the examples by cloning the repo.
```bash
git clone https://github.com/PKU-TANGENT/how_to_debug.git
```

Suppose that the development environment is a server to be connected using ssh. 
## Recommended prerequisites
### Locally
1. `Vscode` for powerful extensions and decent ssh integrations. More specific list for extensions is as follows
    - `Remote - SSH` (Note that the developer is Microsoft. )
### On Server
1. `conda` for easy python environment management. `miniconda` is recommended specifically to save disk memory.
2. `Vscode Extensions` for powerful debug support. Note that the following extensions are installed on server. This can be achieved by first connecting to the server using local ssh extension. (This process may be further explicated in another repo.) Then, search for the extensions and select `install in SSH`. The specified extensions are as follows:
    -  `Python` (Note that the developer is Microsoft)
## Getting Started
I suggest testing directly using the `base` environment of conda. The package that we are using is [debugpy](https://github.com/microsoft/debugpy). The original repo README contains sufficient examples. We shall start by installing debugpy via pip.

(Skipping this bracketed content is okay. Note that for Chinese users, I recommend using Tsinghua `tuna` mirror for pip and conda acceleration. The detailed instructions are [here for pip](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/) and [here for conda](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/). Yet, Mac M1 chip users should not change default conda repos if using M1 custom conda)
```bash
# installing debugpy via pip
# make sure that you are in the (base) conda environment
pip install debugpy
```

Click on `example.py` and wait for the python extension to load. There should be a python interpreter selecter located at the lower-right corner of the Vscode editor. Click on the selector and choose the `(base)` conda environment.
### Debug by Launching the current file
I strongly recommend creating a launch.json file for organizing debug configurations. This can be done by switching to the debug panel. The default configuration is as follows:
```json
{
    "name": "Python: lauch current file",
    "type": "python",
    "request": "launch",
    "program": "${file}",
    "console": "integratedTerminal",
    "justMyCode": true
}
```
The `"name"` field is arbitrary for easy recognition. This configuration launches the currently opened python file. There are two common ways to append a breakpoint in this scenario. 

1. Add a call to `breakpoint()` at desired lines of the file. 

2. Add a breakpoint using Vscode UI and clicking the space left to the desired line number.

Keep `example.py` opened and navigate to debug panel. Select `"Python: launch current file"` and hit the run-debug button. The program should pause after the line of `breakpoint()`.
