# pipelines/my_pipeline/my_pipeline.py
from openwebui.pipeline import Pipeline

class MyPipeline(Pipeline):
    name = "最小化测试 Pipeline"

    def pipe(self, user_message, model_id, messages, body):
        # 直接返回 dict
        return {"result": "Pipeline 启动成功！"}
