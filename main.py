# import the create app function from the website folder
from website import create_app

app = create_app()

# only run the web server if this file is run directly
if __name__ == '__main__':
    # rerun the website if we make changes during dev
    app.run(debug=True)


