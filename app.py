from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run/<model_name>")
def run_model(model_name):
    # Validate model name
    valid_models = ["app1", "app2", "app3"]
    if model_name not in valid_models:
        return "Invalid model selection."

    # Launch the appropriate Streamlit model using subprocess (consider alternatives)
    import subprocess
    command = f"streamlit run {model_name}.py"
    subprocess.run(command.split(), shell=True)

    # Provide feedback to the user (optional)
    return f"Launched {model_name.upper()} Streamlit App!"

if __name__ == "__main__":
    app.run(debug=True)
