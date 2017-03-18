import os
import sys
import pickle
import tweepy

# pylint: disable=C0103
# -*- coding: utf-8 -*-

clear()

filename = os.path.basename(__file__)
fileexists = os.path.exists("keys-DO-NOT-COMMIT.txt")

if fileexists is False:
    consumer_key = raw_input("1 - Enter your Consumer Key: ")
    consumer_secret = raw_input("2 - Enter your Consumer Secret Key: ")
    access_token = raw_input("3 - Enter your Access Token: ")
    access_token_secret = raw_input("4 - Enter your Access Token Secret Key: ")
    keylist = [consumer_key, consumer_secret, access_token, access_token_secret]
    with open('keys-DO-NOT-COMMIT.txt', "wb") as keyloader:
        pickle.dump(keylist, keyloader)

else:
    with open('keys-DO-NOT-COMMIT.txt', "rb") as keyloader:
        keylist = pickle.load(keyloader)
        consumer_key = keylist[0]
        consumer_secret = keylist[1]
        access_token = keylist[2]
        access_token_secret = keylist[3]

# This will be the part where we will work on the API interaction.

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# This ones work for yourself, but they give a
# lot of info, so it's better to keep them off 
# until we find the # way to work with them.

# print(api.me())
# print(api.me().status)

print(api.me().contributors_enabled)
print(api.me().created_at)
print(api.me().default_profile)
print(api.me().default_profile_image)
print(api.me().description)
print(api.me().entities)
print(api.me().favourites_count)
print(api.me().followers_count)
print(api.me().following)
print(api.me().friends_count)
print(api.me().geo_enabled)
print(api.me().has_extended_profile)
print(api.me().id)
print(api.me().id_str)
print(api.me().lang)
print(api.me().listed_count)
print(api.me().location)
print(api.me().name)
print(api.me().needs_phone_verification)
print(api.me().notifications)
print(api.me().profile_background_color)
print(api.me().profile_background_image_url)
print(api.me().profile_background_image_url_https)
print(api.me().profile_background_tile)
print(api.me().profile_banner_url)
print(api.me().profile_image_url)
print(api.me().profile_image_url_https)
print(api.me().profile_link_color)
print(api.me().profile_location)
print(api.me().profile_sidebar_border_color)
print(api.me().profile_sidebar_fill_color)
print(api.me().profile_text_color)
print(api.me().profile_use_background_image)
print(api.me().protected)
print(api.me().screen_name)
print(api.me().statuses_count)
print(api.me().suspended)
print(api.me().time_zone)
print(api.me().translator_type)
print(api.me().url)
print(api.me().utc_offset)
print(api.me().verified)

# AttributeError: 'User' object has no attribute 'hashtags'
#----------------------------------
# print(api.me().coordinates)
# print(api.me()._json)
# print(api.me().favorite_count)
# print(api.me().favorited)
# print(api.me().geo)
# print(api.me().hashtags)
# print(api.me().in_reply_to_screen_name)
# print(api.me().in_reply_to_status_id)
# print(api.me().in_reply_to_status_id_str)
# print(api.me().in_reply_to_user_id)
# print(api.me().in_reply_to_user_id_str)
# print(api.me().indices)
# print(api.me().is_quote_status)
# print(api.me().is_translation_enabled)
# print(api.me().is_translator)
# print(api.me().place)
#print(api.me().retweet_count)
#print(api.me().retweeted)
# print(api.me().source)
# print(api.me().source_url)
# print(api.me().text)
# print(api.me().truncated)
# print(api.me().urls)
# print(api.me().user_mentions)
# print(api.me().User(follow_request_sent))
#----------------------------------
# print(api.me()._api)