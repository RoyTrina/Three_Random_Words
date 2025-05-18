# Three Random Words

![App Icon](App_Icon.jpg)

A comprehensive multifactor authentication system

## Overview

Three Random Words is a secure authentication system that emerged from a family discussion about device security. The
project aims to provide robust yet user-friendly authentication methods for various devices.

## Features

The system supports four authentication methods:

- Username and password authentication
- PIN-based quick access
- Facial recognition
- Voice verification

## How It Works

### Registration Process

New users must complete a one-time registration that includes:

1. Creating username and password
2. Setting up a PIN
3. Capturing facial data
4. Recording voice sample

### Authentication Methods

#### 1. Username and Password

- Traditional login method
- Secure password requirements
- Fall-back authentication option

#### 2. PIN Authentication

- Quick access option
- Numeric PIN-based security
- Suitable for frequent access needs

#### 3. Facial Recognition

- Powered by DeepFace technology
- Real-time face detection using OpenCV
- Secure biometric verification

#### 4. Voice Recognition

- Implemented using SpeechRecognition library
- Voice pattern matching
- Contact-free authentication option

## Technical Stack

- **GUI Framework**: PyQt5
- **Database**: MySQL
- **Key Dependencies**:
    - [DeepFace](https://github.com/serengil/deepface) - Facial recognition
    - [OpenCV—](https://github.com/opencv/opencv)Computer vision
    - [SpeechRecognition](https://github.com/Uberi/speech_recognition) - Voice processing
