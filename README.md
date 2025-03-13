## Photoluminescence Scanner

Thesis Project `Development of a diagnostic imaging system for field inspection solar photovoltaic PV plants` in collaboration with DTU Electro.

Carl Emil Elling, 2025

For access to thesis, find on DTU internal document query FindIT or contact directly at carlemilelling@hotmail.com

### Project Structure

- **Software:** Located in the `Software` folder. This folder contains the project software and calibration files. Note that the `.raw` calibration files are stored using Git LFS and are subject to a monthly bandwidth limit (1GB). These files are only needed for recalibration.
- **Mechanical Data:** Located in the `Mechanical` folder. This folder includes `.STL` files for all 3D printed components of the system, as well as `.step` files for the entire system assembly for reference.
- **PCB Data:** Located in the `PCB` folder. This folder contains data for the custom PCBs used for driving the IR LEDs.
- **Marlin-2.1.2.5-PLRobot:** This folder contains a custom fork of the open-source Marlin 3D printer software. Modified to the dimensions and setup of the PL Robot Scanner implemented in the project.

### Setup Instructions

1. **Download the FLI API:** Please download the proprietary First Light Imaging (FLI) API from their [website](https://andor.oxinst.com/downloads/view/first-light-imaging-sdk-installer) (user login required).
2. **Add FLI API to Work Folder:** Add the downloaded FLI API to the work folder to use the main script `PLRobot.py`.
3. Connect gantry and FLI C-RED 3 camera according to the thesis instructions.
4. Run `PLRobot.py`. Output images will be in the `Images`folder
(OPTIONAL) 5. If necessary, `Marlin-2.1.2.5-PLRobot`firmware can be updated or flashed with PlatformIO and and the `platformio.ino` file in the custom Marlin folder.

### License

This project is licensed under ????

The `Marlin-2.1.2.5-PLRobot` branch is a custom version of the Marlin 3D printer software specifically for this project. It is licensed under the [GPL license](Marlin-2.1.2.5-PLRobot/LICENSE), requiring open access to modifications ▋
