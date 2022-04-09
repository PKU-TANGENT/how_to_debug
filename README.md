# How to Debug for NLP Purposes Decently
This is a simple repo for demonstrating how to effectively debug python files.

This tutorial is a detailed version. If you already have relevant background knowledge, a simpler version is [here](https://github.com/PKU-TANGENT/how_to_debug/blob/main/simpler_version.md)

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
I suggest testing directly using the `base` environment of conda. The package that we are using is [debugpy](https://github.com/microsoft/debugpy). The original repo README contains sufficient examples. Moreover, Microsoft also provides a detailed tutorial on debugging python files via Vscode [here](https://code.visualstudio.com/docs/python/debugging). We shall start by installing debugpy via pip.

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
### Debugging via Attaching Process
In NLP scenarios, it is quite often that the original repo only provides scripts for easy usage. Manually creating a `launch` configuration in `launch.json` is laborious. The best solution is to leverage debugging via attaching. 

Suppose that you have a script like this. 
```bash
#!/bin/bash
python args_test.py \
  "This is arg 1" \
    "This is arg 2"
```
Where command line arguments are passed to the program. The easiest way to debug using attach mode is to modify the script as follows:
```bash
#!/bin/bash
python -m debugpy --listen 127.0.0.1:5678 --wait-for-client args_test.py \
  "This is arg 1" \
    "This is arg 2"
```
This means that we are instead using the debugpy module to launch our program. Moreover, the debug program is listening at `127.0.0.1`(which stands for `localhost`) and port `5678`(which is the default port). The `--wait-for-client` argument makes sure that the program is running after proper attachment of vscode debug functionalities.

Create a configuration in launch.json
```json
{
    "name": "Python: Attach",
    "type": "python",
    "request": "attach",
    "connect": {
        "host": "127.0.0.1",
        "port": 5678
    }
}
```
Note that the `host` and `port` should match your scripts.
Run the test script
```bash
bash test.sh
```
Navigate to the vscode debug panel, select `Python: Attach` and run. Make sure that everything works well. 

## What about the actual debugging process?
Now it is natural to focus on the real debugging process. I would like to elaborate on the `Step into` option. You can set `justMyCode: False` in the launch.json file to enable stepping into local packages and more in-depth debugging. 

What's more, you may keep track of the `call stack` and `variables` on the debug panel. I would like to emphasize the `watch` option. You may add expression whose value you are interested in. Interestingly, you may also call certain functions in the watch expression. For example, when running test.sh and debugging via attaching, you may watch the expression `len(sys.argv)`, which should give you `3` as its value. Another commonly used trick is to hover your mouse over the variable. Its values should pop up accordingly.
