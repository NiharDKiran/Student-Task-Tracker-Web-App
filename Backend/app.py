from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__, template_folder="../Frontend")
app.secret_key = "super-secret-for-flash"

tasks = []  

def add_task(name, task, status):
    tasks.append({"name": name, "task": task, "status": status})

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    try:
        name = request.form.get("name", "").strip()
        task = request.form.get("task", "").strip()
        status = request.form.get("status", "Pending")

        if not name or not task:
            flash("Name and Task are required.", "error")
            return redirect(url_for("index"))

        add_task(name, task, status)
        flash("Task added successfully.", "success")
        return redirect(url_for("index"))

    except Exception as ex:
        flash(f"Error: {ex}", "error")
        return redirect(url_for("index"))

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    try:
        if 0 <= task_id < len(tasks):
            tasks.pop(task_id)
            flash("Task deleted successfully.", "success")
        else:
            flash("Invalid task ID.", "error")
    except Exception as ex:
        flash(f"Error: {ex}", "error")
    return redirect(url_for("index"))

@app.route("/view", methods=["GET"])
def view():
    return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)
