from django.db import models
from quiz_app.models import Question
from random import shuffle


ANSWER_ORDER_OPTIONS = (
    ('content', 'Content'),
    ('random', 'Random')
)


class McqQuestion(Question):

    # answer_order = models.CharField(
    #     max_length=30, null=True, blank=True,
    #     choices=ANSWER_ORDER_OPTIONS,
    #     help_text="The order in which multichoice \
    #                 answer options are displayed \
    #                 to the user",
    #     verbose_name="Answer Order")

    def check_if_correct(self, guess):
        answer = Answer.objects.get(id=guess)

        if answer.correct is True:
            return True
        else:
            return False

    # def order_answers(self, queryset):
    #     if self.answer_order == 'content':
    #         return queryset.order_by('content')
    #     # if self.answer_order == 'random':
    #     #     return queryset.order_by('random')

    def get_answers(self):
        answers = list(Answer.objects.filter(question=self))
        shuffle(answers)
        return answers

    def get_answers_list(self):
        answer_list = [(answer.id, answer.content) for answer in self.get_answers()]
        return answer_list

    def answer_choice_to_string(self, guess):
        return Answer.objects.get(id=guess).content

    class Meta:
        verbose_name = "Multiple Choice Question"
        verbose_name_plural = "Multiple Choice Questions"


class Answer(models.Model):
    question = models.ForeignKey(McqQuestion, verbose_name='Question', on_delete=models.CASCADE)

    content = models.CharField(max_length=1000,
                               blank=False,
                               help_text="Enter the answer text that \
                                            you want displayed",
                               verbose_name="Content")

    correct = models.BooleanField(blank=False,
                                  default=False,
                                  help_text="Is this a correct answer?",
                                  verbose_name="Correct")

    def __str__(self):
        return self.content


    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"