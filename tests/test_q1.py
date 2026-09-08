"""HW1 Question 1 Tests"""

ORIGINAL_CONTENT = '''"""HW1 Question 1

To get full points on this question, modify this file and make a submission.
The file must still work as a valid Python file.
You can write a poem, write Python code, or just add a single character.

Getting your setup ready is the hardest part of the semester.
This question is designed to give you points for getting your GitHub and 
Pawtograder setup working."""

def print_meow() -> None:
    """Prints 'meow' to the console."""
    print("meow")'''


def test_q1_contents() -> None:
    """Test that the contents of q1.py have been modified from the original content."""
    with open("src/q1.py", encoding="utf-8") as f:
        contents = f.read()
    assert contents != ORIGINAL_CONTENT
