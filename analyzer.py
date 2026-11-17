log_file = "sample_logs/auth.log"

def analyze_log(file_path):
	failed_logins = 0
	failed_ips = {}

	with open(file_path, "r") as file:
		for line in file:
			if "FAILED" in line:
				failed_logins += 1
			
				parts = line.split()
				ip_address = parts[-1].split("=")[1]
				
				if ip_address in failed_ips:
					failed_ips[ip_address] += 1
				else:
					failed_ips[ip_address] = 1
	return failed_logins, failed_ips

failed_logins, failed_ips = analyze_log(log_file)

print(f"Failed login attempts: {failed_logins}")
print("Failed login attempts by IP:")

for ip, count in failed_ips.items():
	print(f"{ip}: {count}")

	if count >= 3:
		print(f"ALERT: Potential brute-force activity detected from {ip}")