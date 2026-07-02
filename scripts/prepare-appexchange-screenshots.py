#!/usr/bin/env python3
"""Create AppExchange-ready screenshots without modifying docs originals.

Requirements: 1500x1000 px, PNG or JPEG, <= 1 MB.
Uses letterboxing so wide Salesforce captures are not center-cropped.

Usage (from repo root):
  python3 -m venv .venv-appexchange
  .venv-appexchange/bin/pip install Pillow
  .venv-appexchange/bin/python scripts/prepare-appexchange-screenshots.py
"""

from __future__ import annotations

import io
from pathlib import Path

from PIL import Image

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC = REPO_ROOT / "static/img/screenshots"
DST = REPO_ROOT / "static/img/appexchange"

TARGET_W, TARGET_H = 1500, 1000
MAX_BYTES = 1024 * 1024
PAD_COLOR = (243, 243, 243)  # Salesforce Lightning page gray

# Output name, source filename, optional caption for listing upload notes
SCREENSHOTS = [
    ("01-cpq-hub-quotes.png", "cpq-by-opportunity-quote-saved.png", "Cotiza CPQ hub with quotes, proposals, and contracts for an Opportunity"),
    ("02-playbook-quoting.png", "cpq-playbook-questions.png", "Playbook-driven quote configuration with guided questions"),
    ("03-approvals-hub.png", "cpq-approvals-hub.png", "Cotiza CPQ Approvals hub for submitters and approvers"),
    ("04-generate-proposal.png", "generate-proposal.png", "Generate branded proposal documents from quote data"),
    ("05-proposals-list.png", "proposals-list.png", "Proposals table with generated customer documents"),
    ("06-contract-actions.png", "action-contracts.png", "Amend, Replace, and Renew actions on Account Contracts"),
    ("07-account-contracts.png", "account-contracts-most-active-contract.png", "Account Contracts tab with most active contract snapshot"),
    ("08-approval-workflow.png", "cpq-playbook-approval-needed.png", "Approval Summary triggered by Playbook rules"),
    ("09-create-contract.png", "opportunity-create-contract.png", "Create Contract from a synced, approved Quote"),
    ("10-playbook-rules.png", "playbook-rule-rule-actions.png", "Declarative Playbook Rules and automation actions"),
    ("11-view-sections.png", "playbook-view-section.png", "Configure proposal PDF layout with View Sections"),
    ("12-native-app-launcher.png", "app-launcher-Cotiza-CPQ.png", "Cotiza CPQ Lightning app in the App Launcher"),
    # Optional extras if you want the full 15-slot maximum
    ("13-opportunity-record-page.png", "opp-record-page-cpq-container.png", "Cotiza CPQ Container embedded on an Opportunity record page"),
    ("14-product-summary.png", "quote-products-summary.png", "Quote line items and product summary"),
    ("15-scenario-criteria.png", "playbook-scenario-criteria.png", "Playbook Scenarios with flexible AND/OR criteria"),
]


def fit_with_padding(im: Image.Image) -> Image.Image:
    canvas = Image.new("RGB", (TARGET_W, TARGET_H), PAD_COLOR)
    im = im.convert("RGBA")
    scale = min(TARGET_W / im.width, TARGET_H / im.height)
    new_size = (max(1, int(im.width * scale)), max(1, int(im.height * scale)))
    resized = im.resize(new_size, Image.Resampling.LANCZOS)
    x = (TARGET_W - new_size[0]) // 2
    y = (TARGET_H - new_size[1]) // 2
    canvas.paste(resized, (x, y), resized)
    return canvas


def save_under_limit(im: Image.Image, out_path: Path) -> tuple[Path, int, str]:
    attempts = [
        ("PNG", {"optimize": True, "compress_level": 9}, ".png"),
        ("JPEG", {"quality": 92, "optimize": True, "subsampling": 0}, ".jpg"),
        ("JPEG", {"quality": 85, "optimize": True}, ".jpg"),
        ("JPEG", {"quality": 78, "optimize": True}, ".jpg"),
    ]
    for fmt, kwargs, ext in attempts:
        path = out_path.with_suffix(ext)
        buf = io.BytesIO()
        save_im = im if fmt == "PNG" else im.convert("RGB")
        save_im.save(buf, format=fmt, **kwargs)
        data = buf.getvalue()
        if len(data) <= MAX_BYTES:
            path.write_bytes(data)
            return path, len(data), fmt
    path = out_path.with_suffix(".jpg")
    im.convert("RGB").save(path, format="JPEG", quality=70, optimize=True)
    return path, path.stat().st_size, "JPEG"


def main() -> None:
    DST.mkdir(parents=True, exist_ok=True)
    print(f"Writing AppExchange screenshots to {DST.relative_to(REPO_ROOT)}/\n")
    for out_name, src_name, _caption in SCREENSHOTS:
        src = SRC / src_name
        if not src.exists():
            raise FileNotFoundError(src)
        im = Image.open(src)
        fitted = fit_with_padding(im)
        out_base = DST / Path(out_name).stem
        path, size, fmt = save_under_limit(fitted, out_base)
        print(f"{path.name:35} <- {src_name:45} {size/1024:6.0f} KB {fmt}")


if __name__ == "__main__":
    main()
