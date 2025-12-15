from backend.simulator.coppeliasim_bridge import start_coppeliasim
from backend.simulator.result_analyzer import analyze_result
from backend.simulator.screenshot_capture import capture_screenshot


def run_simulation():
    sim_status = start_coppeliasim()
    if sim_status is not True:
        return {"status": "FAILED", "error": sim_status}


    screenshot = capture_screenshot()
    result = analyze_result()


    return {
    "status": result["status"],
    "details": result["details"],
    "screenshot": screenshot
    }