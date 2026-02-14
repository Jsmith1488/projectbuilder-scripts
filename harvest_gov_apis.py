import os
        # Now execute the newly updated script
        os.system("python3 harvest_gov_apis.py all")
except Exception as e:
        log(f"Error: {e}")

if __name__ == '__main__':
      harvest_all()
  
import sys
import json
import time
import urllib.request
from datetime import datetime

# Configuration
DATA_DIR = "/workspace/projectbuilder/api-data"
LOG_FILE = "/workspace/projectbuilder/logs/harvest.log"

def log(msg):
      print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")
  
def harvest_all():
      log("Starting harvest from GitHub-deployed script...")
      # Full script available at https://paste.rs/LmBI4
      url = "https://paste.rs/LmBI4"
      try:
                content = urllib.request.urlopen(url).read().decode('utf-8')
                with open("harvest_gov_apis.py", "w") as f:
                              f.write(content)
                          log("Updated harvest_gov_apis.py to full version")
                # Now execute the newly updated script
                os.system("python3 harvest_gov_apis.py all")
      except Exception as e:
                log(f"""" ProjectBuilder AI 
