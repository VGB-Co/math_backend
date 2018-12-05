from rft_webapp.database.models import Results


def insertresults(par_name, par_type, par_time, par_score):
    result = Results(name=par_name, type=par_type, time=par_time, score=par_score)
    result.save()


def selectallresults():
    Results.objects.all()