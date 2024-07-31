<div align="center">
  <img src="https://github.com/Vankimfc0/Boot-image-Extractor/assets/98699436/8fc2fc00-4dcd-4506-a161-7fec49a6ee34" loading="lazy" alt="Boot Image Extractor"/>
<h2></h2>   
</div>


<div style="display: flex; justify-content: center;">
  <div style="max-width: 800px;">
    <p>
      Boot Image Extractor is a standalone Python script designed to extract the boot image from Android devices with root access. It supports both <a href="https://source.android.com/devices/tech/ota/ab">A/B</a> and <a href="https://source.android.com/devices/bootloader/partitions">legacy partition</a> styles. This script was developed as part of an automated method for extracting boot images described in the <a href="https://gist.github.com/Vankimfc0/a1f693b64d8f8701ec24477a2ccaab87#file-boot-image-extraction-guide-md">Boot Image Extraction Guide</a>.
    </p>
  </div>
</div>

## Requirements

- Python 3 or higher
- Root access on the Android device
- Python package: `pyfiglet`

## Initial Setup

1. **Install Termux:**
   Download and install [Termux](https://termux.com/) on your device.

2. **Grant Storage Permissions:**
   Open Termux and allow storage permissions using the command:
   ```bash
   termux-setup-storage
   ```

3. **Check for PHH Superuser (if applicable):**
   If you are going to use this script on a [Phh-based GSI](https://github.com/phhusson/treble_experimentations/wiki/Frequently-Asked-Questions-%28FAQ%29) that ships with an inbuilt [superuser](https://github.com/phhusson/treble_experimentations/wiki/Frequently-Asked-Questions-%28FAQ%29#naming-conventions-that-some-gsi-buildermaintainer-uses), check if the PHH Superuser app is installed:
   ```bash
   (pm list packages | grep me.phh.superuser) && echo "App installed" || echo "Not found"
   ```
   > **Note:** If "Not found" is displayed, install the app from [F-Droid](https://f-droid.org/en/packages/me.phh.superuser/). This app is necessary to grant Termux requests to run as root. Skip this step if your device is already rooted with Magisk or another method.

4. **Grant Superuser Permission:**
   Grant superuser permission to Termux by typing:
   ```bash
   su
   ```

## Installation Instructions

#### Procedure 1: Direct Installation

1. **Run with One-Liner Commands:**
   Copy and paste the following command in termux and hit enter to start running the script:
   ```bash
   apt update && apt upgrade -y; { command -v tsu && command -v curl && command -v python && command -v pip && python -c 'import pyfiglet' &>/dev/null; } || apt install -y tsu curl python; pip install pyfiglet; curl -o boot_image_extractor.py https://raw.githubusercontent.com/Vankimfc0/Boot-image-Extractor/main/scripts/boot_image_extractor.py; clear; sudo python boot_image_extractor.py
   ```
   > **Note:** It may take some time to run for the first time because the script will be downloaded along with the required tools. Please be patient.

#### Procedure 2: Manual Installation

1. **Clone or Download Source:**
   Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/Vankimfc0/Boot-image-Extractor.git
   cd Boot-image-Extractor
   ```
   or download the source zip file from [GitHub](https://github.com/Vankimfc0/Boot-image-Extractor/archive/refs/heads/master.zip), extract it, and navigate to the extracted directory.

2. **Install Dependencies:**
   Ensure Python and required packages are installed:
   ```bash
   pkg install python tsu -y
   pip install -r requirements.txt
   ```

3. **Install the Script:**
   Run the setup script to install Boot Image Extractor:
   ```bash
   pip install .
   ```
   This will install the Boot Image Extractor script on your terminal and make it accessible system-wide.

## Usage Instructions

After installation, execute the script using the following command:
```bash
sudo boot_image_extractor.py
```

If you used the direct installation method and the script was downloaded to a different directory instead of Termux's `$HOME` directory, you may need to change to the directory where the script is located before running it.

## Contribution

Contributions to Boot Image Extractor are welcome. Please fork the repository, make your modifications, and submit a pull request. For detailed guidelines, see our [Contributing Guidelines](CONTRIBUTING.md).

## License

This script is distributed under the terms of the [MIT License](LICENSE).

## Support

For any issues or inquiries, please open an issue on the repository's [issue tracker](https://github.com/Vankimfc0/Boot-image-Extractor/issues) or contact the developer via [Telegram](https://t.me/PhantomXPain).
