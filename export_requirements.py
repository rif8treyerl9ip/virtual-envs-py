import os
import subprocess
from datetime import datetime

# 環境変数を使用してenvsディレクトリへのパスを設定
home_dir = os.environ.get('USERPROFILE') or os.environ.get('HOME')
envs_dir = os.path.join(home_dir, 'envs')

current_date = datetime.now().strftime('%Y%m%d')

for env_name in os.listdir(envs_dir):
    env_path = os.path.join(envs_dir, env_name)
    if os.path.isdir(env_path):
        activate_script = os.path.join(env_path, 'bin', 'activate') if os.name != 'nt' else os.path.join(env_path, 'Scripts', 'activate')
        
        # pip freezeコマンドを実行し、結果をファイルに出力
        output_filename = os.path.join(envs_dir, f'{current_date}_{env_name}_requirements.txt')
        command = f'source {activate_script} && pip freeze > {output_filename}' if os.name != 'nt' else f'cmd /c "{activate_script} && pip freeze > {output_filename}"'
        
        subprocess.run(command, shell=True, executable='/bin/bash' if os.name != 'nt' else None)

        print(f'Processed virtual environment: {env_name}')
