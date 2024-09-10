from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# 데이터베이스 연결 함수
def get_db_connection():
    conn = sqlite3.connect('posts.db')
    conn.row_factory = sqlite3.Row
    return conn

# 데이터베이스 초기화
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            writer TEXT,
            write_at DATETIME DATETIME DEFAULT CURRENT_TIMESTAMP,
            count INTEGER default 0
        )
    ''')
    conn.commit()
    conn.close()

# 메인 페이지 (게시글 목록 및 작성)
@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)
    
# 게시글 작성 처리
@app.route('/create', methods=('POST','GET',))
def create():
    if request.method == 'GET':
        return render_template('create.html')
    
    title = request.form['title']
    content = request.form['content']
    writer = request.form['writer']

    if title and content:
        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title, content, writer) VALUES (?, ?, ?)', (title, content, writer))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return redirect(url_for('index'))
@app.route('/view/<int:id>')
def view(id):
    conn = get_db_connection()
    conn.execute('UPDATE posts set count = count + 1 where id = ?', (id, ))
    conn.commit()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (id,)).fetchone()
    conn.close()
    if post is None:
        return 'Post not found!'
    return render_template('view.html', post=post)

# 게시글 수정 페이지
@app.route('/edit/<int:id>')
def edit(id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (id,)).fetchone()
    conn.close()
    if post is None:
        return 'Post not found!'
    return render_template('edit.html', post=post)

# 게시글 수정 처리
@app.route('/update/<int:id>', methods=('POST',))
def update(id):
    title = request.form['title']
    content = request.form['content']
    writer = request.form['writer']

    if title and content:
        conn = get_db_connection()
        conn.execute('UPDATE posts SET title = ?, content = ?, writer = ? WHERE id = ?', (title, content, writer, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return redirect(url_for('edit', id=id))

# 게시글 삭제 처리
@app.route('/delete/<int:id>', methods=('POST',))
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
