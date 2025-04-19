  
import random
import time
import sys
import logger

def type_out(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("")

def cinematic_banner():
    type_out("""
   ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗
  ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝
  ██║  ███╗███████║██║   ██║███████╗   ██║   
  ██║   ██║██╔══██║██║   ██║╚════██║   ██║   
  ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   
   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝ 
             THE GHOST - Ultimate Cyber Ops Simulation
""", delay=0.002)
    time.sleep(1)


def scan_target(target):
    type_out(f"[+] Stealth scanning {target}...", 0.03)
    time.sleep(1)
    open_port = random.choice([22, 80, 443, 3389])
    type_out(f"    [+] Open port detected: {open_port}")
    return open_port

def recon_target(target):
    type_out(f"[+] Gathering intelligence on {target}...", 0.03)
    time.sleep(1)
    ip = f"192.168.1.{random.randint(2, 255)}"
    type_out(f"    [*] IP Address Identified: {ip}")
    type_out("    [*] WHOIS Lookup: Classified Information")
    
def zero_day_discovery(target):
    type_out(f"[+] AI scanning for zero-day vulnerabilities on {target}...", 0.03)
    time.sleep(1)
    type_out("    [+] Zero-day exploit detected! Logging to DarkNet repository...")
    
def firewall_bypass(target):
    type_out(f"[+] Initiating firewall bypass on {target}...", 0.03)
    time.sleep(1)
    type_out("    [*] Bypassing intrusion detection systems...")
    time.sleep(1)
    type_out("    [+] Firewall successfully bypassed!")
    
def intrusion_sequence(target):
    type_out("[+] Initiating multi-layer intrusion sequence...", 0.03)
    time.sleep(1)
    type_out("    [*] Deploying stealth malware...")
    time.sleep(1)
    type_out("    [*] Elevating privileges and accessing secure data zones...")
    time.sleep(1)
    type_out("    [+] SYSTEM COMPROMISED. Unauthorized access granted.")
    
def ai_decision_module():
    type_out("[+] Activating AI decision module...", 0.03)
    time.sleep(1)
    decisions = ["Switching attack vector", "Engaging stealth mode", "Launching secondary payload"]
    decision = random.choice(decisions)
    type_out(f"    [*] AI Decision: {decision}")
    
def data_exfiltration(target):
    type_out(f"[+] Initiating data exfiltration from {target}...", 0.03)
    time.sleep(1)
    type_out("    [*] Compressing confidential files...")
    time.sleep(1)
    type_out("    [*] Encrypting data stream for secure transmission...")
    time.sleep(1)
    type_out("    [+] Data exfiltration complete. Files securely transmitted.")
    
def countermeasure_simulation(target):
    type_out(f"[+] {target} has activated countermeasures!", 0.03)
    time.sleep(1)
    type_out("    [*] AI adapting to resistance... Switching to evasive protocols.")
    time.sleep(1)
    type_out("    [+] Countermeasures bypassed through adaptive learning.")
    
def stealth_mode_toggle():
    modes = ["ACTIVE", "STEALTH"]
    current_mode = random.choice(modes)
    type_out(f"[+] Stealth mode toggled. Current mode: {current_mode}", 0.03)
    
def multi_target_attack():
    type_out("[+] Simulating multi-target attack sequence...", 0.03)
    targets = ["192.168.1.45", "192.168.1.78", "192.168.1.102"]
    for t in targets:
        type_out(f"    [*] Attacking secondary target: {t}")
        time.sleep(0.5)
    type_out("    [+] Multi-target operations executed.")
    
def self_destruct_protocol():
    type_out("[+] INITIATING SELF-DESTRUCT PROTOCOL...", 0.02)
    for i in range(3, 0, -1):   
        type_out(f"    [*] SELF-DESTRUCT IN {i}...", 0.2)  
    type_out("    [+] SYSTEM PURGED. ALL LOGS ENCRYPTED AND ERASED.", 0.02)

    
def ai_phishing_attack(target_email):
    type_out(f"[+] Deploying AI-driven phishing attack on {target_email}...", 0.03)
    email_templates = ["Fake Security Alert", "Account Compromise Warning", "Urgent Payment Required"]
    social_tactics = ["Voice Deepfake", "AI Chatbot Impersonation", "Spoofed MFA Request"]
    selected_template = random.choice(email_templates)
    selected_tactic = random.choice(social_tactics)
    type_out(f"    [*] Phishing payload sent: {selected_template} using {selected_tactic} tactic")
    
def main():
    cinematic_banner()
    target = input("Enter target IP or domain: ")
    recon_target(target)
    scan_target(target)
    zero_day_discovery(target)
    firewall_bypass(target)
    intrusion_sequence(target)
    ai_decision_module()
    data_exfiltration(target)
    countermeasure_simulation(target)
    stealth_mode_toggle()
    multi_target_attack()
    target_email = input("Enter target email for AI phishing attack: ")
    ai_phishing_attack(target_email)
    self_destruct_protocol()
    type_out("\n[+] OPERATION COMPLETE. All simulated actions executed flawlessly.", 0.03)
    
if __name__ == "__main__":
    main()
