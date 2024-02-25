<!-- # Smart-Lighting -->
# Automated Street Lights & Enhanced Security System

## Overview
This repository hosts the codebase and details for an integrated system that combines automated street lights with an advanced security solution, focusing on ensuring the safety of the public on less frequented or less accessible roads. The project aims to detect if police intervention is needed by analyzing audio data and inferring distress signals.

### Tech Stack:
- **Web Technologies (HTML, CSS, JS)**
- **Backend (Node.js, Firebase)**
- **Microcontrollers (ESP32, ESPNow Protocol)**
- **ML Models (n_gram vectorizer, logistic regression model)**
- **Data Communication (Raspberry Pi, ESP32)**
- **Data Storage and Web Interface (Websocket, Website)**

## Features
- **Automated Street Lights:**
  - Motion sensors and LED technology for energy-efficient illumination.
  - Self-diagnostic capabilities for minimizing maintenance requirements.
  - Adaptability to adjust illumination based on environmental conditions.

- **Security Solution:**
  - Initiates audio recording on a button press.
  - Real-time processing to swiftly analyze audio for distress words.
  - Automated alerts to notify authorities upon detecting alarming phrases.

## ML Model
- Using Python's Speech_Recognition module for speech to text conversion.
- Logistic regression model for inference, based on an n-gram approach for vectorization to determine if police intervention is needed.

## Benefits
- **Energy Conservation:**
  - Reduces energy consumption and operational costs.
- **Enhanced Safety Measures:**
  - Swift response to potential threats or emergencies.
- **Privacy Protection:**
  - Selectively triggers alerts based on specific distress signals, respecting privacy.

## Conclusion
This system revolutionizes urban infrastructure, promoting energy efficiency, and addressing safety concerns on less frequented roads. It's a testament to technology's potential in ensuring public safety and a safer, more sustainable future.

### Repository Structure:
- `/src`: Contains the source code for various components.
- `/docs`: Documentation and additional resources.
- `/models`: Stores ML models and related files.

## How to Use
1. Clone the repository.
2. Follow instructions in individual component folders for setup and usage.

## Contributors
- Devansh
- Sharad
- Aditya

Feel free to contribute, report issues, or suggest improvements!
