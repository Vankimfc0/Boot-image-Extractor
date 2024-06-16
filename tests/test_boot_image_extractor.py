import unittest
from unittest.mock import patch, MagicMock

from scripts.boot_image_extractor import (
    print_banner, exit_with_error, extract_boot_image_for_legacy_device,
    extract_boot_image_for_ab_device, main
)

class TestBootImageExtractor(unittest.TestCase):
    """Provides unit tests for the Boot Image Extractor script to ensure its proper functionality
    in various scenarios. Additional test cases can be added to improve test coverage."""

    def infinite_side_effect(self, *values):
        while True:
            for value in values:
                yield value

    @patch('builtins.print')
    def test_print_banner(self, mock_print):
        print_banner("Test Banner")
        mock_print.assert_called()

    @patch('builtins.print')
    @patch('subprocess.getoutput')
    @patch('os.geteuid', MagicMock(return_value=0))
    def test_extract_boot_image_for_legacy_device(self, mock_getoutput, mock_print):
        mock_getoutput.return_value = '/dev/block/boot'
        with patch('subprocess.check_call', MagicMock()) as mock_check_call:
            extract_boot_image_for_legacy_device('/dev/block/boot')
            mock_check_call.assert_called_with(['dd', 'if=/dev/block/boot', 'of=./boot.img'])

    @patch('builtins.print')
    @patch('subprocess.getoutput')
    @patch('os.geteuid', MagicMock(return_value=0))
    @patch('builtins.input', return_value='a')
    def test_extract_boot_image_for_ab_device(self, mock_input, mock_getoutput, mock_print):
        mock_getoutput.side_effect = ['_a', 'a']
        with patch('subprocess.check_call', MagicMock()) as mock_check_call:
            extract_boot_image_for_ab_device('/dev/block/boot_a', '/dev/block/boot_b')
            mock_check_call.assert_called_with(['dd', 'if=/dev/block/boot_a', 'of=./boot_a.img'])

    @patch('os.geteuid', MagicMock(return_value=0))
    @patch('subprocess.getoutput', return_value='')
    @patch('scripts.boot_image_extractor.print_banner', MagicMock())
    @patch('scripts.boot_image_extractor.exit_with_error')
    def test_main_no_boot_partition_found(self, mock_exit_with_error, mock_getoutput):
        main()
        mock_exit_with_error.assert_called_with("No boot partition found", "Unable to locate block device files.")
        
    @patch('os.geteuid', MagicMock(return_value=0))
    @patch('subprocess.getoutput')
    @patch('builtins.print')
    def test_main_legacy_partition_style(self, mock_print, mock_getoutput):
        mock_getoutput.side_effect = ['/dev/block/boot', '', '']
        with patch('subprocess.check_call', MagicMock()) as mock_check_call:
            main()
            mock_print.assert_any_call("\n- Legacy(non-A/B) partition style detected!.")
            mock_check_call.assert_called_with(['dd', 'if=/dev/block/boot', 'of=./boot.img'])
            
    @patch('os.geteuid', MagicMock(return_value=0))
    @patch('subprocess.getoutput')
    @patch('builtins.print')
    @patch('builtins.input', return_value='a')
    def test_main_ab_partition_style(self, mock_input, mock_print, mock_getoutput):
        # Set the side_effect to our infinite_side_effect function
        mock_getoutput.side_effect = self.infinite_side_effect('_a', '/dev/block/boot_a', '/dev/block/boot_b')
        with patch('subprocess.check_call', MagicMock()) as mock_check_call:
            main()
            mock_print.assert_any_call("\n- A/B partition style detected!.")
            mock_check_call.assert_called_with(['dd', 'if=/dev/block/boot_a', 'of=./boot_a.img'])        

if __name__ == '__main__':
    unittest.main()

    