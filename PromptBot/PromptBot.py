from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Configure OpenAI API key
openai.api_key = "OpenAI_API_key"

# Define home page
@app.route("/")
def home():
    return render_template("home.html")

# Define endpoint for generating prompts
@app.route("/generate_prompts", methods=["POST"])
def generate_prompts():
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

if __name__ == "__main__":
    app.run(debug=True)
