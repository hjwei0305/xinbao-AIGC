#!/usr/bin/env python3
import os
from modelscope.hub.snapshot_download import snapshot_download

# 模型信息
repo_id = 'BAAI/bge-large-zh-v1.5'
local_dir = '/opt/models/bge-large-zh-v1.5'

# 创建目录
os.makedirs(local_dir, exist_ok=True)

print(f"开始下载模型 {repo_id} 到 {local_dir} ...")

# 下载模型（不传 resume_download 和 force_download）
snapshot_download(
    repo_id=repo_id,
    local_dir=local_dir
)

print(f"模型下载完成，保存路径：{local_dir}")
