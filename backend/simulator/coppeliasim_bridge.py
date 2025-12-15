import subprocess
import time
import os

COPPELIASIM_PATH = "/opt/CoppeliaSim/coppeliaSim.sh"
SCENE_PATH = os.path.abspath(
    "backend/simulator/scenes/scene_ur5_cube.ttt"
)

def start_coppeliasim():
    try:
        subprocess.Popen([COPPELIASIM_PATH, SCENE_PATH])
        time.sleep(5)
        return True
    except Exception as e:
        return str(e)
