from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def home():
    return "Payment application is running"


@app.route("/version")
def version():
    return {
        "application": "payment",
        "version": os.getenv("APP_VERSION", "unknown"),
        "git_commit": os.getenv("GIT_COMMIT", "unknown"),
        "jenkins_build": os.getenv("BUILD_NUMBER", "unknown"),
        "branch": os.getenv("BRANCH_NAME", "unknown"),
        "docker_image": os.getenv("DOCKER_IMAGE", "unknown")
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)