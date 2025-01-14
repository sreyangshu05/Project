from flask import Flask, render_template, request, redirect, url_for   # type: ignore
import sqlite3  

app = Flask(__name__)  

# Initialize the database  
def init_db():  
    conn = sqlite3.connect('stories.db')  
    cursor = conn.cursor()  
    cursor.execute('''  
        CREATE TABLE IF NOT EXISTS stories (  
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            title TEXT NOT NULL,  
            content TEXT NOT NULL  
        )  
    ''')  
    conn.commit()  
    conn.close()  

@app.route('/')  
def home():  
    conn = sqlite3.connect('stories.db')  
    cursor = conn.cursor()  
    cursor.execute('SELECT * FROM stories')  
    stories = cursor.fetchall()  
    conn.close()  
    return render_template('index.html', stories=stories)  

@app.route('/submit', methods=['POST'])  
def submit_story():  
    title = request.form['title']  
    content = request.form['content']  

    if title and content:  
        conn = sqlite3.connect('stories.db')  
        cursor = conn.cursor()  
        cursor.execute('INSERT INTO stories (title, content) VALUES (?, ?)', (title, content))  
        conn.commit()  
        conn.close()  
    return redirect(url_for('home'))  

if __name__ == '__main__':  
    init_db()  
    app.run(debug=True)  
