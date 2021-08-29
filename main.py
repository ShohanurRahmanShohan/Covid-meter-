import requests
from bs4 import BeautifulSoup
from flask import Flask , render_template

app = Flask(__name__)
@app.route("/")
def main():
    return render_template("index.html", cdb=cd, cdn=cn, cdr=cr,cwn=wcn, cwr=wcr, cwd=wcd)

web = "https://www.worldometers.info/coronavirus/country/bangladesh/"
web2= "https://www.worldometers.info/coronavirus/"
page = requests.get(web)
soup = BeautifulSoup(page.content,'html.parser')
cn = soup.find_all(class_="maincounter-number")[0].get_text()
cd = soup.find_all(class_="maincounter-number")[1].get_text()
cr = soup.find_all(class_="maincounter-number")[2].get_text()
page2 = requests.get(web2)
soup2 = BeautifulSoup(page2.content,'html.parser')
wcn = soup2.find_all(class_="maincounter-number")[0].get_text()
wcd = soup2.find_all(class_="maincounter-number")[1].get_text()
wcr = soup2.find_all(class_="maincounter-number")[2].get_text()


if __name__ == '__main__':
    app.run(debug=True, port=8000 )