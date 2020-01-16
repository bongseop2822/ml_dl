# 엔트리 포인트 : 진입로, 시작점, 모든 경로법은 엔트로부터 따진다
# 1. 모듈 가져오기
from flask import Flask, render_template, request, jsonify, redirect
from ml.mod import *
from ml import PI2
# 2. Flask 객체 생성
app = Flask( __name__ )
# 3. 라우팅
@app.route('/')
def home():
  print( '-', PI, PI2 )
  return render_template('index.html')
# 4. 서버 가동
if __name__ == '__main__':
  app.run(debug=True)
else:
  print('작동 않됨')