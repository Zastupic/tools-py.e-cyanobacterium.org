from flask import Blueprint, render_template

pixel_profile = Blueprint('pixel_profile', __name__)

@pixel_profile.route('/pixel_profiles', methods=['GET', 'POST'])
def pixel_profiles():
    return render_template("pixel_profiles.html")