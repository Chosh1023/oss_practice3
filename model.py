from pydantic import BaseModel

# 과목 모델 
class Course(BaseModel):
    course_code: str
    course_name: str
    credits: int
    grade: str

# 학생 데이터 모델
class StudentData(BaseModel):
    student_id: str
    name: str
    courses: list[Course]