# HashGuard — Open-Source Windows Utility

Privacy-friendly Windows SHA-256 file hashing and checksum verification utility.

[![Automated tests](https://github.com/amirhoseinteras/hashguard-desktop/actions/workflows/tests.yml/badge.svg)](https://github.com/amirhoseinteras/hashguard-desktop/actions/workflows/tests.yml)
[Download latest](https://github.com/amirhoseinteras/hashguard-desktop/releases/latest) · [Source code](https://github.com/amirhoseinteras/hashguard-desktop) · [Issues](https://github.com/amirhoseinteras/hashguard-desktop/issues)

**Version:** 1.0.0 · **Platform:** Windows · **License:** MIT

## Features
- Compute a SHA-256 digest for local files.
- Compare the digest against an expected SHA-256 checksum.
- Works offline without accounts or analytics.
- Choose an installer or a portable Windows package.

## Download for Windows

| Package | Download | Usage |
| --- | --- | --- |
| Installer | [HashGuard-Setup.exe](https://github.com/amirhoseinteras/hashguard-desktop/releases/latest/download/HashGuard-Setup.exe) | Install with Start Menu shortcut and uninstaller for the current user |
| Portable | [HashGuard-Portable.zip](https://github.com/amirhoseinteras/hashguard-desktop/releases/latest/download/HashGuard-Portable.zip) | Unzip and launch HashGuard.exe; no installation |
| Checksums | [SHA256SUMS.txt](https://github.com/amirhoseinteras/hashguard-desktop/releases/latest/download/SHA256SUMS.txt) | Verify the downloaded files |

**Important:** Release files are unsigned; Windows SmartScreen may display a warning. Check the source and published hashes before trusting an executable. Do not disable your security software to bypass warnings.

### Check download integrity

~~~powershell
Get-FileHash .\HashGuard-Setup.exe -Algorithm SHA256
~~~
Compare the output with the corresponding line of SHA256SUMS.txt from the same release.

## Requirements & limitations

A hash match confirms file integrity relative to the supplied checksum, but does not establish who published a file or whether its contents are safe.

## Run from source

Windows and Python 3.10+ with Tkinter are required.

~~~powershell
python -m pip install -r requirements.txt
python hashguard.py
python -m unittest discover -s tests -v
~~~

The source tree includes build_windows.py and packaging/installer.py for reproducible Windows packaging.

## Support and development

- [Security](SECURITY.md) · [License](LICENSE) · [Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md)
- [Report bugs or request features](https://github.com/amirhoseinteras/hashguard-desktop/issues). Provide the OS version, steps, and expected/actual results.
- No telemetry or account is needed for these offline tools. The source code provides the authoritative feature specification.

## فارسی — راهنمای دانلود

**HashGuard** برنامه‌ای متن‌باز و رایگان برای ویندوز است. فایل Setup برای نصب و نسخه Portable ZIP برای اجرا بدون نصب ارائه شده است.
نسخه‌های اجرایی امضای دیجیتال ندارند. مقدار SHA-256 هر فایل را با فایل SHA256SUMS.txt داخل همان انتشار مقایسه کنید.

---
**Repository:** https://github.com/amirhoseinteras/hashguard-desktop · **Releases:** https://github.com/amirhoseinteras/hashguard-desktop/releases