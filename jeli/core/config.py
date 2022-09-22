"""

Autor: RobotsMaliAI Team
"""

import pathlib

ROOT = pathlib.Path(__file__).parent.parent.parent

with open(f"{ROOT}/jeli/config") as fp:
    confs = fp.readlines()

# Z_TOKEN = confs[0].split("=")[1].replace("\n", "")
VERSION = confs[0].split("=")[1].replace("\n", "")
