import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False


class StudentScoreAnalysis:
    def __init__(self):
        
        self.students = [f'학생{i}' for i in range(1,21)]
        self.math = np.random.randint(50,100,len(self.students))
        self.english = np.random.randint(50,100,len(self.students))
        self.science = np.random.randint(50,100,len(self.students))

        self.data = {
            "Student" : self.students,
            "Math" : self.math,
            "English" : self.english,
            "Science" : self.science
        }

        self.df = pd.DataFrame(self.data)
        self.df['Total'] = self.df['Math']+self.df["English"]+self.df["Science"]

    def mean(self):
        math_mean = self.df['Math'].mean()
        english_mean = self.df['English'].mean()
        science_mean = self.df['Science'].mean()

        plt.bar(['수학', '영어', '과학'], [math_mean, english_mean, science_mean], color = 'orange')
        
        plt.title('과목별 평균 성적')
        plt.ylabel('평균 점수')

        plt.show()

    def top_5(self):
        top_idx = self.df['Total'].sort_values(ascending=False).head().index
        top_students = [self.df.iloc[i,0] for i in top_idx]
        top_mean = [self.df.iloc[i,4]/3 for i in top_idx]

        plt.bar(top_students, top_mean, color = 'green')

        plt.title('상위 5명의 평균 성적')
        plt.ylabel('평균 점수')

        plt.show()


score = StudentScoreAnalysis()
score.mean()
score.top_5()