from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        df = pd.read_excel(file)
        data = df.to_html(index=False)
        return render_template('page.html', data=data)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
