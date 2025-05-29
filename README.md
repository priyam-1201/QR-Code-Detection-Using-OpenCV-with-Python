# Real_Time_QR-Code-Scanner-and-Generate_Link

## Overview

This project leverages Python's powerful libraries—OpenCV, Pyzbar, and NumPy—to create a robust real-time QR code scanner. It captures video from your webcam, detects QR codes in the live feed, and decodes the embedded data seamlessly. A user-friendly graphical display highlights the decoded data and overlays bounding shapes around the detected QR codes.

### Features
- Real-time QR code detection from your webcam feed.
- Decodes and prints QR code data directly in the terminal.
- Highlights QR codes using bounding quadrilaterals.
- No external dependencies for lens distortion correction.
- Easy-to-use and extensible.

## Prerequisites

Before running the code, make sure you have the following installed:

- Python 3.7+
- OpenCV
- Pyzbar
- Pillow
- NumPy

## Usage

Clone this repository to your local machine:

-bash
git clone https://github.com/yourusername/Python-QR-Code-Detection.git
Navigate to the project directory:

-bash
cd Python-QR-Code-Detection
Run the script:

-bash
python qr_code_detection.py
-> Use your webcam to scan QR codes. Press q to exit.

## How It Works
-Grayscale Conversion: Converts webcam video feed to grayscale for efficient QR code detection.

-QR Code Decoding: Uses Pyzbar to decode QR data and outputs the text in the terminal.

-Bounding Quadrilateral: Detects and draws a quadrilateral around the QR code for visual feedback.

-3D Model Points Projection: Implements 3D model projections for additional feature detection and analysis.

