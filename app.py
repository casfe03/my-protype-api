from flask import Flask, request, render_template
import openpyxl
import pandas as pd

app = Flask(__name__)

data = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global data

    if request.method == 'POST':
        file = request.files['file']
        # Processar o arquivo e obter os dados da planilha
        try:
            workbook = openpyxl.load_workbook(file)
            sheet = workbook.active
            data = pd.DataFrame(sheet.values)
            data.columns = data.iloc[0]
            data = data[1:].to_html(index=False)
            return "Dados da planilha recebidos com sucesso!"
        except Exception as e:
            return f"Erro ao processar o arquivo da planilha: {str(e)}"
    else:
        return render_template('index.html')

@app.route('/data', methods=['GET'])
def data_page():
    global data

    if data:
        return render_template('data.html', data=data)
    else:
        return "Nenhum dado disponível."

if __name__ == '__main__':
    app.run(debug=True)
