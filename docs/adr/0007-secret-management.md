# ADR-0007: Secret management via a `SecretProvider` port

- **Status:** Accepted
- **Date:** 2026-11-14

## Context
Kalshi authenticates with an API key ID plus a private key that signs every request (RSA-PSS). Whoever holds the private key can trade the account. The bot runs locally now and on AWS later.

## Decision
- Define a `SecretProvider` protocol with `get(name) -> SecretStr`.
  - v1: `KeychainSecretProvider` (OS keychain via `keyring`).
  - Later: `AwsSecretsManagerProvider` (KMS-encrypted, IAM-scoped).
- **Forbidden:** private keys in `.env` files, environment variables, CLI arguments, config files, or the repo.
- The private key is loaded into memory only inside the `executor` signer, held as `SecretStr`, and never logged, serialized, or included in exceptions.
- The logging pipeline applies a redaction filter for key material and signature headers.
- Separate keys for demo and production (Kalshi does not share credentials between environments). Keychain entries are namespaced by environment.
- A `uatu secrets set` command writes to the keychain from a file path or stdin, then reminds the user to delete the plaintext source.

## Consequences
- Moving to AWS is a new provider class, not a refactor.
- Key rotation means replacing one keychain entry.
- Developers must use the CLI to set up secrets, a small cost for removing a whole class of leaks.
