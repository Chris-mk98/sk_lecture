class StudentScores:
    def __init__(self):
        self.scores = {}
    
    def get_data(self, file_name):
        try:
            with open(file_name, encoding='utf8') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip().split(',')
                    self.scores[line[0]] = int(line[1])  # 이름, 점수
        except Exception as e:
            print(f"파일 읽기 오류: {e}")
    
    def total_score(self):
        return sum(self.scores.values())
    
    def mean_score(self):
        return self.total_score() / len(self.scores)
    
    def high_score(self):
        return [student for student, score in self.scores.items() if score >= self.mean_score()]
    
    def low_score(self):
        try:
            with open('below_average_korean.txt', 'w', encoding='utf8') as file:
                for student, score in self.scores.items():
                    if score < self.mean_score():
                        file.write(student + ' : ' + str(score) + '점\n')
        except Exception as e:
            print(f"파일 쓰기 오류: {e}")
    
    def result_print(self):
        print(f"""

----------------------------------------------------------------

평균 점수: {self.mean_score():.2f}

평균 이상을 받은 학생들: {'['+', '.join(self.high_score())+']'}

----------------------------------------------------------------
""")

# 실행 코드
if __name__ == '__main__':
    Test = StudentScores()
    Test.get_data('scores_korean.txt')  # 파일 이름
    Test.low_score()  # 평균 이하 학생 파일 저장
    Test.result_print()  # 결과 출력