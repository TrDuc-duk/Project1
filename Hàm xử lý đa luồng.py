# Hàm xử lý đa luồng
def crack_zip_multithread(zip_path, password_list, num_threads=4):
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Gửi tất cả mật khẩu vào các luồng
        results = executor.map(lambda pwd: try_password(zip_path, pwd), password_list)