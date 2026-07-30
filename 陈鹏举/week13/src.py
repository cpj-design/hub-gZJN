class SkillExecutor:
    """执行技能，注入上下文"""
    def __init__(self, ctx: dict):
        self.ctx = ctx

    async def execute(self, skill_name: str, **kwargs) -> str:
        skill = get_registry().get(skill_name)
        if not skill:
            raise ValueError(f"技能 {skill_name} 不存在")
        # 若 execute 是 async 函数，直接 await
        if inspect.iscoroutinefunction(skill.execute):
            result = await skill.execute(self.ctx, **kwargs)
        else:
            result = skill.execute(self.ctx, **kwargs)
        return str(result)
