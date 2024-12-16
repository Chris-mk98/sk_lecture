class StudentScores:
    def __init__(self):
        self.scores = {}
        self.high = []
        self.low = []
    
    def get_data(self, file_name):
        try:
            with open(file_name, encoding='utf8') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.split(',')
                    self.scores[line[0]] = int(line[1])
        except:
            print("파일 읽기 오류")
    
    def total_score(self):
        return sum(self.scores.values())
    
    def mean_score(self):
        return self.total_score()/len(self.scores.values())

    def high_score(self):
        return [student for (student, score) in self.scores if score >= self.mean_score]

    def low_score(self):
        try:
            file = open('below_average_korean.txt', 'w')
            for (student, score) in self.scores:
                if score <= self.mean_score:
                    file.write(student,'\n')
        except:
            print("파일 쓰기 오류")

    def result_print(self):
        print(f"""

----------------------------------------------------------------

평균 점수: {self.mean_score}

평균 이상을 받은 학생들: {self.high_score}

----------------------------------------------------------------
""")
        

if __name__ == '__name__':
    Test = StudentScores()
    Test.getdata('scores_korean.txt')
    Test.low_score()
    Test.result_print()
    
