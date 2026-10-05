import pytest
from student import Student


@pytest.fixture
def student():
    return Student("Sam", 10)


def test_new_student_has_no_scores(student):
    assert student.scores == []


def test_add_score(student):
    student.add_score(88)
    assert 88 in student.scores


def test_add_score_over_100_raises(student):
    with pytest.raises(ValueError):
        student.add_score(101)


def test_average_with_no_scores(student):
    assert student.average() == 0.0


def test_average_of_three_scores(student):
    for score in [80, 90, 75]:
        student.add_score(score)
    assert student.average() == pytest.approx(81.667, abs=0.001)


def test_highest_with_no_scores_is_none(student):
    assert student.highest() is None


@pytest.mark.parametrize("score, passing", [
    (100, True),
    (60, True),      # edge: exactly passing
    (59, False),     # edge: just below
    (0, False),
])
def test_is_passing(student, score, passing):
    student.add_score(score)
    assert student.is_passing() == passing


def test_promote(student):
    student.promote()
    assert student.grade_level == 11


def test_senior_cannot_be_promoted():
    with pytest.raises(ValueError, match="Seniors"):
        Student("Lee", 12).promote()
