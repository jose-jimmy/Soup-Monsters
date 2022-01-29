from copy import Error
from distutils.log import debug
from flask import Flask, jsonify, make_response,request, redirect, url_for
from flask_restful import Resource, Api, reqparse
from instaloader import Instaloader, Profile

app =Flask(__name__)
api = Api(app)

class checkuser(Resource):
    def get(self, username):
        L = Instaloader()
        PROFILE = username
        try:
            profile = Profile.from_username(L.context, PROFILE)
        except:
            return jsonify({'result':'Account not found'})
        
        followers = (profile.followers)
        following = profile.followees
        if(followers == 0):
            followers = 1
        ratio = following/followers
        posts = profile.mediacount

        
        if(following < 100):
            return jsonify({'result': 'Data is insufficient'})
            # return 'Data is insufficient', 201
        if(following > 100):
            if(ratio > 10):
                return jsonify({'result':'Fake account'})
            else:
                return jsonify({'result':'Valid account'})

        
api.add_resource(checkuser, '/user/<username>')        
if __name__ == "__main__":
    
    app.run(debug=True)