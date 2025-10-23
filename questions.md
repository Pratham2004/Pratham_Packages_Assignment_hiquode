1. What is a package in Python?  
   A package is a directory that contains one or more Python modules and an `__init__.py` file (even if empty). It lets you organize related modules into a hierarchical namespace (e.g., `package.submodule`).

2. What is the difference between a module and a package?  
   A module is a single `.py` file that can define functions, classes, and variables.  
   A package is a folder that can hold multiple modules (and even sub-packages) and must include `__init__.py`.

3. What is the purpose of the `__init__.py` file in a package?  
   It signals to Python that the directory should be treated as a package. It can also execute initialization code or expose selected objects at the package level via `__all__`.

4. Name any 5 built-in Python packages and their uses.  
   - `math` – mathematical functions (sqrt, sin, log).  
   - `random` – pseudo-random number generation.  
   - `datetime` – date and time manipulation.  
   - `json` – encode/decode JSON data.  
   - `os` – interact with the operating system (files, paths, env vars).

5. Difference between:  
   a) `import math`  
      Imports the entire module; you must prefix its contents: `math.sqrt(9)`.  
   b) `from math import sqrt`  
      Imports only the `sqrt` function into the current namespace; call it directly: `sqrt(9)`.