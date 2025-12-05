import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('mydb.sqlite')  # mydb.sqlite が app.py と同じフォルダにある想定
    conn.row_factory = sqlite3.Row        # カラム名でアクセスできるようにする
    return conn

@app.route('/')
def inventory():
    conn = get_db_connection()
    products = conn.execute('SELECT product_id, category, item_name, stock_quantity, min_stock_quantity FROM Products').fetchall()
    conn.close()
    return render_template('inventory.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('mydb.sqlite')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def inventory():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM Products').fetchall()
    conn.close()
    return render_template('inventory.html', products=products)
# 入庫フォーム（GET）
@app.route('/stock_in', methods=['GET'])
def stock_in_form():
    conn = get_db_connection()
    products = conn.execute("SELECT product_id, item_name FROM Products").fetchall()
    conn.close()
    return render_template("stock_in.html", products=products)

# 入庫処理（POST）
@app.route('/stock_in', methods=['POST'])
def stock_in():
    product_id = request.form['product_id']
    quantity = int(request.form['quantity'])

    conn = get_db_connection()
    conn.execute(
        "UPDATE Products SET stock_quantity = stock_quantity + ? WHERE product_id = ?",
        (quantity, product_id)
    )
    conn.commit()
    conn.close()

    return redirect(url_for('inventory'))


# 入庫フォーム表示
@app.route('/stock_in', methods=['GET'])
def stock_in_form():
    conn = get_db_connection()
    products = conn.execute('SELECT product_id, item_name FROM Products').fetchall()
    conn.close()
    return render_template('stock_in.html', products=products)

# 入庫処理（フォーム送信後のPOST処理）
@app.route('/stock_in', methods=['POST'])
def stock_in():
    product_id = request.form['product_id']
    quantity = int(request.form['quantity'])

    conn = get_db_connection()
    conn.execute('UPDATE Products SET stock_quantity = stock_quantity + ? WHERE product_id = ?', (quantity, product_id))
    conn.commit()
    conn.close()

    return redirect(url_for('inventory'))
# 入庫フォーム表示（GET）
@app.route('/stock_in', methods=['GET'])
def stock_in_form():
    conn = get_db_connection()
    products = conn.execute('SELECT product_id, item_name FROM Products').fetchall()
    conn.close()
    return render_template('stock_in.html', products=products)

# 入庫処理（POST）
@app.route('/stock_in', methods=['POST'])
def stock_in():
    product_id = request.form['product_id']
    quantity = int(request.form['quantity'])

    conn = get_db_connection()
    conn.execute(
        'UPDATE Products SET stock_quantity = stock_quantity + ? WHERE product_id = ?',
        (quantity, product_id)
    )
    conn.commit()
    conn.close()

    return redirect(url_for('inventory'))


