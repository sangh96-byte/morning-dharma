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

run("git add .")
run('git commit -m "feat: 3번(이산선사 발원문), 4번(우리말 반야심경), 6번(경전독송의식) 독송 음원 플레이어 연동 및 배포"')
run("git push origin main")
