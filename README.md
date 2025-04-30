# PCB Defect Detection Demo

![PCB Defect Detection](https://img.shields.io/badge/Computer%20Vision-Quality%20Control-blue)
![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13.0-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8.0-red)

A web application that demonstrates how machine learning and computer vision can be used to detect defects in printed circuit boards (PCBs). This project is intended for educational purposes to show how computers can help in manufacturing quality control.

![Example Detection](static/img/demo_screenshot.jpg)

## Overview

This application allows users to upload images of PCBs and uses computer vision techniques to classify them into different defect categories:

1. **Missing Hole** - A hole that should be present is missing
2. **Mouse Bite** - Part of the copper is damaged, creating a bite-like appearance
3. **Open Circuit** - A break in the circuit path that should be connected
4. **Short** - Unintended connection between two points
5. **Spur** - Unwanted projection from a conductor
6. **Spurious Copper** - Unwanted copper remnants in areas that should be clear
7. **Normal** - No defect detected

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/pcb-defect-detection.git
   cd pcb-defect-detection
   ```

2. Create and activate a virtual environment (recommended):
   ```
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the setup script:
   ```
   python setup_project.py
   ```
   
   This will:
   - Create the necessary directory structure
   - Generate synthetic PCB images for testing
   - Create a dummy model for demonstration

5. Run the application:
   ```
   python app.py
   ```

6. Open your browser and navigate to `http://localhost:5000`

### Using the Application

1. **Upload an Image**: Click the "Choose File" button and select a PCB image
2. **Analyze**: Click the "Analyze PCB" button to process the image
3. **View Results**: See the detection results, including:
   - Detected defect type (if any)
   - Confidence level
   - Information about the defect
   - Recommended action
4. **View Feature Detection**: For advanced users, click "View Feature Detection" to see how the image is processed

## How It Works

The application uses several computer vision techniques to detect PCB defects:

1. **Preprocessing**: The uploaded image is resized and normalized
2. **Feature Extraction**: 
   - Contour detection to identify PCB components
   - Edge detection to find traces and connections
   - Circle detection to locate holes
3. **Classification**: Features are analyzed to determine the most likely defect type
4. **Visualization**: Detection results are displayed with feature highlighting

In a production environment, this would be enhanced with deep learning models trained on thousands of labeled PCB images.

## Dataset

This demo is inspired by the PCB defects dataset which contains: `https://www.kaggle.com/datasets/akhatova/pcb-defects`
- 1386 images with 6 types of defects
- Each defect is annotated with bounding boxes
- The dataset simulates real manufacturing defects in PCBs

For educational purposes, this demo uses synthetic images, but the concepts apply to real-world PCB inspection.

## 📝 Future Enhancements

Here are some ways this project could be extended:

1. **Real ML Model**: Train an actual deep learning model on a PCB defect dataset
2. **Object Detection**: Implement localization to identify where defects occur on the PCB
3. **Multiple Defect Detection**: Detect multiple defects in a single image
4. **Real-time Video Analysis**: Analyze PCBs from a webcam or video feed
5. **Detailed Analytics**: Track defect statistics and generate reports

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/awesome-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add awesome feature'`)
5. Push to the branch (`git push origin feature/awesome-feature`)
6. Open a Pull Request


## 🙏 Acknowledgments

- Based on PCB defect detection research in manufacturing
- Inspired by automated optical inspection (AOI) systems used in electronics manufacturing
- Created for educational purposes to demonstrate computer vision applications