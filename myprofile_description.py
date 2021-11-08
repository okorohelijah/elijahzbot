def my_description():
    import tweepy

    """
        Checks if you want to change the description

        If you choose to updates, it updates it for you

        If not, it remains the same

        """
    auth = tweepy.OAuthHandler("eLz5PW2HhVvfeJ2hmKjlZmP6g", "BDGnsOitwOcZJWdvvSwTr5iI2OKGglinEHT6glhCJrpLbHl1GT")
    auth.set_access_token("1445122551773110273-OhjDrVIbWb4yKcbew3TfkZJLgPJUNt",
                          "RPAzEmtTwiRRxlJfWJJegXbPQkvwH5Q17s8SeUzXhURXz")
    api = tweepy.API(auth)

    check_description = input('Do you want to change your description ? Y or N \n')

    if check_description.lower() == 'y':
        print("What do you want your description to be: ")
        profile = input()
        api.update_profile(description=profile)
        print('You updated your status to {}'.format(profile))
    else:
        print('OK! Your description remains the same!')
