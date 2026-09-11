FROM docker.io/library/ubuntu:24.04

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y python3 socat tar gpg coreutils sudo bash && \
    apt-get clean

# User 'analyst' erstellen
RUN useradd -ms /bin/bash analyst

# Das anfällige Skript erstellen
RUN mkdir -p /opt /home/analyst
COPY tech_diag.py /opt/tech_diag.py
RUN chmod 755 /opt/tech_diag.py

# Sudoers Konfiguration MIT SETENV direkt und sauber hinterlegen (löscht alte Regeln)
RUN echo "analyst ALL=(root) NOPASSWD: SETENV: /usr/bin/python3 /opt/tech_diag.py" > /etc/sudoers.d/analyst && \
    chmod 440 /etc/sudoers.d/analyst

RUN mkdir -p /root/evidence
COPY project_alpha_bkp.tar.gpg /root/evidence/project_alpha_bkp.tar.gpg
COPY secrets.conf /root/evidence/secrets.conf

# WICHTIG: Nur Root darf in diesen Ordner schauen oder die Dateien anfassen!
RUN chmod 700 /root && \
    chmod 700 /root/evidence && \
    chmod 600 /root/evidence/secrets.conf && \
    chmod 600 /root/evidence/project_alpha_bkp.tar.gpg && \
    chown -R root:root /root/evidence

# Home-Verzeichnis für den Analysten vorbereiten
COPY syslog.txt /home/analyst/syslog.txt
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh && chown -R analyst:analyst /home/analyst

USER analyst
WORKDIR /home/analyst

EXPOSE 1337
CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:/app/entrypoint.sh,pty,raw,echo=0"]