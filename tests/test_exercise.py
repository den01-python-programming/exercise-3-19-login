import pytest
import src.exercise

def test_exercise():
    input_values = ["grace","hopper","emma","haskell","alex","password"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()
    
    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert output[0:2] == ["Enter username:","Enter password:","You have successfully logged in!"]
    assert output[3:5] == ["Enter username:","Enter password:","You have successfully logged in!"]
    ssert output[6:8] == ["Enter username:","Enter password:","Incorrect username or password!"]
