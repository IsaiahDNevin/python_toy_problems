import unittest
from unittest.mock import patch
from rock_paper_scissors import run_game, get_user_input, get_computer_choice, print_starting_message, evaluate_winner


class TestRockPaperScissors(unittest.TestCase):
    # Im using setUp and tearDown methods to globally mock time.sleep
    # Start mocking time.sleep before each test
    def setUp(self):
         # Here im using self.patcher = patch('time.sleep', return_value=None) in my setUp method to mock time.sleep across all tests in the class.
        self.patcher = patch('time.sleep', return_value=None)
        self.mock_sleep = self.patcher.start()
    # Stop mocking time.sleep after each test 
    def tearDown(self):
        self.patcher.stop()

    @patch('builtins.print')
    @patch('time.sleep')
    def test_print_starting_message_prints_correct_values(self, _mock_time, mock_print):
        print_starting_message()

        mock_print.assert_has_calls([
            unittest.mock.call("Rock"),
            unittest.mock.call("Paper"),
            unittest.mock.call("Scissors"),
        ])

    @patch('builtins.print')
    @patch('time.sleep')
    def test_print_starting_message_sleeps_between_each_print(self, mock_time, _mock_print):
        print_starting_message()

        mock_time.assert_has_calls([
            unittest.mock.call(0.5),
            unittest.mock.call(0.5),
            unittest.mock.call(0.5),
        ])

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["Rock"])
    def test_get_user_input_user_prints_the_prompt(self, mock_input, _mock_print):
        get_user_input()
        mock_input.assert_called_with("Enter rock, paper, or scissors: ")

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["Rock"])
    def test_get_user_input_user_chooses_rock(self, _mock_input, _mock_print):
        user_choice = get_user_input()
        self.assertEqual(user_choice, 'rock')

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["Paper"])
    def test_get_user_input_user_chooses_paper(self, _mock_input, _mock_print):
        user_choice = get_user_input()
        self.assertEqual(user_choice, 'paper')

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["Scissors"])
    def test_get_user_input_user_chooses_scissors(self, _mock_input, _mock_print):
        user_choice = get_user_input()
        self.assertEqual(user_choice, 'scissors')

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["notathing", "Rock"])
    def test_get_user_input_user_chooses_a_wrong_thing(self, mock_input, mock_print):
        user_choice = get_user_input()

        mock_input.assert_has_calls([
            unittest.mock.call('Enter rock, paper, or scissors: '),
            unittest.mock.call('Enter rock, paper, or scissors: '),
        ])
        mock_print.assert_has_calls([
            unittest.mock.call('Invalid choice. Please try again.'),
        ])
        self.assertEqual(user_choice, 'rock')        

    @patch('random.randint', side_effect=[1])
    def test_get_computer_choice_computer_chooses_rock(self, _):
        computer_choice = get_computer_choice()
        self.assertEqual(computer_choice, 'rock')

    @patch('random.randint', side_effect=[2])
    def test_get_computer_choice_computer_chooses_paper(self, _):
        computer_choice = get_computer_choice()
        self.assertEqual(computer_choice, 'paper')

    @patch('random.randint', side_effect=[3])
    def test_get_computer_choice_computer_chooses_scissors(self, _):
        computer_choice = get_computer_choice()
        self.assertEqual(computer_choice, 'scissors')

    @patch('random.randint')
    def test_get_computer_choice_computer_chooses_rock(self, mock_random):
        get_computer_choice()
        mock_random.assert_has_calls([
            unittest.mock.call(1, 3),
        ])
    
    @patch('rock_paper_scissors.get_user_input', return_value="rock")
    @patch('rock_paper_scissors.get_computer_choice', return_value="rock")
    @patch('builtins.print') 
    def test_run_game_return_tie(self, mock_computer_choice, mock_user_input, mock_print):
        result = run_game()
        self.assertEqual(result, "tie")  # Assert that the result is "tie"
    
    @patch('rock_paper_scissors.get_user_input', return_value="rock")
    @patch('rock_paper_scissors.get_computer_choice', return_value="scissors")
    @patch('builtins.print') 
    def test_run_game_player_wins(self, mock_computer_choice, mock_user_input, mock_print):
        result = run_game()
        self.assertEqual(result, "player")

    @patch('rock_paper_scissors.get_user_input', return_value="rock")
    @patch('rock_paper_scissors.get_computer_choice', return_value="paper")
    @patch('builtins.print') 
    def test_run_game_computer_wins(self, mock_computer_choice, mock_user_input, mock_print):
        result = run_game()
        self.assertEqual(result, "computer")


    def test_evaluate_winner_computer_wins(self):
        state = {"player": 2, "computer": 1}
        result = evaluate_winner(state)
        self.assertEqual(result, "You won!!")


    def test_evaluate_winner_player_wins(self):
        state = {"player": 1, "computer": 3}
        result = evaluate_winner(state)
        self.assertEqual(result, "You lose :(")

if __name__ == '__main__':
    unittest.main()
