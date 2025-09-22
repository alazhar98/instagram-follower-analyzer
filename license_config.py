"""
Local license configuration for Instagram Follower Analyzer Pro.

This is a simple, offline license check. Replace the keys below with
your real issued license keys or integrate with a remote validator.
"""

from __future__ import annotations

from typing import Set

# Placeholder keys for demonstration. Replace with real keys.
VALID_LICENSE_KEYS: Set[str] = {
    "IFA-PRO-TRIAL-1234-5678",
    "IFA-PRO-XXXX-YYYY-ZZZZ",
}


def is_license_valid(license_key: str) -> bool:
    """Return True if license key is in the local allowlist."""
    normalized = (license_key or "").strip()
    return normalized in VALID_LICENSE_KEYS


