# 学生成绩计算程序 - 包含代码坏味道
def calculate_student_score_1():
    # 未使用变量（代码坏味道1）
    unused_var = "this is never used"
    
    # 学生1成绩计算
    math = 85
    english = 90
    science = 78
    # 重复代码块（代码坏味道2）
    total = math + english + science
    average = total / 3
    if average >= 60:
        print(f"总分：{total}，平均分：{average} - 及格")
    else:
        print(f"总分：{total}，平均分：{average} - 不及格")

def calculate_student_score_2():
    # 学生2成绩计算
    math = 92
    english = 88
    science = 95
    # 完全重复的代码块（代码坏味道2）
    total = math + english + science
    average = total / 3
    if average >= 60:
        print(f"总分：{total}，平均分：{average} - 及格")
    else:
        print(f"总分：{total}，平均分：{average} - 不及格")

# 调用函数
calculate_student_score_1()
calculate_student_score_2()
