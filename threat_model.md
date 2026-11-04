
# Sensor System – STRIDE Threat Model

## 1. System Overview

This project simulates a sensor system using Python.

Components:
- Sensor Simulator
- JSON Data Storage
- Sensor Processor
- HMAC Secret Key
- Security Logging

## 2. Security Objectives

- Protect sensor data integrity
- Authenticate messages using HMAC-SHA256
- Detect unauthorized data modification
- Record security events
- Prevent unauthorized access to secret keys

## 3. STRIDE Threat Analysis

| ID | Threat | Description | Mitigation |
|---|---|---|---|
| S-01 | Spoofing | Attacker impersonates a sensor | HMAC authentication and sensor identity management |
| T-01 | Tampering | Attacker modifies sensor data | HMAC-SHA256 verification |
| R-01 | Repudiation | Attacker denies modifying data | Protected security logs and audit trails |
| I-01 | Information Disclosure | Secret key is exposed | Restrictive file permissions and secure key storage |
| D-01 | Denial of Service | Sensor data file is deleted or corrupted | Error handling, backups, and availability monitoring |
| E-01 | Elevation of Privilege | Attacker gains unauthorized privileges | Least privilege and access controls |

## 4. Implemented Security Controls

- Input validation
- HMAC-SHA256 message authentication
- Security event logging
- Secret key file permissions

## 5. Remaining Security Gaps

- No replay attack protection
- No per-sensor key management
- No centralized security logging
- No network transport security
- No automated recovery from data loss
