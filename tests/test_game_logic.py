from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

#FIX: Asked Copilot to generate pytest for go high/low indicators/messages
def test_hint_message_correct():
    # Winning outcome should produce the correct emoji message
    assert get_hint_message("Win") == "🎉 Correct!"

def test_hint_message_go_lower():
    # Too High outcome should tell the player to go lower
    assert get_hint_message("Too High") == "📉 Go LOWER!"

def test_hint_message_go_higher():
    # Too Low outcome should tell the player to go higher
    assert get_hint_message("Too Low") == "📈 Go HIGHER!"
