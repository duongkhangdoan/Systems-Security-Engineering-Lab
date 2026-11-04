# Systems Security Engineering & Risk Assessment Lab

## Project Overview

A hands-on cybersecurity lab designed to simulate a sensor data processing system and apply fundamental Systems Security Engineering practices.

The project focuses on secure data processing, message authentication, threat modeling, software assurance, vulnerability assessment, and software supply chain security.

**Environment:** Ubuntu Linux, Python, Git

## Project Architecture

```text
Sensor Simulator
       |
       | JSON Sensor Data + HMAC
       v
Sensor Processor
       |
       |-- HMAC Verification
       |-- Input Validation
       |-- Security Logging
       v
Accept / Reject Message
```

## Security Implementation

### 1. Sensor Data Simulation

Developed a Python-based sensor simulator to generate sample sensor data for security testing.

### 2. HMAC Authentication

Implemented HMAC-based message authentication using Python's `hmac` and `hashlib` libraries.

- Generate message authentication codes using a shared secret key.
- Verify message integrity and authenticity.
- Detect unauthorized modification of authenticated sensor data.

### 3. STRIDE Threat Modeling

Applied the STRIDE framework to identify potential threats involving spoofing, tampering, repudiation, information disclosure, denial of service, and elevation of privilege.

See [Threat Model](threat_model.md).

### 4. Security Risk Assessment

Documented identified security risks, potential impacts, and mitigation strategies.

See [Risk Assessment](risk_assessment.md).

### 5. Software Assurance — Bandit

Performed Static Application Security Testing (SAST) on Python source code.

**Final result:** 0 reported security findings.

### 6. Software Supply Chain Security — CycloneDX

Generated a Software Bill of Materials (SBOM) for the Python virtual environment.

**Result:** 49 identified components, including development tooling.

### 7. Dependency Vulnerability Assessment — pip-audit

- Initial scan: 12 vulnerability entries affecting `pip 25.1.1`.
- Remediation: Upgraded `pip` to version 26.3.
- Final verification: No known vulnerabilities found.

## Security Reports

| File | Description |
|---|---|
| `SECURITY_ASSESSMENT.md` | Overall security assessment |
| `threat_model.md` | STRIDE threat modeling |
| `risk_assessment.md` | Security risk analysis |
| `bandit_report.json` | Static analysis results |
| `sbom.json` | CycloneDX SBOM |
| `pip_audit_report.json` | Dependency vulnerability audit |

## Tools & Technologies

- Python
- Ubuntu Linux
- HMAC / SHA-based cryptographic hashing
- STRIDE Threat Modeling
- Bandit (SAST)
- CycloneDX (SBOM)
- pip-audit
- Git / GitHub

## Security Considerations

The HMAC secret key is excluded from version control using `.gitignore`.

This lab uses simulated data and is intended for educational and portfolio purposes. Security scan results do not guarantee the absence of vulnerabilities.

## Key Learning Outcomes

- Implemented and tested message authentication.
- Practiced security threat modeling and risk assessment.
- Performed static source code analysis.
- Generated and reviewed a software bill of materials.
- Identified, remediated, and verified known dependency vulnerabilities.
- Documented security findings and engineering decisions.
