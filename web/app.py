from flask import Flask, render_template, request
import os
from flask import redirect
from backend.checker.checker import run_checker
from backend.simulator.run_simulator import run_simulation


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


last_report = None


@app.route('/', methods=['GET', 'POST'])
def upload():
    global last_report

    if request.method == 'POST':
        file = request.files.get('file')
        if not file:
            return render_template('upload.html', report=None)

        path = os.path.join(UPLOAD_FOLDER, file.filename)
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        file.save(path)

        last_report = run_checker(path)

        # ✅ SAFETY CHECK
        if last_report and not last_report.get('errors'):
            return redirect('/simulate')

    return render_template('upload.html', report=last_report)


@app.route('/report')
def report():
    return render_template('report.html', report=last_report)


@app.route('/simulate')
def simulate():
    global last_report

    if not last_report:
        return "No validated package found. Please upload a package first.", 400

    result = run_simulation()
    return render_template('simulation.html', result=result)



if __name__ == '__main__':
    app.run(debug=True)