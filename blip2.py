import pkg_resources
import subprocess

try:
    pkg_resources.get_distribution('salesforce-lavis')
    print("salesforce-lavis is installed.")
except pkg_resources.DistributionNotFound:
    print("Installing salesforce-lavis...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "salesforce-lavis"])