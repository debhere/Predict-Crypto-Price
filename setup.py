# from typing import List
# from pathlib import Path
# from setuptools import setup, find_packages

# def get_requirements(filename: Path) -> List:
    
#     with open(filename) as f:
#         requirements = f.readlines()
#         requirements = [r.replace('\n', '') for r in requirements]
#         requirements = [r.replace('-e .', '') for r in requirements]

#     return requirements


# setup(
#     name = "predictcrypto",
#     version = "0.0.1",
#     author = "Debmalya (Deb)",
#     packages = find_packages(),
#     install_requires = get_requirements("requirements.txt")
# )





