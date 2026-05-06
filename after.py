# 学生成绩计算程序 - 重构后（无代码坏味道）

# 提取公共方法：解决重复代码 + 函数过长问题
def calculate_and_show_score(math, english, science):
    """计算总分、平均分并输出结果（公共复用函数）"""
    total = math + english + science
    average = total / 3
    result = "及格" if average >= 60 else "不及格"
    print(f"总分：{total}，平均分：{average:.2f} - {result}")

# 业务函数：仅传入数据，无重复代码
def calculate_student_score_1():
    calculate_and_show_score(85, 90, 78)

def calculate_student_score_2():
    calculate_and_show_score(92, 88, 95)

# 调用函数
calculate_student_score_1()
calculate_student_score_2()
