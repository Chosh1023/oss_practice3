from fastapi import APIRouter
from model import StudentData
from model import Course 

func = APIRouter()
student_inform = []

# 점수 변환 기준
GRADE_MAP = {
    "A+": 4.5, "A": 4.0, "B+": 3.5, "B": 3.0,
    "C+": 2.5, "C": 2.0, "D+": 1.5, "D": 1.0, "F": 0.0
}
# gpa 계산 함수
def calculate_gpa(courses):
    total_credits = 0
    total_score = 0.0
    for course in courses:
        score = GRADE_MAP.get(course.grade.upper(), 0.0)
        total_credits += course.credits
        total_score += score * course.credits
    gpa = round(total_score / total_credits, 2)
    return gpa, total_credits


@func.post("/score")
async def process_student(data: StudentData):
    gpa, total_credits = calculate_gpa(data.courses)
    summary = {
        "student_id": data.student_id,
        "name": data.name,
        "gpa": gpa,
        "total_credits": total_credits
    }
    student_inform.append(summary)
    return {
        "msg" : "input success"
        }

@func.get("/score")
async def retrieve_student() -> dict:
    return {
        "student summary" : student_inform
    }