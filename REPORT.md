TP2 — Modern Python Tooling



Part 1: Environment Isolation with uv



1\. Compare sys.executable and sys.prefix



Global Python run



Python executable: C:\\Users\\mohan\\anaconda3\\python.exe



sys.prefix: C:\\Users\\mohan\\anaconda3



Virtual environment: False



uv run



Python executable: C:\\Users\\mohan\\Documents\\EPITA\\epita\_vignesh\_kandavel\_crypto\\.venv\\Scripts\\python.exe



sys.prefix: C:\\Users\\mohan\\Documents\\EPITA\\epita\_vignesh\_kandavel\_crypto\\.venv



Virtual environment: True



2\. Explanation



The global Python command uses the Python installation provided by Anaconda. In contrast, uv run uses the project's virtual environment, keeping the project's Python execution isolated from the global Python environment.



uv run automatically selects the project's environment and runs the command within it. This avoids needing to activate the virtual environment manually for each command.

