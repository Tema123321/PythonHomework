def select_top_users_by_rate(users, top_size):
    return sorted(users, key= lambda x: -x.rate)[0:top_size]
