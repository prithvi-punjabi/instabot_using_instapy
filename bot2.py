from instapy import InstaPy
import getpass

print('Welcome to the Instagram Bot')
username = input("Please enter your Instagram Username: ")
password = getpass.getpass()

session = InstaPy(username=username, password=password, headless_browser=False)
session.login()


def follow():
    global session
    inp = input("Enter the usernames you would like to follow separated by spaces:")
    user = inp.split()
    session.set_skip_users(skip_private=False)
    session.follow_by_list(followlist=user, times=1, sleep_delay=600, interact=False)


def like():
    global session
    inp = input("Enter the username of the person whose pictures you want to like:")
    amt = int(input("Enter the number of pictures you want to like:"))
    session.set_do_like(enabled=True, percentage=100)
    session.set_do_comment(enabled=False)
    session.interact_by_users([inp], amount=amt, randomize=True, media='Photo')


def comment():
    global session
    inp1 = input("Enter the username of the person whose pictures you want to like & comment on:")
    amt = int(input("How many pictures do you want to like and comment on?: "))
    string = input("Enter your comments, separated by spaces: ")
    comment = string.split()
    session.set_do_follow(enabled=True)
    session.set_do_like(enabled=True, percentage=100)
    session.set_do_comment(True, percentage=100)
    session.set_comments(comment)
    session.interact_by_users([inp1], amount=amt, randomize=True, media='Photo')


def unfollow():
    inp = input("Enter the usernames you would like to follow separated by spaces:")
    user = inp.split()
    session.unfollow_users(amount=len(user), custom_list_enabled=True, custom_list=user, custom_list_param="all",
                           style="FIFO", unfollow_after=5, sleep_delay=10)


def unfollowers():
    user_list = []
    input_user = input("Enter username")
    user_list.append(input_user)
    nonfollowers = session.pick_nonfollowers(username=str(user_list[0]), live_match=True, store_locally=True)
    for i in nonfollowers:
        print(i)


while True:
    dict1 = {1: "Follow", 2: "Like", 3: "Like & Comment",4:'Unfollow',5:'List Unfollowers'}
    print("What would you like to do?")
    print(dict1)
    try:
        opt = int(input("Enter your choice: "))
    except ValueError:
        print("Please try again")
        continue
    if opt == 1:
        follow()
    elif opt == 2:
        like()
    elif opt == 3:
        comment()
    elif opt == 4:
        unfollow()
    elif opt == 5:
        unfollowers()
    else:
        break