def retweet():
    import tweepy
    from textblob import TextBlob
    from reply_bot import reply_messages
    import time
    """
            Always checking the timeline for updates

            If there are very good comments, which according to me are polarities above 0.2, it likes and retweets

            If the statements are derogatory or the comments does not really reflect a very good comment, it does not
            take any action

    """

    auth = tweepy.OAuthHandler("eLz5PW2HhVvfeJ2hmKjlZmP6g", "BDGnsOitwOcZJWdvvSwTr5iI2OKGglinEHT6glhCJrpLbHl1GT")
    auth.set_access_token("1445122551773110273-OhjDrVIbWb4yKcbew3TfkZJLgPJUNt",
                          "RPAzEmtTwiRRxlJfWJJegXbPQkvwH5Q17s8SeUzXhURXz")
    api = tweepy.API(auth)

    # Some important variables which will be used later
    bot_id = api.me()
    mention_id = 1
    while True:
        mentions = api.mentions_timeline(since_id=mention_id)
        for mention in mentions:
            print("Mention Tweet found!")
            print(f"MENTION: {mention.author.screen_name} - {mention.text}")
            mention_id = mention.id
            mention_analysis = TextBlob(mention.text)
            mention_analysis_score = mention_analysis.sentiment.polarity
            print(f"Tweet has polarity score of {mention_analysis_score}")
            if mention.in_reply_to_status_id is None and mention.author.id != bot_id:
                if mention_analysis_score >= 0.3 and not mention.retweeted:
                    try:
                        print("trying retweet...")
                        api.retweet(mention.id)
                        mention.favorite()
                        print("Tweet successfully retweeted!\n")
                    except Exception as err:
                        print(err)
                else:
                    print("Tweet will not be retweeted.\n")
        time.sleep(15)
        print('OK! On to the next step...')
        reply_messages()
