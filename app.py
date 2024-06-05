from flask import Flask,  url_for, render_template, redirect, jsonify, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm

from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = 'shhh'

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.app_context().push()
connect_db(app)
db.create_all()

    
# # # # # # # # # # # # # # # # # # ROUTES # # # # # # # # # # # # # # # # # # # # # # # # # # 
@app.route('/', methods=['GET'])
def display_pet_index():
    '''Homepage diplays all pets including: name, photo, availability.'''
    pets = Pet.query.all()

    return render_template('pet-index.html', pets=pets)




@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        # data = {key: val for key, val in form.data.items() if key != 'csrf_token'}
        # pet = Pet(**data)
        pet = Pet(
            name = form.name.data,
            species = form.species.data,
            img_url = form.img_url.data,
            age = form.age.data,
            notes = form.notes.data
        )
        db.session.add(pet)
        db.session.commit()
        return redirect(url_for('display_pet_index'))

    else:
        return render_template('add-pet.html', form=form)
    


@app.route('/<int:pet_id>', methods=['GET','POST'])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.img_url = form.img_url.data,
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')

    else:
        return render_template('edit-pet.html', form=form, pet=pet)