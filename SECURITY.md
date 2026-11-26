# Security Policy

## Reporting a vulnerability
Please report vulnerabilities privately via GitHub's **Security → Report a vulnerability** on this repository. Do not open public issues for security problems.

## Scope
Of particular interest: anything that could leak signing keys, bypass human approval, bypass risk gates, or cause orders to be sent to the production environment unintentionally.

## Handling secrets
This project never reads private keys from environment variables, `.env` files, or the repository. See [ADR-0007](docs/adr/0007-secret-management.md).
