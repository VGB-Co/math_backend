from rft_webapp.database.models import Results


def insertresults(par_userid, par_type, par_time):
    result = Results(user_id=par_userid, type=par_type, time=par_time)
    result.save()


def selectresultsbytype(par_type):
    Results.objects.all().filter(type=par_type)


def selectallresults():
    Results.objects.all()


def selectownresults(par_userid, par_type):
    if par_type is None:
        Results.objects.all().filter(user_id=par_userid)
    else:
        Results.objects.all().filter(user_id=par_userid, type=par_type)
