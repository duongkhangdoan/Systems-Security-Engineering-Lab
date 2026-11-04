
# Sensor System – Security Risk Assessment

## Risk Scoring Method

Risk Score = Likelihood × Impact

Likelihood: 1 (Rare) to 5 (Very Likely)
Impact: 1 (Minor) to 5 (Critical)

Risk Levels:
- Low: 1–5
- Medium: 6–10
- High: 11–15
- Critical: 16–25

## Risk Register

| ID | Threat | Likelihood | Impact | Score | Level |
|---|---|---:|---:|---:|---|
| S-01 | Sensor Spoofing | 3 | 4 | 12 | High |
| T-01 | Data Tampering | 4 | 5 | 20 | Critical |
| R-01 | Repudiation | 2 | 3 | 6 | Medium |
| I-01 | Secret Key Exposure | 3 | 5 | 15 | High |
| D-01 | Denial of Service | 3 | 4 | 12 | High |
| E-01 | Privilege Escalation | 2 | 5 | 10 | Medium |

## Risk Mitigation Priorities

1. Protect sensor data integrity with HMAC-SHA256.
2. Secure secret keys using access controls.
3. Strengthen security logging and monitoring.
4. Implement replay attack protection.
5. Improve availability and recovery mechanisms.

## Assessment Notes

The likelihood and impact scores are illustrative
estimates for this simulated environment.

Implemented controls include HMAC verification,
input validation, logging, and file permissions.

Remaining risks require additional security controls
and testing.

