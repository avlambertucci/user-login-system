from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
import uuid
from app import users_collection

class User:

  def start_session(self, user):
    del user['password']
    session['logged_in'] = True
    session['user'] = user
    return jsonify(user), 200


  def signup(self):
    print(request.form)
    #Create the user object from submitted fields
    user = {
      "_id": uuid.uuid4().hex,
      "name": request.form.get('name'),
      "email": request.form.get('email'),
      "password": request.form.get('password'),
    }
    #Encrypt password
    user['password'] = pbkdf2_sha256.encrypt(user['password'])
    #Checks if there is already a user with this email
    if users_collection.find_one({'email': user['email']}):
      return jsonify({"error": "Email address already in use"}), 400
    if users_collection.insert_one(user):
      return self.start_session(user)
    return jsonify({"error": "Signup failed"}), 400

  def signout(self):
    session.clear()
    return redirect('/')