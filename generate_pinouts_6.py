import os
import json

base_path = "/Users/stavrostsioulis/Code/github/stavros-tsioulis/voltdocs-public/entries/modules"

def single_opamp():
    return {"pkg": "dip8", "pins": ["OFFSET_N1", "IN-", "IN+", "V-", "OFFSET_N2", "OUT", "V+", "NC"]}

def dual_opamp():
    return {"pkg": "dip8", "pins": ["OUT1", "IN1-", "IN1+", "V-", "IN2+", "IN2-", "OUT2", "V+"]}

def quad_opamp():
    return {"pkg": "dip14", "pins": ["OUT1", "IN1-", "IN1+", "V+", "IN2+", "IN2-", "OUT2", "OUT3", "IN3-", "IN3+", "V-", "IN4+", "IN4-", "OUT4"]}

components = {
    "analog/ad620": {"pkg": "dip8", "pins": ["RG_1", "IN-", "IN+", "V-", "REF", "OUT", "V+", "RG_2"]},
    "analog/ca3130": {"pkg": "dip8", "pins": ["OFFSET_N1", "IN-", "IN+", "V-", "OFFSET_N2", "OUT", "V+", "STROBE"]},
    "analog/lm747": {"pkg": "dip14", "pins": ["IN1-", "IN1+", "OFFSET1", "V-", "OFFSET2", "IN2+", "IN2-", "V+", "OUT2", "OUT1", "V+", "NC", "V-", "NC"]},
    "analog/opa333": {"pkg": "sot23-5", "pins": ["OUT", "V-", "IN+", "IN-", "V+"]},
    "analog/tl074": quad_opamp(),
    "analog/tl081": single_opamp(),
    "analog/tlv2372": dual_opamp(),
    
    "audio/lm1875": {"pkg": "bottom5", "pins": ["IN+", "IN-", "V-", "OUT", "V+"]},
    "audio/tda2003": {"pkg": "bottom5", "pins": ["IN+", "IN-", "GND", "OUT", "VS"]},
    "audio/pt2399": {"pkg": "dip16", "pins": ["VCC", "REF", "AGND", "DGND", "CLK_O", "VCO", "CC1", "CC0", "OP1_OUT", "OP1_IN", "OP2_IN", "OP2_OUT", "LPF2_IN", "LPF2_OUT", "LPF1_IN", "LPF1_OUT"]},
    "audio/tda7052": {"pkg": "dip8", "pins": ["VS", "IN+", "IN-", "GND", "OUT+", "GND", "GND", "OUT-"]},
    
    "drivers/a4950": {"pkg": "dip8", "pins": ["GND", "IN2", "IN1", "VREF", "VBB", "OUT1", "LSS", "OUT2"]},
    "drivers/al8807": {"pkg": "sot23-5", "pins": ["SW", "GND", "CTRL", "SET", "VIN"]},
    "drivers/cat4238": {"pkg": "sot23-5", "pins": ["SW", "GND", "FB", "SHDN", "VIN"]},
    "drivers/drv8837": {"pkg": "dip8", "pins": ["VM", "OUT1", "OUT2", "GND", "IN2", "IN1", "nSLEEP", "VCC"]},
    "drivers/drv8871": {"pkg": "dip8", "pins": ["GND", "IN2", "IN1", "ILIM", "VM", "OUT1", "PGND", "OUT2"]},
    "drivers/ir2103": {"pkg": "dip8", "pins": ["VCC", "HIN", "LIN'", "COM", "LO", "VS", "HO", "VB"]},
    "drivers/ir2104": {"pkg": "dip8", "pins": ["VCC", "IN", "SD'", "COM", "LO", "VS", "HO", "VB"]},
    "drivers/ir2110": {"pkg": "dip14", "pins": ["LO", "COM", "VCC", "NC", "NC", "VS", "VB", "HO", "NC", "HIN", "SD", "LIN", "VDD", "VSS"]},
    "drivers/ir2153": {"pkg": "dip8", "pins": ["VCC", "RT", "CT", "COM", "LO", "VS", "HO", "VB"]},
    "drivers/ir2181": {"pkg": "dip8", "pins": ["VCC", "HIN", "LIN", "COM", "LO", "VS", "HO", "VB"]},
    "drivers/lm3914": {"pkg": "dip18", "pins": ["LED1", "V-", "V+", "RLO", "SIG", "RHI", "REF_OUT", "REF_ADJ", "MODE", "LED10", "LED9", "LED8", "LED7", "LED6", "LED5", "LED4", "LED3", "LED2"]},
    "drivers/lm3915": {"pkg": "dip18", "pins": ["LED1", "V-", "V+", "RLO", "SIG", "RHI", "REF_OUT", "REF_ADJ", "MODE", "LED10", "LED9", "LED8", "LED7", "LED6", "LED5", "LED4", "LED3", "LED2"]},
    "drivers/pt4115": {"pkg": "sot23-5", "pins": ["SW", "GND", "DIM", "CSN", "VIN"]},
    "drivers/sn754410": {"pkg": "dip16", "pins": ["1,2EN", "1A", "1Y", "GND", "GND", "2Y", "2A", "VCC2", "3,4EN", "3A", "3Y", "GND", "GND", "4Y", "4A", "VCC1"]},
    "drivers/tc4420": {"pkg": "dip8", "pins": ["VDD", "IN", "NC", "GND", "GND", "OUT", "OUT", "VDD"]},
    "drivers/tc4429": {"pkg": "dip8", "pins": ["VDD", "IN", "NC", "GND", "GND", "OUT'", "OUT'", "VDD"]},
    
    "interface/4n26": {"pkg": "dip6", "pins": ["A", "K", "NC", "E", "C", "B"]},
    "interface/cd4511": {"pkg": "dip16", "pins": ["B", "C", "LT'", "BI'", "LE", "D", "A", "VSS", "e", "d", "c", "b", "a", "g", "f", "VDD"]},
    "interface/pc817": {"pkg": "dip4", "pins": ["A", "K", "E", "C"]}
}

def guess_pin(name):
    if name in ["V+", "VDD", "VCC", "VCC1", "VCC2", "VM", "VS", "VIN", "VBB"]: return "power", "power-in"
    if name in ["V-", "VSS", "GND", "COM", "AGND", "DGND", "PGND"]: return "power", "power-in"
    if "IN+" in name or "IN-" in name or "SIG" in name or name in ["A", "B", "C", "D"]: return "analog", "input" if not name in ["A", "B", "C", "D"] else ("digital", "input")
    if "OUT" in name or name in ["LO", "HO", "1Y", "2Y", "3Y", "4Y", "e", "d", "c", "b", "a", "g", "f"]: return "digital", "output" if not "OUT" in name else ("analog", "output")
    if name == "NC": return "nc", "passive"
    if name in ["OFFSET", "BAL", "COMP", "REF", "RG", "VREF", "REF_ADJ", "REF_OUT", "RLO", "RHI"]: return "analog", "input"
    if "LED" in name: return "digital", "output"
    if name in ["A", "K", "E", "C", "B"]: return "other", "passive" # optocoupler
    return "digital", "input"

for comp, data in components.items():
    comp_path = os.path.join(base_path, comp)
    yaml_path = os.path.join(comp_path, "entry.yaml")
    pinouts_dir = os.path.join(comp_path, "pinouts")
    
    if os.path.exists(yaml_path):
        with open(yaml_path, 'r') as f:
            content = f.read()
        
        if "pinouts:" not in content:
            if "\nbody:" in content:
                content = content.replace("\nbody:", "\npinouts:\n  - id: ic\n    path: pinouts/ic.json\nbody:")
            elif "\nassets:" in content:
                content = content.replace("\nassets:", "\npinouts:\n  - id: ic\n    path: pinouts/ic.json\nassets:")
            else:
                content += "\npinouts:\n  - id: ic\n    path: pinouts/ic.json\n"
            
            with open(yaml_path, 'w') as f:
                f.write(content)
                
    os.makedirs(pinouts_dir, exist_ok=True)
    json_path = os.path.join(pinouts_dir, "ic.json")
    
    pinout_obj = {
        "$schema": "https://voltdocs.dev/schemas/pinout-1.json",
        "version": 1,
        "pins": [],
        "layout": {
            "package": "ic",
            "sides": {}
        }
    }
    
    for idx, name in enumerate(data["pins"]):
        p_type, p_dir = guess_pin(name)
        pin_def = {
            "id": str(idx + 1),
            "name": name,
            "type": p_type,
            "direction": p_dir,
            "description": f"Pin {name}"
        }
        pinout_obj["pins"].append(pin_def)
        
    pkg = data["pkg"]
    if pkg == "dip4":
        pinout_obj["layout"]["sides"]["left"] = ["1", "2"]
        pinout_obj["layout"]["sides"]["right"] = ["4", "3"]
    elif pkg == "dip6":
        pinout_obj["layout"]["sides"]["left"] = ["1", "2", "3"]
        pinout_obj["layout"]["sides"]["right"] = ["6", "5", "4"]
    elif pkg == "dip8":
        pinout_obj["layout"]["sides"]["left"] = [str(i) for i in range(1, 5)]
        pinout_obj["layout"]["sides"]["right"] = [str(i) for i in range(8, 4, -1)]
    elif pkg == "dip14":
        pinout_obj["layout"]["sides"]["left"] = [str(i) for i in range(1, 8)]
        pinout_obj["layout"]["sides"]["right"] = [str(i) for i in range(14, 7, -1)]
    elif pkg == "dip16":
        pinout_obj["layout"]["sides"]["left"] = [str(i) for i in range(1, 9)]
        pinout_obj["layout"]["sides"]["right"] = [str(i) for i in range(16, 8, -1)]
    elif pkg == "dip18":
        pinout_obj["layout"]["sides"]["left"] = [str(i) for i in range(1, 10)]
        pinout_obj["layout"]["sides"]["right"] = [str(i) for i in range(18, 9, -1)]
    elif pkg == "sot23-5":
        pinout_obj["layout"]["sides"]["left"] = ["1", "2", "3"]
        pinout_obj["layout"]["sides"]["right"] = ["5", "4"]
    elif pkg == "bottom5":
        pinout_obj["layout"]["sides"]["bottom"] = ["1", "2", "3", "4", "5"]
        
    with open(json_path, 'w') as f:
        json.dump(pinout_obj, f, indent=2)

print("Done processing 30 components.")
