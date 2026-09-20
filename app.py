from flask import Flask, jsonify, request

from models import db, User, Category, Note

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return {
        "message": "Notes API works"
    }


@app.route("/seed", methods=["POST"])
def seed():
    if User.query.count() == 0:
        user = User(name="Adam")
        db.session.add(user)

    if Category.query.count() == 0:
        db.session.add(Category(name="Study"))
        db.session.add(Category(name="Work"))

    db.session.commit()

    return {
        "message": "Seed completed"
    }


@app.route("/notes", methods=["GET"])
def get_notes():

    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 5))

    query = Note.query

    title = request.args.get("title")

    if title:
        query = query.filter(
            Note.title.contains(title)
        )

    pagination = query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    result = []

    for note in pagination.items:
        result.append({
            "id": note.id,
            "title": note.title,
            "content": note.content
        })

    return jsonify({
        "page": page,
        "total": pagination.total,
        "items": result
    })


@app.route("/notes", methods=["POST"])
def create_note():
    data = request.json

    note = Note(
        title=data["title"],
        content=data["content"],
        user_id=data["user_id"],
        category_id=data["category_id"]
    )

    db.session.add(note)
    db.session.commit()

    return {
        "message": "Note created",
        "id": note.id
    }, 201


@app.route("/notes/<int:note_id>", methods=["PUT"])
def update_note(note_id):
    note = Note.query.get(note_id)

    if not note:
        return {"error": "Not found"}, 404

    data = request.json

    note.title = data.get("title", note.title)
    note.content = data.get("content", note.content)

    db.session.commit()

    return {
        "message": "Note updated"
    }


@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    note = Note.query.get(note_id)

    if not note:
        return {"error": "Not found"}, 404

    db.session.delete(note)
    db.session.commit()

    return {
        "message": "Note deleted"
    }

@app.route("/notes/details")
def notes_details():

    notes = Note.query.all()

    result = []

    for note in notes:

        user = User.query.get(note.user_id)
        category = Category.query.get(note.category_id)

        result.append({
            "id": note.id,
            "title": note.title,
            "content": note.content,
            "user": user.name,
            "category": category.name
        })

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)