import pytest
from django.utils import timezone

from polls.models import Question


@pytest.mark.django_db
def test_question_create():
    # Give
    question_text = "Whats?"
    pub_date = timezone.now()
    active = True

    # When
    question = Question.objects.create(
        question_text=question_text, pub_date=pub_date, active=active
    )

    # Then
    assert question.question_text == question_text
    assert question.pub_date == pub_date
    assert question.active == active


@pytest.mark.django_db
def test_question_model_was_published_recently_sucess():
    # Give
    question_text = "Whats?"
    pub_date = timezone.now()  # - timezone.timedelta(days=2)
    active = True

    # When
    question = Question.objects.create(
        question_text=question_text, pub_date=pub_date, active=active
    )

    # Then
    assert question.was_published_recently() is True
