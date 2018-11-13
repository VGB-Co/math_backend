from rft_webapp.database.models import User, Results


def insertuser(username):
    user = User(user_id=username)
    user.save()


def insertresults(par_userid, par_type, par_time):
    result = Results(user_id=par_userid, type=par_type, time=par_time)
    result.save()


def selectresultsbytype(par_type):
    result = Results(type = par_type)


def selectallresults():
    result = Results.objects.all()

