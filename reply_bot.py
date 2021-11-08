def reply_messages():
    """
    replies to questions in which i am tagged

    """
    import tweepy
    import time
    from time_and_date import time_date
    from tech_reply import reply_tech

    # Initialization code
    auth = tweepy.OAuthHandler("eLz5PW2HhVvfeJ2hmKjlZmP6g", "BDGnsOitwOcZJWdvvSwTr5iI2OKGglinEHT6glhCJrpLbHl1GT")
    auth.set_access_token("1445122551773110273-OhjDrVIbWb4yKcbew3TfkZJLgPJUNt", "RPAzEmtTwiRRxlJfWJJegXbPQkvwH5Q17s8SeUzXhURXz")
    api = tweepy.API(auth)

    # Some important variables which will be used later
    bot_id = api.me()
    mention_id = 1
    words = ["why", "how", "when", "what", "?"]
    message = "If you have any questions, feel free to send us a DM @{}"

    # The actual bot
    while True:
        mentions = api.mentions_timeline(since_id=mention_id) # Finding mention tweets
        # Iterating through each mention tweet
        for mention in mentions:
            print("Mention tweet found")
            print(f"{mention.author.screen_name} - {mention.text}")
            mention_id = mention.id
            if mention.in_reply_to_status_id is None and mention.author.id != bot_id:
                if True in [word in mention.text.lower() for word in words]:
                    try:
                        print("Replying...")
                        api.update_status(message.format(mention.author.screen_name), in_reply_to_status_id=mention.id_str)
                        print("Successfully replied!")
                    except Exception as exc:
                        print(exc)
        time.sleep(15)
        reply_tech()

