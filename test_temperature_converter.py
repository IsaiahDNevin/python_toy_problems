import unittest
from unittest.mock import patch
from temperature_converter import user_input_temperature_type, convert_to_fehrenheit, convert_to_celsius, main

class TestTempreratureConverter(unittest.TestCase):
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=["F"])
    def test_user_input_temperature_type(self, mock_input, _mock_print):
        user_input_temperature_type()
        mock_input.assert_called_with("Pick either Fehrenheit or Celsius to convert (F, C): ")


    def test_convert_to_fehrenheit(self):
        self.assertEqual(convert_to_fehrenheit(72), 22)

    def test_convert_to_celsius(self):
        self.assertEqual(convert_to_celsius(22), 72)


    @patch('builtins.print')    
    @patch('builtins.input', side_effect=["32"])
    @patch('temperature_converter.user_input_temperature_type', return_value="F")
    def test_main(self, mock_user_input_temperature_type, mock_input, mock_print):
        main()
        mock_user_input_temperature_type.assert_called_once()
        mock_input.assert_any_call("Input Temperature in F: ")
        mock_print.assert_called_once_with(convert_to_fehrenheit(32))
    
if __name__ == '__main__':
    unittest.main()