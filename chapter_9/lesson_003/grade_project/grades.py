def letter_grade(score):
    """Return the letter grade (A-F) for a score from 0 to 100.

    Raises TypeError if score is not a number.
    Raises ValueError if score is below 0 or above 100.
    """
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise TypeError("score must be a number")
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
