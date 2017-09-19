from django.db import models

from home.models import User


class TypeTest(models.Model):
    """
    Model for different type of tests.
    For example: Python level 1, Python level 2, Java level 1 and etc.
    """
    type_test = models.CharField(max_length=200)

    def __str__(self):
        return self.type_test.capitalize()


class Question(models.Model):
    """Model for questions."""
    question_text = models.CharField(max_length=400)
    type_test = models.ForeignKey(TypeTest, on_delete=models.CASCADE)  # many-to-one

    def __str__(self):
        return self.question_text


class Option(models.Model):
    """Model for test options."""
    option_text = models.CharField(max_length=200)
    truth = models.BooleanField(default=False)  # True if option is correct
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # many-to-one

    def __str__(self):
        return 'Option is {} - {}'.format(self.option_text, self.truth)


class UserResult(models.Model):
    """This model stores information about questions which user has passed."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # many-to-one
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # many-to-one
    right_question = models.BooleanField(default=False)  # True when user gave the correct answer

    def __str__(self):
        return self.question


class CurrentUserResult(models.Model):
    """
    This model contains information about current test.
    After test it will be deleted.
    """
    user_id = models.IntegerField(primary_key=True, blank=False)  # store user_id
    results = models.IntegerField(default=1)  # store the number of questions
    right_answers = models.IntegerField(default=1)

    def __str__(self):
        return 'Correct answers of {} out of {}'.format(self.right_answers, self.results)
