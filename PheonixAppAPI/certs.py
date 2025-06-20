"""Certificates ..."""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CERTIFICATES = os.path.join(BASE_DIR, "certificates")
CA_BUNDLE_PATH = os.path.join(CERTIFICATES, "ca-bundle.crt")
