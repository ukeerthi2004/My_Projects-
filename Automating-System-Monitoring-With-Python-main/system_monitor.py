import psutil
import schedule
import time
import logging
import os

# ------------------- Logging Configuration -------------------
logging.basicConfig(
    filename='system_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ------------------- Utility Functions -------------------

def log_message(message):
    logging.info(message)

def print_alert(message):
    print(f"ALERT: {message}")

# ------------------- System Health Checks -------------------

def check_cpu_usage(threshold=50):
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > threshold:
            message = f"High CPU usage detected: {cpu_usage}%"
            log_message(message)
            print_alert(message)
    except Exception as e:
        logging.error(f"CPU check failed: {e}")

def check_memory_usage(threshold=80):
    try:
        memory_usage = psutil.virtual_memory().percent
        if memory_usage > threshold:
            message = f"High memory usage detected: {memory_usage}%"
            log_message(message)
            print_alert(message)
    except Exception as e:
        logging.error(f"Memory check failed: {e}")

def check_disk_space(path='C:\\', threshold=75):
    try:
        disk_usage = psutil.disk_usage(path).percent
        if disk_usage > threshold:
            message = f"Low disk space detected: {disk_usage}%"
            log_message(message)
            print_alert(message)
    except Exception as e:
        logging.error(f"Disk check failed: {e}")

def check_network_traffic(threshold=100 * 1024 * 1024):
    try:
        counters = psutil.net_io_counters()
        total_bytes = counters.bytes_recv + counters.bytes_sent

        if total_bytes > threshold:
            mb = total_bytes / (1024 * 1024)
            message = f"High network traffic detected: {mb:.2f} MB"
            log_message(message)
            print_alert(message)
    except Exception as e:
        logging.error(f"Network check failed: {e}")

# ------------------- File Cleanup (File Management) -------------------

def cleanup_old_files(folder='sample_folder', days=7):
    try:
        now = time.time()
        cutoff = now - days * 86400

        if not os.path.exists(folder):
            os.makedirs(folder)
            logging.info(f"Created cleanup folder: {folder}")
            return

        for file in os.listdir(folder):
            path = os.path.join(folder, file)
            if os.path.isfile(path):
                if os.stat(path).st_mtime < cutoff:
                    os.remove(path)
                    logging.info(f"Deleted old file: {file}")

    except Exception as e:
        logging.error(f"File cleanup failed: {e}")

# ------------------- Main Health Check Runner -------------------

def run_health_checks():
    try:
        print("Monitoring the system...")
        log_message("Running system health checks...")

        check_cpu_usage()
        check_memory_usage()
        check_disk_space()
        check_network_traffic()

        log_message("Health checks completed.")

    except Exception as e:
        logging.error(f"Health check execution failed: {e}")

# ------------------- Scheduling -------------------

# Run monitoring every 1 minute
schedule.every(1).minutes.do(run_health_checks)

# Run file cleanup once per day
schedule.every().day.do(cleanup_old_files)

# ------------------- Main Loop -------------------

if __name__ == "__main__":
    logging.info("Automated System Monitoring Tool Started")
    print("System Monitoring Tool Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)
