from copy import Error
from distutils.log import debug
from flask import Flask, jsonify, make_response, render_template,request, redirect, url_for
from flask_restful import Resource, Api, reqparse
from instaloader import Instaloader, Profile

app =Flask(__name__)
api = Api(app)

# Setting routes for our web-pages:
@app.route("/")
def home():
    return render_template("home.html")
    

@app.route("/instagram-check", methods=["GET", "POST"])
# class checkuser(Resource):
def insta_prediction():
    account_prediction_text = ""
    if request.method == "POST":

        L = Instaloader()
        PROFILE = request.form["Name"]
        try:
            profile = Profile.from_username(L.context, PROFILE)
        except:
            result = 'Account not found'
            return render_template('result.html', account_prediction_text=result)
            
            # return jsonify({'result':'Account not found'})
        
        followers = (profile.followers)
        following = profile.followees
        if(followers == 0):
            followers = 1
        ratio = following/followers
        posts = profile.mediacount

        
        if(following < 100):
            # return jsonify({'result': 'Data is insufficient'})
            # return 'Data is insufficient', 201
            result = 'Data is insufficient'
        if(following > 100):
            if(ratio > 10):
                # return jsonify({'result':'Fake account'})
                result = 'Fake account'
            else:
                # return jsonify({'result':'Valid account'})
                result = 'Valid account'
    return render_template('result.html', account_prediction_text=result)
        
# api.add_resource(checkuser, '/user/<username>')        
if __name__ == "__main__":
    
    app.run(debug=True)
