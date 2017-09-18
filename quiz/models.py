from django.db import models


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
    truth = models.BooleanField()  # can be False if option is not right or True if is truth
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # many-to-one

    def __str__(self):
        return 'Option is {} - {}'.format(self.option_text, self.truth)


class Result(models.Model):
    result = models.IntegerField(default=0)
    right_answer = models.IntegerField(default=0)

    def __str__(self):
        return self.result
