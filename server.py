from flask import Flask, request, send_file, make_response, jsonify
import subprocess
import os.path

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload_netlist():
    # get text from request body
    if not request.data:
        return "No netlist text provided", 400
        
    netlist_text = request.data.decode("utf-8")
    
    # remove markdown code block markers if present
    if netlist_text.startswith("```") and netlist_text.endswith("```"):
        # remove first line
        first_newline = netlist_text.find("\n")
        if first_newline != -1:
            netlist_text = netlist_text[first_newline + 1 :]
        # remove last line
        last_newline = netlist_text.rfind("\n")
        if last_newline != -1:
            netlist_text = netlist_text[:last_newline]
    
    # save the netlist text to file
    netlist_path = "received_netlist.cir"
    with open(netlist_path, "w") as f:
        f.write(netlist_text)
    
    # simulate the netlist with ngspice
    try:
        subprocess.run(["ngspice", "-b", netlist_path], check=True)
        
        # ngspice output -> csv and plot
        subprocess.run(["python", "plot.py"], check=True)
        print("Simulation and plot generation successful!")
        
        # return the image file
        if os.path.exists("bode_plot.png"):
            return send_file(
                "bode_plot.png",
                mimetype="image/png",
                as_attachment=True,
                download_name="bode_plot.png",
            )
        else:
            return "Plot generation failed", 500
            
    except subprocess.CalledProcessError as e:
        return f"Simulation failed: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)