from flask import Flask
app=Flask(__name__)
@app.route("/singh/<introduction>")
def netanya(introduction):
    return 'hello! im NETANYA SINGH %s'%introduction
if __name__ == "__main__":
    app.run()
