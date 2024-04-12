from flask import Flask, render_template,request,session,url_for,redirect
import chat
import sqlite3


def create_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       username TEXT UNIQUE NOT NULL, 
                       password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

create_table()


app = Flask(__name__)
app.secret_key='abc@123'

@app.route('/')
def home():
    return render_template('index.html') 


@app.route('/about')
def about():
    return render_template('about.html') 




@app.route('/login', methods=['GET', 'POST'])
def login():



    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        
        connection.close()

        if user:
            session['username'] = username
            
            return redirect(url_for('chat_route'))
        else:
            return "Login Failed. Please check your credentials."

    return render_template('login.html')



@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        return redirect(url_for('login'))



    return render_template('signup.html') 



@app.route('/chat', methods = ['GET', 'POST'])
def chat_route():

    
    
    
            if request.method == 'POST':
                query = request.form.get('query')  # Get the search query from the form
                print(f"User Query: {query}")
                result = chat.chat(query)  # Pass the query to the chat function
                return render_template('chat.html', value=result)
            else:
                
                pass
            return render_template('chat.html') 
    


if __name__ == '__main__':
    app.run(debug=True)