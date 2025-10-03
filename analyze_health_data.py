#!/usr/bin/env python3
"""
Health Sensor Data Analysis Script

Complete the TODO sections to analyze health sensor data using NumPy.
This script demonstrates basic NumPy operations for data loading, statistics,
filtering, and report generation.
"""

import numpy as np
def load_data(filename):
    """Load CSV data using NumPy.
    
    Args:
        filename: Path to CSV file
        
    Returns:
        NumPy structured array with all columns
    """
    # This code is provided (np.genfromtxt not covered in lecture)
    dtype = [('patient_id', 'U10'), ('timestamp', 'U20'),
             ('heart_rate', 'i4'), ('blood_pressure_systolic', 'i4'),
             ('blood_pressure_diastolic', 'i4'), ('temperature', 'f4'),
             ('glucose_level', 'i4'), ('sensor_id', 'U10')]
    
    data = np.genfromtxt(filename, delimiter=',', dtype=dtype, skip_header=1)
    return data

# Args:
#  data: NumPy structured array
        
    # Returns:
    #     Dictionary with statistics
        
    # Calculate and return:
    # - Average heart rate (use .mean())
    # - Average systolic BP (use .mean())
    # - Average glucose level (use .mean())
    # - Return as dictionary
    # - Format values with f-strings using .1f

def calculate_statistics(data):
    """Calculate basic statistics for numeric columns."""
    stats = {
        'avg_heart_rate': float(f"{data['heart_rate'].mean():.1f}"),
        'avg_systolic_bp': float(f"{data['blood_pressure_systolic'].mean():.1f}"),
        'avg_glucose': float(f"{data['glucose_level'].mean():.1f}")
    }
    return stats

# def find_abnormal_readings(data):
#     """Find readings with abnormal values.
    
#     Args:
#         data: NumPy structured array
        
#     Returns:
#         Dictionary with counts
        
#     TODO: Count readings where:
#     - Heart rate > 90 (use boolean indexing)
#     - Systolic BP > 130 (use boolean indexing)
#     - Glucose > 110 (use boolean indexing)
#     - Return dictionary with counts
#     """

def find_abnormal_readings(data):
    """Find readings with abnormal values."""
    abnormal = {
        'high_heart_rate': (data['heart_rate'] > 90).sum(),
        'high_blood_pressure': (data['blood_pressure_systolic'] > 130).sum(),
        'high_glucose': (data['glucose_level'] > 110).sum()
    }
    return abnormal

# def generate_report(stats, abnormal, total_readings):
#     """Generate formatted analysis report.
    
#     Args:
#         stats: Dictionary of statistics
#         abnormal: Dictionary of abnormal counts
#         total_readings: Total number of readings
        
#     Returns:
#         Formatted string report
        
#     TODO: Create a formatted report string using f-strings
#     - Include all statistics with proper formatting
#     - Use .1f for decimal numbers
#     - Make it readable and well-formatted
#     """

def generate_report(stats, abnormal, total_readings):
    """Generate formatted analysis report."""
    report = f"""Health Sensor Data Analysis Report

Dataset Summary:
- Total readings: {total_readings}

Average Measurements:
- Heart Rate: {stats['avg_heart_rate']:.1f} bpm
- Systolic BP: {stats['avg_systolic_bp']:.1f} mmHg
- Glucose Level: {stats['avg_glucose']:.1f} mg/dL

Abnormal Readings:
- High Heart Rate (>90): {abnormal['high_heart_rate']} readings
- High Blood Pressure (>130): {abnormal['high_blood_pressure']} readings
- High Glucose (>110): {abnormal['high_glucose']} readings
"""
    return report

# def save_report(report, filename):
#     """Save report to file.
    
#     Args:
#         report: Report string
#         filename: Output filename
        
#     TODO: Write the report to a file
#     """

def save_report(report, filename):
    """Save report to file."""
    with open(filename, 'w') as f:
        f.write(report)


# def main():
#     """Main execution function.
    
#     TODO: Orchestrate the analysis:
#     1. Load the data from 'health_data.csv'
#     2. Calculate statistics
#     3. Find abnormal readings
#     4. Calculate total readings using len(data)
#     5. Generate report with all three parameters
#     6. Save to 'output/analysis_report.txt'
#     7. Print success message
#     """

def main():
    """Main execution function."""
    # 1. Load data
    data = load_data('health_data.csv')
    
    # 2. Calculate statistics
    stats = calculate_statistics(data)
    
    # 3. Find abnormal readings
    abnormal = find_abnormal_readings(data)
    
    # 4. Total readings
    total_readings = len(data)
    
    # 5. Generate report
    report = generate_report(stats, abnormal, total_readings)
    
    # 6. Save report
    save_report(report, 'output/analysis_report.txt')
    
    # 7. Success message
    print("Analysis complete! Report saved to output/analysis_report.txt")


if __name__ == "__main__":
    main()