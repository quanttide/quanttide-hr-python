import uuid
from pydantic import BaseModel
from typing import Optional

class Skill(BaseModel):
    skill_id: uuid.UUID
    title: str
    category: str

class SkillLevel(BaseModel):
    level_id: uuid.UUID
    value: int
    name: str
    description: str
    skill_id: uuid.UUID

class EmployeeSkill(BaseModel):
    employee_id: int
    skill_id: uuid.UUID
    skill_title: str
    skill_category: str
    skill_level: int
    skill_level_name: str
    skill_description: str

if __name__ == '__main__':
    # 创建 Skill 实例
    skill_python = Skill(skill_id=uuid.uuid4(), title="Python编程", category="计算机编程")
    skill_java = Skill(skill_id=uuid.uuid4(), title="Java编程", category="计算机编程")

    # 创建 SkillLevel 实例
    skill_level_ignorant = SkillLevel(
        level_id=uuid.uuid4(),
        value=0,
        name="无知",
        description="对该技能毫无认知",
        skill_id=skill_python.skill_id
    )
    skill_level_entry = SkillLevel(
        level_id=uuid.uuid4(),
        value=1,
        name="入门",
        description="基础知识",
        skill_id=skill_python.skill_id
    )
    skill_level_understand = SkillLevel(
        level_id=uuid.uuid4(),
        value=2,
        name="了解",
        description="基本了解",
        skill_id=skill_python.skill_id
    )
    skill_level_proficient = SkillLevel(
        level_id=uuid.uuid4(),
        value=3,
        name="熟悉",
        description="能够独立完成任务",
        skill_id=skill_python.skill_id
    )
    skill_level_adept = SkillLevel(
        level_id=uuid.uuid4(),
        value=4,
        name="擅长",
        description="在该领域有出色表现",
        skill_id=skill_python.skill_id
    )
    skill_level_expert = SkillLevel(
        level_id=uuid.uuid4(),
        value=5,
        name="精通",
        description="对该领域有深远影响",
        skill_id=skill_python.skill_id
    )

    # 创建 EmployeeSkill 实例
    employee_skill_python = EmployeeSkill(
        employee_id=1001,
        skill_id=skill_python.skill_id,
        skill_title=skill_python.title,
        skill_category=skill_python.category,
        skill_level=skill_level_proficient.value,
        skill_level_name=skill_level_proficient.name,
        skill_description=skill_level_proficient.description
    )

    # 打印实例
    print(skill_python)
    print(skill_java)
    print(skill_level_ignorant)
    print(skill_level_entry)
    print(skill_level_understand)
    print(skill_level_proficient)
    print(skill_level_adept)
    print(skill_level_expert)
    print(employee_skill_python)