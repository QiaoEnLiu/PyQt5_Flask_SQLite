from flask_app import app as flask_app
from flask_app import selectSQL_R4X_Reg
# import requests

# response = request.get('http://localhost:5000/')
while True:
    reg=str(input('輸入Reg位址：'))
    print(selectSQL_R4X_Reg(reg = reg))