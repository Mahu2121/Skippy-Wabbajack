# Skippy-Wabbajack

Skippy-Wabbajack is a small Python automation script that repeatedly looks for on-screen images and clicks them when found.

This project is based on the wabbajack-skip repository.

It was created to help skip repetitive prompts in Wabbajack-like workflows by detecting a primary image (`reference.png`) and, if needed, a fallback image (`reference_alt.png`).

## Features

- Repeated image detection and automatic click.
- Primary and fallback reference images.
- Configurable delays in `settings.ini`.
- Windows alert sound when neither image appears on screen.

## Requirements

- Windows (current script uses `winsound` for alerts).
- Python 3.9+ recommended.
- Python packages:
	- `pyautogui`
	- `opencv-python`
	- `pillow`

Install dependencies:

```bash
pip install pyautogui opencv-python pillow
```

## Project Files

- `main.py`: Main automation loop.
- `settings.ini`: Optional timing configuration.
- `reference.png`: Primary image target (you need to provide this file).
- `reference_alt.png`: Secondary image target (you need to provide this file).

## Configuration

Edit `settings.ini`:

```ini
[SETTINGS]
delay_between_tries = 0.5
delay_after_succeding = 8
delay_after_failing = 5
```

Parameter meanings:

- `delay_between_tries`: Wait time between each scan attempt.
- `delay_after_succeding`: Wait time after a successful click.
- `delay_after_failing`: Wait time after both images fail to match.

If a value is missing, `main.py` uses its internal defaults.

## Usage

1. Place `reference.png` and `reference_alt.png` in the same folder as `main.py`.
2. Open the target app/window you want to automate.
3. Run:

```bash
python main.py
```

The script runs in an infinite loop until you stop it.

## Stop the Script

- Press `Ctrl + C` in the terminal.

## Notes

- Keep your screen resolution/scaling consistent with how the reference images were captured.
- If matching is unstable, retake cleaner reference screenshots.
- The script currently uses a fixed image confidence value (`0.6`) in code.
"# Skippy-Wabbajack" 
