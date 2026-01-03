from flask import Blueprint, request, jsonify
from db import task_collection
from bson.objectid import ObjectId

task_bp = Blueprint("task_bp", __name__)
