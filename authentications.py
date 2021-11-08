import tweepy

from config import create_api


# auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
# auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

def authentication():
    auth = tweepy.OAuthHandler("eLz5PW2HhVvfeJ2hmKjlZmP6g",
                               "BDGnsOitwOcZJWdvvSwTr5iI2OKGglinEHT6glhCJrpLbHl1GT")
    auth.set_access_token("1445122551773110273-OhjDrVIbWb4yKcbew3TfkZJLgPJUNt",
                          "RPAzEmtTwiRRxlJfWJJegXbPQkvwH5Q17s8SeUzXhURXz")

    # api = tweepy.API(auth)

    # create API object
    api = tweepy.API(auth, wait_on_rate_limit=True)
