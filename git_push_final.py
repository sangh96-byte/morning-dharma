import subprocess
import sys
sys.stdout.reconfigure(encoding='utf-8')

def run(cmd):
    print("Running:", cmd)
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8', errors='replace')
    print("STDOUT:", res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)
    if res.returncode != 0:
        sys.exit(res.returncode)

run("git add -A")
run('git commit -m "feat: 1, 2, 4, 5, 8번 음원 추가/교체 및 예불 시작/단계 이동 시 자동 재생 연동"')
run("git push origin main")
