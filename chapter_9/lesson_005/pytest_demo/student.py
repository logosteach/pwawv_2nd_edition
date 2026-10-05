class Student:
    def __init__(self, name, grade_level):
        if grade_level not in (9, 10, 11, 12):
            raise ValueError("grade_level must be 9, 10, 11, or 12")
        self.name = name
        self.grade_level = grade_level
        self.scores = []

    def add_score(self, score):
        if score < 0 or score > 100:
            raise ValueError("score must be between 0 and 100")
        self.scores.append(score)

    def average(self):
        """Return the average score, or 0.0 if there are no scores yet."""
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)

    def highest(self):
        """Return the highest score, or None if there are no scores yet."""
        if not self.scores:
            return None
        return max(self.scores)

    def is_passing(self):
        return self.average() >= 60

    def promote(self):
        """Move up one grade level. Seniors cannot be promoted."""
        if self.grade_level == 12:
            raise ValueError("Seniors cannot be promoted")
        self.grade_level += 1
