import json
import os
import flask
from flask import Flask, request, abort, jsonify, make_response
from flask_cors import CORS, cross_origin
from datetime import date, datetime
import random
from flask_migrate import Migrate
from models import *

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
    # create and configure the app
    #==============================================================
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    migrate = Migrate(app, db)
    #==============================================================

    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}}) 

    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    @app.after_request 
    def after_request(response): 
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true') 
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS') 
        return response 
    
    @app.route('/')
    @cross_origin() 
    def welcome_app(): 
        return jsonify({'App': 'Trivia API Application'})

    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.Pz
    """
    @app.route('/get-categories')
    @cross_origin() 
    def get_categories():
        try:
            categories = Category.query.all()
            formatted_categories = [cate.format() for cate in categories]
            return jsonify({
                'success': True,
                'categories': formatted_categories
            })
        except Exception as e:
            print(e)
        

    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """
    @app.route('/get-questions')
    @cross_origin() 
    def get_questions():
        try:
            page = request.args.get('page', 1, type=int)
            start = (page - 1) * 10
            end = start + 10
            questions = Question.query.all()
            formatted_questions = [ques.format() for ques in questions]

            categories = Category.query.all()
            formatted_categories = [cate.format() for cate in categories]
            return jsonify({
                'success': True,
                'questions':formatted_questions[start:end],
                'total_questions':len(formatted_questions),
                'current_category': '',
                'categories': formatted_categories
            })
        except Exception as e:
            print(e)

    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """
    @app.route('/delete-question/<int:question_id>', methods=["DELETE"])
    @cross_origin() 
    def delete_question(question_id):
        try:
            question = Question.query.get_or_404(question_id)
            db.session.delete(question)
            db.session.commit()
            return jsonify({'result': 'Delete question successfully'})
        except Exception as e:
            print(e)

    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """
    @cross_origin()
    @app.route('/create-questions', methods = ['POST'])
    def create_questions():
        try:
            question = Question(
                question=request.json['question'], 
                answer=request.json['answer'], 
                category=request.json['difficulty'], 
                difficulty=request.json['category']
            )
            db.session.add(question)
            db.session.commit()
            return jsonify({"response": "Created successfully"})
        except Exception as e:
                print(e)

    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """
    @cross_origin() 
    @app.route('/search-questions', methods=['POST'])
    def search_questions():
        try:
            search = request.json['searchTerm']
            questions = Question.query.filter(Question.question.ilike(f'%{search}%')).all()
            categories = Category.query.all()

            page = request.args.get('page', 1, type=int)
            start = (page - 1) * 10
            end = start + 10
            formatted_questions = [ques.format() for ques in questions]

            formatted_categories = [cate.format() for cate in categories]
            return jsonify({
                'success': True,
                'questions':formatted_questions[start:end],
                'total_questions':len(formatted_questions),
                'current_category': '',
                'categories': formatted_categories
            })
        except Exception as e:
            print(e)

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """
    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def category_questions(category_id):
        try:
            category = Category.query.get_or_404(category_id)

            questions = Question.query.filter_by(category=category_id).all()
            page = request.args.get('page', 1, type=int)
            start = (page - 1) * 10
            end = start + 10
            formatted_questions = [ques.format() for ques in questions]

            return jsonify({
                'success': True,
                'questions':formatted_questions[start:end],
                'total_questions':len(formatted_questions),
                'current_category': category.type,
            })
        except Exception as e:
            print(e)
    

    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """
    @cross_origin()
    @app.route('/quizzes', methods = ['POST'])
    def quizzes():
        try:
            previous_questions = request.json['previous_questions']
            category_id = request.json['quiz_category']
            question_id = 0
            force_end = False
            
            if(len(previous_questions) > 0):
                questions = Question.query.filter(Question.id.notin_(previous_questions), Question.category==category_id).all()
                if len(questions) == 0:
                    question_id = None
                for question in questions:
                    question_id = question.id

            question = Question.query.filter(Question.category==category_id).first()
            if question_id == 0:
                force_end = False
            elif question_id == None:
                force_end = True
            else:
                question = Question.query.filter(Question.category==category_id, Question.id==question_id).first()

            return jsonify({
                "question": question.format(),
                "force_end": force_end
            })
        except Exception as e:
            print(e)

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found"
        }), 404
    
    @app.errorhandler(422)
    def handle_unprocessable_entity(err):
        exc = getattr(err, 'exc')
        if exc:
            messages = exc.messages
        else:
            messages = ['Invalid request']
        return jsonify({
            "success": False,
            "error": 422,
            "message": messages
        }), 422

    return app

