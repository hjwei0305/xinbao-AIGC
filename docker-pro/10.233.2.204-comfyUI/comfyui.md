1、激活环境
source venv/bin/activate
2、启动
nohup python3 main.py --listen 0.0.0.0 --port 8188 > comfyui.log 2>&1 &