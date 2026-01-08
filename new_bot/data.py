users = {}


def get_user_ball(user_id):
    ball = 0
    for user in users.values():
        print(f"user_id={user_id} user={user}")
        if user_id == user['reffer_id'] and user['flag']:
            ball += 1
    return ball
