# Real-time Quality Control System for Roll-to-Roll Lithium-Ion Battery Production

A prototype system for real-time monitoring of critical parameters in roll-to-roll lithium-ion battery manufacturing.

## Problem

Traditional manufacturing quality control often relies on manual and periodic sampling. This can delay the detection of abnormal production conditions and may affect productivity and quality-control efficiency.

This project aims to provide a real-time monitoring approach for:

- Temperature
- Humidity
- Ion concentration in electrolyte solution

## Objectives

- Enable real-time monitoring of critical production parameters.
- Develop an IoT-based sensor monitoring system.
- Detect abnormal conditions using Machine Learning.
- Explore edge computing and cloud-based analytics for manufacturing systems.

## Current Implementation

The current prototype includes:

- FastAPI backend
- Sensor data API
- Sensor data validation using Pydantic
- Machine Learning anomaly detection using Isolation Forest
- Basic project structure for future IoT and dashboard integration

## System Flow

```text
IoT Sensors
     ↓
Raspberry Pi
     ↓
Python Backend
     ↓
Machine Learning
     ↓
Real-time Dashboard