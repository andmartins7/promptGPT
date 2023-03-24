from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Configure OpenAI API key
if "OPENAI_API_KEY" in os.environ:
    openai.api_key = os.environ["OPENAI_API_KEY"]
else:
    print("Erro: variável de ambiente OPENAI_API_KEY não definida.")
    exit()

# Define home page
@app.route("/")
def home():
    return render_template("home.html")

# Define endpoint for generating prompts
@app.route("/generate_prompts", methods=["POST"])
def generate_prompts():
    try:
        prompt = request.form.get("prompt")
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return render_template("result.html", prompt=prompt, result=response.choices[0].text)
    except Exception as e:
        print("Error:", e)
        return render_template("error.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True)
