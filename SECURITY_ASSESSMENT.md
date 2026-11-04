# Systems Security Engineering — Security Assessment Report

## 1. Project Overview

This project simulates a sensor data processing system to demonstrate fundamental Systems Security Engineering practices, including message authentication, threat modeling, software assurance, and software supply chain security.

The lab was developed in a controlled environment for educational purposes.

## 2. Security Controls

The following security controls were implemented:

- **HMAC Authentication:** Uses a shared secret key to verify message integrity and authenticity.
- **Input Validation:** Validates incoming sensor data before processing.
- **Security Logging:** Records security-related events for troubleshooting and investigation.
- **Secrets Management:** Excludes the HMAC secret key from Git version control.

## 3. Threat Modeling

The STRIDE methodology was used to identify potential security threats:

- Spoofing
- Tampering
- Repudiation
- Information Disclosure
- Denial of Service
- Elevation of Privilege

Threats and mitigation strategies are documented in `threat_model.md`.

## 4. Software Assurance — Bandit

Bandit was used to perform Static Application Security Testing (SAST) on the Python source code.

**Final scan results:**
- Security findings: 0
- Scan report: `bandit_report.json`

## 5. Software Supply Chain Security

CycloneDX was used to generate a Software Bill of Materials (SBOM).

**Results:**
- Components identified: 49
- SBOM format: CycloneDX JSON
- Report: `sbom.json`

The SBOM represents the Python virtual environment, including development and security tooling dependencies.

## 6. Dependency Vulnerability Assessment

`pip-audit` was used to identify publicly reported vulnerabilities in installed Python packages.

**Initial findings:**
- 12 reported vulnerability entries affecting `pip 25.1.1`.

**Remediation:**
- Upgraded `pip` from version 25.1.1 to 26.3.

**Verification:**
- Final result: No known vulnerabilities found.
- Report: `pip_audit_report.json`

## 7. Residual Risks and Limitations

- HMAC does not encrypt sensor data.
- A compromised HMAC key could allow attackers to forge authenticated messages.
- The current lab does not establish protection against replay attacks.
- Static analysis cannot detect every software vulnerability.
- Dependency auditing is limited to known vulnerabilities and available advisory data.
- The environment SBOM includes development tools and does not exclusively represent application dependencies.

## 8. Conclusion

This project demonstrates hands-on experience with:

- Systems Security Engineering
- HMAC Message Authentication
- STRIDE Threat Modeling
- Security Risk Assessment
- Static Application Security Testing
- Software Bill of Materials Generation
- Dependency Vulnerability Scanning
- Vulnerability Remediation and Verification

The lab provides a foundation for further learning in Software Assurance, Supply Chain Risk Management, and secure systems engineering.
