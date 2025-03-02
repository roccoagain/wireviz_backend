from flask import Flask, request, send_file
import os
import subprocess

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_netlist():
    # get netlist from request
    if 'netlist' not in request.files:
        return "No netlist file provided", 400
    
    netlist_file = request.files['netlist']
    
    # save the netlist file
    netlist_path = "received_netlist.cir"
    netlist_file.save(netlist_path)
    
    # simulate the netlist with ngspice
    subprocess.run(["ngspice", "-b", netlist_path], check=True)
    
    # ngspice output -> csv
    subprocess.run(["python", "toDesmos.py"], check=True)
    
    # return the csv
    return send_file("freq_mag_for_desmos.csv", 
                     as_attachment=True,
                     download_name="freq_mag_for_desmos.csv")

@app.route('/download')
def download():
    # send the last csv to the client
    return send_file("freq_mag_for_desmos.csv", 
                     as_attachment=True,
                     download_name="freq_mag_for_desmos.csv")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)