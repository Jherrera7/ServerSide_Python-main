from flask import Flask, render_template, request, make_response, redirect
from flask_bootstrap import Bootstrap 
from logic.person import Person

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    
    return render_template('person_detail.html', value=p)


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)


@app.route('/update', methods=['POST'])
def update():
    for person in model:
        if person.id_person == request.form['id_person']:
            model.remove(person)

    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)

"ACTUALIZACION DE PERSONAS"
@app.route('/update_person/<string:id>', methods=['GET'])
def update_person(id):
    data = 0
    for person in model:
        if person.id_person == id:
            data = person

    return render_template('update_person.html', data=data)

"ELIMINAR PERSONAS"
@app.route('/delete_person/<string:id>')
def delete_person(id):
    for person in model:
        if person.id_person == id:
            model.remove(person)

    return redirect('/people')


if __name__ == '__main__':
    app.run(debug=True)
