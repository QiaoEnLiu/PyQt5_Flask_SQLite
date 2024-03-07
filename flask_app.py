from flask import Flask, jsonify
import sqlite3

sql_path='SentrakSQL/SentrakSQL.db'
app = Flask(__name__)

def init_db():
    conn = sqlite3.connect(sql_path)
    # cursor = conn.cursor()
    # cursor.execute('''
    #     CREATE TABLE IF NOT EXISTS users (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         username TEXT NOT NULL,
    #         email TEXT NOT NULL
    #     )
    # ''')
    conn.commit()
    conn.close()

def get_R4X_Datas():
    conn = sqlite3.connect(sql_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM R4X')
    datas = cursor.fetchall()
    conn.close()

    data_list = [{'Reg': data[0], 'Name': data[1], 'Value': data[2]} for data in datas]
    return data_list

# def selectSQL_R4X_Reg(reg):
#     # 連接到SQLite數據庫（如果不存在，將創建一個新的）
#     conn = sqlite3.connect(sql_path)

#     # 設置 row_factory 為 sqlite3.Row，以便查詢結果以字典形式返回
#     conn.row_factory = sqlite3.Row

#     # 創建一個游標對象來執行SQL語句
#     cursor = conn.cursor()

#     # 查詢整個表格的數據
#     cursor.execute('SELECT * FROM R4X WHERE Reg = ?', (reg,))
#     reg_data = cursor.fetchall()

#     # 關閉游標和連接
#     cursor.close()
#     conn.close()

#     return dict(reg_data[0]) if reg_data else {}

@app.route('/', methods=['GET'])
def api_get_R4X_datas():
    datas = get_R4X_Datas()
    return jsonify({'R4X': datas})

def flaskActivate():
    return 'Flask API Activate'


if __name__ == '__main__':
    print(flaskActivate())
    init_db()
    app.run(debug = True, port = 5000)