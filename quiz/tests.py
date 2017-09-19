from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import RequestFactory

from .views import UserProfileView
from .models import TypeTest, Question, Option, CurrentUserResult


class TestTypeTest(TestCase):
    """Test TypeTest model, check that all attributes are set as expected."""
    def setUp(self):
        self.python = TypeTest.objects.create(type_test='python2 level 1')
        self.java = TypeTest.objects.create(type_test='java level 1')

    def test_type_test_str_capitalize(self):
        self.assertEqual(self.python.__str__(), 'Python2 level 1')
        self.assertEqual(self.java.__str__(), 'Java level 1')

    def test_type_test_quantity(self):
        self.assertEqual(len(TypeTest.objects.all()), 2)


class TestQuestion(TestCase):
    """Test Question model, check that all attributes are set as expected."""
    def setUp(self):
        self.python = TypeTest.objects.create(type_test='python2 level 1')
        self.q = Question.objects.create(question_text='What\'s up?', type_test=self.python)

    def test_question_get_by_id(self):
        self.assertEqual(Question.objects.get(id=1), self.q)

    def test_question_type_test(self):
        self.assertEqual(self.q.type_test, self.python)

    def test_question_text(self):
        self.assertEqual(self.q.question_text, 'What\'s up?')


class TestOption(TestCase):
    """Test Option model, check that all attributes are set as expected."""
    def setUp(self):
        self.python = TypeTest.objects.create(type_test='python2 level 1')
        self.q = Question.objects.create(question_text='What\'s up?', type_test=self.python)
        self.option_1 = Option.objects.create(option_text='great', truth=True, question=self.q)
        self.option_2 = Option.objects.create(option_text='bad', question=self.q)  # default truth

    def test_option_str_format(self):
        self.assertEqual(self.option_1.__str__(), 'Option is great - True')
        self.assertEqual(self.option_2.__str__(), 'Option is bad - False')

    def test_option_default_truth(self):
        self.assertEqual(self.option_2.truth, False)

    def test_option_question(self):
        self.assertEqual(self.option_1.question, self.q)
        self.assertEqual(self.option_2.question, self.q)

    def test_option_text(self):
        self.assertEqual(self.option_1.option_text, 'great')
        self.assertEqual(self.option_2.option_text, 'bad')


class TestCurrentUserResult(TestCase):
    """Test CurrentUserResult model, check that all attributes are set as expected."""
    def setUp(self):
        self.current_user_result = CurrentUserResult(user_id=1)
        self.current_user_result.save()

    def test_current_user_result_default_values(self):
        self.assertEqual(self.current_user_result.results, 1)
        self.assertEqual(self.current_user_result.right_answers, 1)

    def test_current_user_result_update_attributes(self):
        self.current_user_result.results += 1
        self.current_user_result.right_answers += 1

        self.assertEqual(self.current_user_result.results, 2)
        self.assertEqual(self.current_user_result.right_answers, 2)

    def test_current_user_result_get_by_id(self):
        self.assertEqual(CurrentUserResult.objects.get(user_id=1), self.current_user_result)

    def test_current_user_result_raises_does_not_exist(self):
        self.assertRaises(CurrentUserResult.DoesNotExist, user_id=2)

    def test_current_user_result_str_format(self):
        self.assertEqual(self.current_user_result.__str__(), 'Correct answers of 1 out of 1')
