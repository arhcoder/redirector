from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/redirect", methods=["GET"])
def redirect_url():
    target_url = request.args.get("url")
    if target_url:
        return redirect(target_url)
    else:
        return "No se proporcionó una URL para redirigir", 400

if __name__ == "__main__":
    app.run()