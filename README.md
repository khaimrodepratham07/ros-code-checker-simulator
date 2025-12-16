## ROS Code Checker & Simulation Preview Tool

## Overview

This project is a **ROS 2 code validation and simulation preview system** developed as part of a **Robotics Internship Assignment**. The goal of the system is to automatically:

1. Validate submitted ROS 2 packages for correctness and safety
2. Identify structural, syntax, and logical issues
3. Launch a robotic simulation environment (CoppeliaSim)
4. Provide a clear success/failure outcome with visual proof

The system is designed with **real-world robotics pipelines in mind**, where code validation must happen *before* simulation or deployment.

---

## Problem Statement (Assignment Context)

Robotics teams often receive ROS-based control code from multiple contributors. Running unverified code directly on simulators or hardware can lead to crashes, unsafe motions, or wasted debugging time.

This project solves that problem by:

* Automatically checking ROS package structure
* Performing static safety analysis
* Allowing simulation only after validation
* Providing clear feedback through reports and visuals

---

## High-Level System Architecture

```
User Uploads ZIP
        ↓
Code Validation Engine
        ↓
Validation Report (Errors / Warnings)
        ↓
Simulation Trigger (CoppeliaSim)
        ↓
Success / Failure + Screenshots
```

The system is divided into three main layers:

* **Backend (Validation + Simulation logic)**
* **Web Interface (User interaction)**
* **Simulation Environment (CoppeliaSim)**

---

## Features

### 1. ROS 2 Package Validation

The system validates uploaded ROS 2 packages for:

* Presence of `package.xml`
* Presence of `setup.py` or `CMakeLists.txt`
* Correct ROS package layout

### 2. Syntax & Style Analysis

* Python files are scanned using **flake8**
* Syntax errors are flagged
* Style issues are reported as warnings (not blocking)

### 3. Safety Checks

Static analysis is performed to detect:

* Infinite loops without sleep
* Unsafe joint value usage (context-aware)

Safety issues are reported as warnings or errors depending on severity.

### 4. Simulation Preview (CoppeliaSim)

After successful validation:

* A real **CoppeliaSim** scene is launched
* Scene contains:

  * 6-DOF robotic arm (UR5)
  * One cube
  * One target position
* Simulation logic evaluates success based on cube-to-target distance

### 5. Web-Based Interface

A lightweight **Flask** UI allows:

* Uploading ROS packages as ZIP files
* Viewing validation reports
* Triggering simulation manually

---

## Project Structure

```
ros-code-checker-sim/
├── backend/
│   ├── checker/           # Validation logic
│   ├── simulator/         # CoppeliaSim integration
│   └── utils/             # Helper utilities
│
├── web/                   # Flask web interface
│   ├── templates/
│   └── static/
│
├── test_packages/         # Good & faulty ROS test packages
├── scripts/               # Startup scripts
├── README.md
└── .gitignore
```

---

## Technologies Used

* **ROS 2 (Python)**
* **CoppeliaSim** (robotic simulation)
* **Python 3**
* **Flask** (web interface)
* **flake8** (syntax & style checking)
* **WSL 2 (Ubuntu 24.04)**

---

## Setup Instructions

### 1. Prerequisites

* Ubuntu 22.04+ (native or WSL)
* Python 3.10+
* ROS 2 installed
* CoppeliaSim installed

### 2. Clone Repository

```bash
git clone https://github.com/PrathamKhairmode/ros-code-checker-simulator.git
cd ros-code-checker-sim
```

### 3. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
```

### 4. Run the Web Application

```bash
./scripts/start_web.sh
```

Open browser:

```
http://127.0.0.1:5000
```

---

## How to Use

1. Open the web interface
2. Upload a ROS 2 package as a ZIP file
3. View the validation report
4. If validation passes, click **Run Simulation**
5. CoppeliaSim launches with the robotic scene
6. Simulation determines success or failure

---

## Test Packages

The repository includes sample packages for demonstration:

* **good_package** – Valid ROS 2 package (passes checks)
* **faulty_package** – Intentionally broken package (fails checks)

These demonstrate how the checker differentiates valid and unsafe code.

---

## Design Decisions

* Simulation is **manually triggered** after validation to ensure safety
* Style warnings do not block execution
* Each uploaded ZIP is extracted into an isolated workspace
* Scene logic is handled inside CoppeliaSim for stability

---

## Limitations & Future Work

Current limitations:

* ROS node execution is not yet fully integrated with simulator control
* Motion planning and grasping are simplified

Planned improvements:

* Direct ROS 2 ↔ CoppeliaSim communication
* Automatic simulation gating based on validation
* Enhanced success metrics and logging

---

## Demo

A demonstration video showcasing:

* Code upload
* Validation results
* Simulation launch
* Success detection

is included in the assignment submission.

---

## Author

**Pratham Khairmode**
B.E. Computer Science & Engineering
Robotics & Software Intern Applicant

---

## License

This project is intended for educational and evaluation purposes.
