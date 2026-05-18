from flask import Flask, render_template, request

app = Flask(__name__)


# 시작 페이지
@app.route('/')
def home():
    return render_template('index.html')


# 입력 페이지
@app.route('/form')
def form():
    return render_template('form.html')


# 결과 페이지
@app.route('/result', methods=['POST'])
def result():

    my_mbti = request.form.get('my_mbti')
    other_mbti = request.form.get('other_mbti')
    interest = request.form.get('interest')

    topics = []

    # 추천 로직
    if my_mbti == "INFP":
        topics.append("감성적인 영화 이야기")

    if other_mbti == "ESTJ":
        topics.append("계획 세우기 이야기")

    if interest == "음악":
        topics.append("좋아하는 가수 추천")

    if my_mbti == "INFP" and other_mbti == "ESTJ":
        topics.append("성격 차이 이야기")

    # 추천 없을 때
    if len(topics) == 0:
        topics.append("오늘 하루 이야기")

    return render_template('result.html', topics=topics)


# 서버 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)