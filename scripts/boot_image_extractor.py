#!/usr/bin/env python3

"""A script to extract boot images from any Android device with root access."""

import os
import sys
import time
import pyfiglet
import subprocess

def print_banner(title):
    max_width = os.get_terminal_size().columns
    banner = pyfiglet.figlet_format(title, font='small', width=max_width)
    print(banner.center(max_width))

def exit_with_error(error_message, error_detail):
    print("\033[91m\nError:\033[0m", error_message)
    print("\nReason:", error_detail)
    sys.exit(1)

def extract_boot_image_for_ab_device(boot_a_path, boot_b_path):
    active_slot_suffix = subprocess.getoutput('getprop ro.boot.slot_suffix')
    print(f"\n- Current active slot: ({active_slot_suffix}).")
    time.sleep(1)

    while True:
        selected_slot = input("- Which boot slot image would you like to extract? (a/b): ").lower()
        if selected_slot == 'a':
            boot_image_path = boot_a_path
            break
        elif selected_slot == 'b':
            boot_image_path = boot_b_path
            break
        else:
            print("Invalid input. Please enter 'a' or 'b'.\n")

    print(f"\n- Extracting the boot image from {boot_image_path}...")
    time.sleep(1)
    try:
        subprocess.check_call(['dd', f'if={boot_image_path}', f'of=./boot_{selected_slot}.img'])
        print(f"\033[92m\n- Boot image successfully extracted and saved as boot_{selected_slot}.img in the current directory.\033[0m")
    except subprocess.CalledProcessError:
        exit_with_error("Extraction failed", "The dd command did not complete successfully.")

def extract_boot_image_for_legacy_device(boot_path):
    print(f"\n- Extracting the boot image from {boot_path}...")
    time.sleep(1)
    try:
        subprocess.check_call(['dd', f'if={boot_path}', 'of=./boot.img'])
        time.sleep(1)
        print("\033[92m\n- Boot image successfully extracted and saved as boot.img in the current directory.\033[0m")
    except subprocess.CalledProcessError:
        exit_with_error("Extraction failed", "The dd command did not complete successfully.")

def main():
    if os.geteuid() != 0:
        exit_with_error("Insufficient privileges", "This script requires root access. Please run as root or use sudo.")

    print_banner("Boot Image Extractor")
    time.sleep(1)

    boot_partitions = {}
    for partition in ["boot", "boot_a", "boot_b"]:
        partition_path = subprocess.getoutput(f"find /dev/block -type b -o -type l -iname '{partition}' -print -quit 2>/dev/null")
        if partition_path:
            boot_partitions[partition] = os.path.realpath(partition_path)
            
    if 'boot_a' in boot_partitions and 'boot_b' in boot_partitions:
        print("\n- A/B partition style detected!.")
        time.sleep(1)
        extract_boot_image_for_ab_device(boot_partitions['boot_a'], boot_partitions['boot_b'])
    elif 'boot' in boot_partitions:
        print("\n- Legacy(non-A/B) partition style detected!.")
        time.sleep(1)
        extract_boot_image_for_legacy_device(boot_partitions['boot'])
    else:
        exit_with_error("No boot partition found", "Unable to locate block device files.")

if __name__ == '__main__':
    main()