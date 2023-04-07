from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/scrum_master_view')
def scrum_master_view():
    return render_template('scrum_master_view.html')

@views.route('/scrum_team_member_view')
def scrum_team_member_view():
    return render_template('team_view.html')

@views.route('/create_poker_board')
def create_poker_board():
    return render_template('create_board.html')

@views.route('/t-shirt')
def tshirt():
    return render_template('t-shirt.html')

