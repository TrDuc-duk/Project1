# Hàm kiểm tra mật khẩu
def try_password(zip_path, password):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            zf.extractall(pwd=password.encode('utf-8'))
        return password
    except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile):
        return None