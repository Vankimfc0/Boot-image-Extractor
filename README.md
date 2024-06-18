# Boot Image Extractor

Boot Image Extractor is a standalone Python script designed to extract the boot image from Android devices with root access. It supports both [A/B](https://source.android.com/devices/tech/ota/ab) and [legacy partition](https://source.android.com/devices/bootloader/partitions) styles. This script was developed as part of an automated method for extracting boot images described in the [Boot Image Extraction Guide](https://gist.github.com/gitclone-url/a1f693b64d8f8701ec24477a2ccaab87#file-boot-image-extraction-guide-md).

## Requirements

- Python 3 or higher
- Root access on the Android device
- Python package: `pyfiglet`

## Installation Instructions

#### Procedure 1: Direct Installation

1. Download [Termux](https://termux.com/) and install it.
2. Open Termux and allow storage permission using:
   ```bash
   termux-setup-storage
   ```
3. If you going to use this script on a [Phh-based GSI](https://github.com/phhusson/treble_experimentations/wiki/Frequently-Asked-Questions-%28FAQ%29) that ships with an inbuilt [superuser](https://github.com/phhusson/treble_experimentations/wiki/Frequently-Asked-Questions-%28FAQ%29#naming-conventions-that-some-gsi-buildermaintainer-uses) check if the PHH Superuser app is installed by running:
   ```bash
   (pm list packages | grep me.phh.superuser) && echo "Found" || echo "Not found"
   ```
   > **Note:** If "Not found" is displayed, install the app from [F-Droid](https://f-droid.org/en/packages/me.phh.superuser/). This app is essential to manage root access for Termux. Skip this step if your device is already rooted with Magisk or a other method.

4. Grant superuser permission to Termux by typing:
   ```bash
   su
   ```
5. Copy and paste the following command and hit enter to start running the script:
   ```bash
   apt update && apt upgrade -y; { command -v tsu && command -v curl && command -v python && command -v pip && python -c 'import pyfiglet' &>/dev/null; } || apt install -y tsu curl python; pip install pyfiglet; curl -s https://raw.githubusercontent.com/gitclone-url/Boot-img-flasher/Master/boot-img-flasher.sh -o boot-img-flasher.sh; clear; sudo boot_image_extractor.py
   ```
   > **Note:** It may take some time to run for the first time because the script will be downloaded along with the required tools. Please be patient.

#### Procedure 2: Manual Installation

1. Clone the repository or download the zip file from [GitHub](https://github.com/gitclone-url/Boot-image-Extractor/archive/refs/heads/master.zip).

2. Install Python if not already installed on your terminal:
   ```bash
   pkg install python -y
   ```

3. Install `tsu` using the following command:
   ```bash
   pkg install tsu
   ```

4. Navigate to the cloned or extracted directory and run the command:
   ```bash
   pip install .
   ```
   This will install the Boot Image Extractor script on your terminal and make it accessible system-wide.

## Usage Instructions

After installation, you can execute the script using the following command:
```bash
sudo boot_image_extractor.py
```

If you used the direct installation method and the script was downloaded to a different directory instead of Termux's `$HOME` directory, you may need to change the directory to where the script is located before running it.

## Contribution

Contributions to the Boot Image Extractor are welcome. Please fork the repository, make your modifications, and submit a pull request. For detailed guidelines, see our [Contributing Guidelines](CONTRIBUTING.md).

## License

This script is distributed under the terms of the [MIT License](LICENSE).

## Support

For any issues or inquiries, please open an issue on the repository's [issue tracker](https://github.com/gitclone-url/Boot-image-Extractor/issues) or contact the developer via [Telegram](https://t.me/PhantomXPain).