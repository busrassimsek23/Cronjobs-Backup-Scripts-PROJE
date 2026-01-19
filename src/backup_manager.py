import subprocess
import datetime

def run_backup(source, destination):
    print(f"[{datetime.datetime.now()}] Yedekleme basliyor...")
    # Unix terminal komutunu calistiriyoruz (Terminal Automation)
    # Hatalari ve ciktilari yakaliyoruz (Unix I/O)
    try:
        result = subprocess.run(
            ['tar', '-czf', destination, source],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("Yedekleme basariyla tamamlandi.")
        else:
            print(f"Hata olustu (stderr): {result.stderr}")
            
    except Exception as e:
        print(f"Sistem hatasi: {e}")

if __name__ == "__main__":
    # Test amacli kullanim
    run_backup("/home/user/data", "/home/user/backups/backup.tar.gz")
