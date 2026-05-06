# before.py - 包含明显的坏味道
def process_student1():
    # 未使用变量（死代码）
    debug_flag = True
    
    # 重复的成绩计算逻辑
    scores = [85, 90, 78]
    total = sum(scores)
    avg = total / len(scores)
    if avg >= 60:
        print(f"Student 1: Pass ({avg:.1f})")
    else:
        print(f"Student 1: Fail ({avg:.1f})")

def process_student2():
    # 完全重复的逻辑（复制粘贴的代码）
    scores = [92, 88, 95]
    total = sum(scores)
    avg = total / len(scores)
    if avg >= 60:
        print(f"Student 2: Pass ({avg:.1f})")
    else:
        print(f"Student 2: Fail ({avg:.1f})")

def process_student3():
    # 超长函数（把逻辑全堆在一起）
    print("=== Student 3 ===")
    scores = [70, 65, 80]
    total = sum(scores)
    avg = total / len(scores)
    grade = ""
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"Total: {total}, Avg: {avg:.1f}, Grade: {grade}")

# 调用
process_student1()
process_student2()
process_student3()
