import numpy as np
 
# ---------------------------------------------------------------------------
# 1. Data
# ---------------------------------------------------------------------------
students = np.array(["S1", "S2", "S3", "S4", "S5"])
subjects = np.array(["Mathematics", "Physics", "Chemistry", "English"])
 
max_marks_per_subject = 100
num_subjects = len(subjects)
total_max_marks = num_subjects * max_marks_per_subject
 
# Rows = students, Columns = subjects
mid_sem_marks = np.array([
    [65, 70, 68, 72],   # S1
    [78, 75, 80, 77],   # S2
    [55, 60, 58, 62],   # S3
    [82, 85, 80, 88],   # S4
    [70, 68, 72, 74],   # S5
])
 
end_sem_marks = np.array([
    [72, 78, 75, 80],   # S1
    [84, 82, 86, 83],   # S2
    [65, 68, 66, 70],   # S3
    [88, 90, 85, 92],   # S4
    [78, 75, 80, 82],   # S5
])
 
# ---------------------------------------------------------------------------
# 2. Vectorized computations
# ---------------------------------------------------------------------------
# Total marks per student (sum across subjects -> axis=1)
mid_totals = mid_sem_marks.sum(axis=1)
end_totals = end_sem_marks.sum(axis=1)
 
# Average marks per student
mid_avg = mid_sem_marks.mean(axis=1)
end_avg = end_sem_marks.mean(axis=1)
 
# Percentage per student
mid_pct = (mid_totals / total_max_marks) * 100
end_pct = (end_totals / total_max_marks) * 100
 
# Percentage-point improvement from Mid-Sem to End-Sem
pct_improvement = end_pct - mid_pct
 
# ---------------------------------------------------------------------------
# 3. Report
# ---------------------------------------------------------------------------
def print_report():
    header = (f"{'Student':<10}{'Mid Total':>10}{'Mid Avg':>10}{'Mid %':>8}"
               f"{'End Total':>11}{'End Avg':>10}{'End %':>8}{'Improve':>10}")
    print(header)
    print("-" * len(header))
    for i, name in enumerate(students):
        print(f"{name:<10}{mid_totals[i]:>10}{mid_avg[i]:>10.2f}{mid_pct[i]:>8.2f}"
              f"{end_totals[i]:>11}{end_avg[i]:>10.2f}{end_pct[i]:>8.2f}"
              f"{pct_improvement[i]:>10.2f}")
 
    print("\nClass-wide stats:")
    print(f"  Average total marks (Mid-Sem): {mid_totals.mean():.2f}")
    print(f"  Average total marks (End-Sem): {end_totals.mean():.2f}")
    print(f"  Average % improvement        : {pct_improvement.mean():.2f}")
    print(f"  Best improved student        : {students[np.argmax(pct_improvement)]} "
          f"(+{pct_improvement.max():.2f}%)")
    print(f"  Least improved student        : {students[np.argmin(pct_improvement)]} "
          f"({pct_improvement.min():.2f}%)")
 
    print("\nSubject-wise class average:")
    subject_avg_mid = mid_sem_marks.mean(axis=0)
    subject_avg_end = end_sem_marks.mean(axis=0)
    for subj, m, e in zip(subjects, subject_avg_mid, subject_avg_end):
        print(f"  {subj:<12} Mid: {m:6.2f}   End: {e:6.2f}   Change: {e - m:+.2f}")
 
 
if __name__ == "__main__":
    print_report()
 
