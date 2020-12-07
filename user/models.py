from flask import Flask, jsonify, request
from passlib.hash import pbkdf2_sha256
import uuid
from app import users_collection

class User:

  def signup(self):
    print(request.form)
    #Create the user object
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
      return jsonify(user), 200
    return jsonify({"error": "Signup failed"}), 400
