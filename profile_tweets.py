import tweepy


def tweets():
    import tweepy

    """
    Checks if you want to tweet anything.

    If you choose yo tweet, it updates it for you

    If not, it remains the same

    """

    auth = tweepy.OAuthHandler("eLz5PW2HhVvfeJ2hmKjlZmP6g", "BDGnsOitwOcZJWdvvSwTr5iI2OKGglinEHT6glhCJrpLbHl1GT")
    auth.set_access_token("1445122551773110273-OhjDrVIbWb4yKcbew3TfkZJLgPJUNt",
                          "RPAzEmtTwiRRxlJfWJJegXbPQkvwH5Q17s8SeUzXhURXz")
    api = tweepy.API(auth)

    # Some important variables which will be used later
    check_tweet = input('Would you like to tweet ? Y or N \n')
    if check_tweet.lower() == 'y':
        print('what would you like to tweet : ')
        x = input()
        if x:
            api.update_status(x)
            print('You tweeted', x)
    else:
        print('you can still change your mind')
        check_tweet = input('Would you like to tweet ? Y or N \n')
        if check_tweet.lower() == 'y':
            print('what would you like to tweet : ')
            x = input()
            if x:
                api.update_status(x)
                print('You tweeted', x)
        else:
            print('Okay! you did not tweet anything.')
