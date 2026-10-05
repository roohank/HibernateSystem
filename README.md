# HibernateSystem

An NVDA add-on that hibernates the Windows system with a single keyboard shortcut.

**Repository:** [https://github.com/roohank/HibernateSystem](https://github.com/roohank/HibernateSystem)

## Features

- Hibernates the system instantly with a keyboard shortcut.
- Runs silently in the background without freezing NVDA.
- Provides audio feedback to the user via NVDA's speech.

## Keyboard Shortcut

| Key Combination | Action |
|---|---|
| `NVDA + Alt + H` | Hibernate the system |

## Requirements

- NVDA version 2019.3 or later.
- Windows 10 or Windows 11.
- The Hibernate feature must be enabled in Windows. Run `powercfg /hibernate on` as administrator to enable it.

## Installation

1. Download the latest `HibernateSystem.nvda-addon` file from the [Releases](https://github.com/roohank/HibernateSystem/releases) page.
2. Press `Enter` on the file or double-click it.
3. Follow the on-screen instructions in NVDA to install the add-on.
4. Restart NVDA when prompted.

## Usage

Press `NVDA + Alt + H` at any time. NVDA will announce:

> "Hibernating the system..."

Then the system will hibernate.

## Building from Source

If you want to build the add-on yourself:

1. Clone this repository:

   ```bash
   git clone https://github.com/roohank/HibernateSystem.git
2. 
Make sure the folder structure looks like this:
HibernateSystem/
├── manifest.ini
├── README.md
├── LICENSE
└── globalPlugins/
    └── hibernate.py