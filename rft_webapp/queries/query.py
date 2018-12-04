from rft_webapp.database.models import Results


def insertresults(par_userid, par_type, par_time, par_score):
    result = Results(user=par_userid, type=par_type, time=par_time, score=par_score)
    result.save()


def selectallresults():
    Results.objects.all()


def toplist(par_type):
    if par_type is None:
        return Results.objects.all().order_by('time')
    else:
        return Results.objects.all().filter(type=par_type).order_by('time')
