from rft_webapp.mathematic import temp
from rft_webapp.mathematic import enums
from rft_webapp.API import serializers
from rft_webapp.mathematic import models

class Generator():


    def generatings(cica, lvl):
        for i in range(cica):
            tmp = temp.Generating(lvl)
            task = models.Task()
            task.question = tmp.question
            task.correct_answer = tmp.correct_answer
            task.save()