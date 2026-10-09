# HashGuard for Windows

Calculate SHA-256 hashes for local files and verify them against an expected checksum.

**Version:** 1.0.0. Works fully offline, with no accounts or analytics.

## Download / دانلود

Use GitHub Releases: **HashGuard-Setup.exe** to install (Start Menu, desktop shortcut, uninstall) or **HashGuard-Portable.zip** to run without installing. Both builds are unsigned. Windows SmartScreen can warn about unsigned programs.

## Run from source

Requires Windows and Python 3.10+ with Tkinter. Run: python hashguard.py

## Important

No network or API; checking a hash does not prove a publisher's identity.

## License / مشارکت

MIT for original source code. Bug reports, translations and genuine contributions are welcome. Do not submit fake stars, downloads, or meaningless pull requests.

## Reproducible Windows builds

Install Python 3.10+, run 'python -m pip install -r requirements.txt pyinstaller' then 'python build_windows.py'. Outputs are under dist/. The installer provides per-user installation and uninstall; it never requires administrator access.
