#!/bin/sh

check() {
  echo -e "\e[1;34m[+] Verifying Challenge Integrity\e[0m"
  # Nutzt deine generierte sha256sum.txt
  sha256sum -c sha256sum
}

build_container() {
  echo -e "\e[1;34m[+] Building Challenge Docker Container\e[0m"
  docker build -t localhost/coffeebotv2 --platform linux/amd64 .
}

run_container() {
  echo -e "\e[1;34m[+] Running Challenge Docker Container on 127.0.0.1:80\e[0m"
  # Startet den Container mit einer Test-Flagge als Umgebungsvariable
  docker run --name coffeebotv2-chall --rm -p 127.0.0.1:8080:8080 -t -i \
    -e HOST=127.0.0.1 \
    -e PORT=8080 \
    -e TIMEOUT=30 \
    --read-only \
    --privileged \
    --platform linux/amd64 \
    localhost/coffeebotv2
}

kill_container() {
  echo -e "\e[1;31m[-] Stopping Challenge Container\e[0m"
  docker ps --filter "name=coffeebotv2-chall" --format "{{.ID}}" \
    | tr '\n' ' ' \
    | xargs docker stop -t 0 \
    || true
}

case "${1}" in
  "check")
    check
    ;;
  "build")
    build_container
    ;;
  "run")
    run_container
    ;;
  "kill")
    kill_container
    ;;
  *)
    check
    build_container && run_container
    ;;
esac