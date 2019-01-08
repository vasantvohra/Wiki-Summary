from flask import Flask
from flask import render_template
from flask import request

from wiki import *
#import jinja2
app=Flask(__name__)
#app.jinja_env.line_statement_prefix = '%'

@app.route("/", methods=['GET', 'POST'])
def application():
    phrase=""
    answer = None
    error=""
    if request.method=="POST":
        try:
            phrase = request.form["phrase"]
            if phrase.strip()=="":
                error="Think of any words and TYPE!"
            else:
                result=search(phrase)
                if result=="Sorry! not in Wiki":
                    error="Sorry! Not in wiki"
        except(SyntaxError) as e:
            error ="Could not understand"
            print("Error:" + str(e))

        try:
            if result!="Sorry! not in Wiki":
                answer=result
        except Exception as e:
            print(e)

    return render_template('main.html', phrase=phrase,
                           answer=answer, error=error)


if __name__ == "__main__":
    app.run(debug=True)
