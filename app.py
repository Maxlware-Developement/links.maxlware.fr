# @eletrix

from flask import Flask,render_template,redirect

app = Flask(__name__, template_folder='html',static_folder='static')

links = {} #ex : {"random string": "https://example.com"}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/generate_link/<path:url>', methods=['POST'])
def generate_link(url):
    #add into the links dict
    import random, string   
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    links[random_string] = url
    return {"short_link": f"https://links.maxlware.fr/{random_string}"}

@app.route('/<string:short_link>')
def redirect(short_link):
    if short_link in links:
        return render_template("base/redirect.html", redirect_url=links[short_link])
    else:
        return render_template("index.html", error="Lien non trouvé.")
    
app.run(host='0.0.0.0', port=5004, debug=True)