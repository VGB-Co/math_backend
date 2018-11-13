from rft_webapp.database.models import User, Results


def insertuser(username):
    user = User(user_name=username)

def insertresults(par_userid, par_type, par_time):
    result = Results(user_id = par_userid, type = par_type, time = par_time)