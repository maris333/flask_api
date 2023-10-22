from src import create_app, db
from src.models import Notes


def create_db(app):
    with app.app_context():
        db.create_all()


def main():
    app = create_app()

    create_db(app)

    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == '__main__':
    main()