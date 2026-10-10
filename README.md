# HibernateSystem

An NVDA add-on that hibernates the Windows system with a single keyboard shortcut.

**Repository:** [https://github.com/roohank/HibernateSystem](https://github.com/roohank/HibernateSystem)

## Features

- Hibernates the system instantly with a keyboard shortcut.
- Runs silently in the background without freezing NVDA.
- Provides audio feedback via NVDA's speech.
- Uses a conflict-free default shortcut (`NVDA + Shift + Control + H`) that can be customized by the user.

## Keyboard Shortcut

| Key Combination | Action |
|---|---|
| `NVDA + Shift + Control + H` | Hibernate the system |

## How to Use

Press `NVDA + Shift + Control + H` at any time. NVDA will announce "Hibernating the system..." and then the system will hibernate.

### Changing the Shortcut

If you prefer a different key combination:

1. Open the NVDA menu (`NVDA + N`).
2. Go to **Preferences** → **Input Gestures**.
3. In the tree view, find **HibernateSystem**.
4. Select **Hibernate the system**.
5. Click **Add**, press your desired key combination, and confirm.
6. Click **OK**.

## Requirements

- NVDA version 2019.3 or later.
- Windows 10 or Windows 11.
- The Hibernate feature must be enabled in Windows. Run `powercfg /hibernate on` as administrator to enable it.

## Installation

1. Download the latest `HibernateSystem.nvda-addon` file from the [Releases](https://github.com/roohank/HibernateSystem/releases) page.
2. Press `Enter` on the file or double-click it.
3. Follow the on-screen instructions in NVDA to install the add-on.
4. Restart NVDA when prompted.

## Building from Source

If you want to build the add-on yourself:

1. Clone this repository:

   ```bash
   git clone https://github.com/roohank/HibernateSystem.git
2. 
Make sure the folder structure looks like this:
text
Copy
Download
HibernateSystem/
├── manifest.ini
├── README.md
├── LICENSE
├── doc/
│   └── en/
│       └── readme.html
└── globalPlugins/
    └── hibernate.py
3. 
Select manifest.ini, doc, and the globalPlugins folder.
4. 
Right-click → Send to → Compressed (zipped) folder.
5. 
Rename the resulting .zip file to HibernateSystem.nvda-addon.
License
This add-on is released under the GNU General Public License v2.0. See the LICENSE file for details.
Author
• 
Roohan — GitHub: @roohank
Changelog
Version 1.1
• 
Translated UI messages from Persian to English.
• 
Changed the default shortcut from NVDA+Alt+H to NVDA+Shift+Control+H to avoid conflicts with NVDA's Remote Access.
• 
Updated documentation.
Version 1.0
• 
Initial release.