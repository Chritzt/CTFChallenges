FROM docker.io/library/ubuntu@sha256:3f85b7caad41a95462cf5b787d8a04604c8262cdcdf9a472b8c52ef83375fe15 AS base

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y python3 python3-venv socat coreutils && apt-get clean

RUN python3 -m venv /.venv
ENV PATH="/.venv/bin:$PATH"

COPY requirements.txt /app/requirements.txt
RUN /.venv/bin/pip install --no-cache-dir --upgrade -r /app/requirements.txt 

FROM docker.io/opensuse/tumbleweed@sha256:b2daeb56bbe4edcc696af872ed0ad3d2ad0120e3fc0e06c791f16dcb5bed15ad 

RUN zypper -n install nsjail fakeroot && zypper -n clean --all

COPY --from=base / /jail

RUN mkdir -p /jail/app
COPY ./challenge /jail/app/challenge
RUN chmod +x /jail/app/challenge

RUN chown -R 1337:1337 /jail/app /jail/.venv

CMD ["nsjail", \
    "--mode", "l", \
    "--disable_proc", \
    "--time_limit", "30", \
    "--bindhost", "0.0.0.0", \
    "--port", "1337", \
    "--chroot", "/jail", \
    "--cwd", "/app", \
    "-u", "1337:1337:1", \
    "-g", "1337:1337:1", \
    "--", "/usr/bin/socat", "TCP-LISTEN:1337,fork,reuseaddr", "EXEC:/.venv/bin/python3 -u /app/challenge"]