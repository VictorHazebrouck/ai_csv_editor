from flask import Blueprint, request, current_app, jsonify, send_file
from werkzeug.datastructures import FileStorage
import pandas as pd
from pandas import DataFrame
from io import BytesIO
from app.ollama.modules import ask_ai

main = Blueprint('main', __name__)

@main.route('/generate', methods=['POST'])
def api_generate():

    csv_file: FileStorage | None = request.files.get('CSV')
    file_context: str | None = request.form.get('request_context')
    new_columns_titles: list[str] = request.form.getlist('new_column_title[]')
    new_culumns_prompts: list[str] = request.form.getlist('new_column_prompt[]')

    #validation
    if not csv_file:
        return jsonify({"error": ".csv file missing"}), 400

    if not file_context:
        return jsonify({"error": "Empty context"}), 400
    
    if "" in new_columns_titles:
        return jsonify({"error": "Empty title"}), 400
    
    if "" in new_culumns_prompts:
        return jsonify({"error": "Empty prompt"}), 400

    #create '''virtual table''' with passed in csv information
    dataFrame: DataFrame = pd.read_csv(csv_file, encoding='utf-8')

    #loop through each row of the table
    for index, row in dataFrame.iterrows():
        row_information = "|".join(str(value) for value in row)

        #for each row ask ai to fill new columns with provided prompt, row info, context
        for column_title, column_prompt in zip(new_columns_titles, new_culumns_prompts):
            dataFrame.at[index, column_title] = ask_ai(file_context, column_prompt, row_information)

    new_csv= BytesIO()
    dataFrame.to_csv(new_csv, index=False)
    new_csv.seek(0)


    return send_file(
        new_csv,
        as_attachment=True,
        download_name="CSV_modified.csv",
        mimetype="text/csv"
    )
