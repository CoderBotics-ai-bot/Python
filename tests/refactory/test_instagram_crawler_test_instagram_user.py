#from web_programming.instagram_crawler import *
#
#import pytest
#import os
#from unittest.mock import patch
#from InstagramUser import InstagramUser
#
#
#def test_test_instagram_user(username: str = "github") -> None:
#    mockData = {
#        "username": "username",
#        "fullname": "fullname",
#        "biography": "",
#        "user_data": {"key": "value"},
#        "website": "website",
#        "number_of_posts": 100,
#        "number_of_followers": 12001,
#        "number_of_followings": 20,
#        "is_verified": True,
#        "is_private": False,
#        "email": "email@domain.com",
#        "profile_picture_url": "profile_picture_url",
#    }
#    with patch.object(InstagramUser, "__init__", return_value=mockData):
#        instagram_user = InstagramUser(username)
#        assert instagram_user.user_data
#        assert isinstance(instagram_user.user_data, dict)
#        assert instagram_user.username == username
#        if username != "github":
#            return
#        assert instagram_user.fullname == "GitHub"
#        assert instagram_user.biography == "Built for developers."
#        assert instagram_user.number_of_posts > 150
#        assert instagram_user.number_of_followers > 120000
#        assert instagram_user.number_of_followings > 15
#        assert instagram_user.email == "support@github.com"
#        assert instagram_user.website == "https://github.com/readme"
#        assert instagram_user.profile_picture_url.startswith("https://instagram.")
#        assert instagram_user.is_verified is True
#        assert instagram_user.is_private is False
#
#
#def test_test_instagram_user_with_other_user() -> None:
#    mockData = {
#        "username": "username",
#        "fullname": "fullname",
#        "biography": "",
#        "user_data": {"key": "value"},
#        "website": "website",
#        "is_verified": True,
#        "is_private": False,
#        "email": "email@domain.com",
#        "profile_picture_url": "profile_picture_url",
#    }
#
#    with patch.object(InstagramUser, "__init__", return_value=mockData):
#        username = "other"
#        instagram_user = InstagramUser(username)
#        assert instagram_user.user_data
#        assert isinstance(instagram_user.user_data, dict)
#        assert instagram_user.username == username
#