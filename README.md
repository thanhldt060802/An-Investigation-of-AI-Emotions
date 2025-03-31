Truy cập trang chủ OpenAI để tạo API_KEY, sau khi tạo API_KEY, gán nó vào biến OPENAI_API_KEY của tệp cấu hình môi trường .env
<br>
Ngoài ra còn có thể điều chỉnh các mô hình được cho phép để có thể sử dụng bởi API_KEY (phụ thuộc vào tài khoản)
<br><br>

Sử dụng phiên bản Python yêu cầu là 3.13.1
<br><br>
Tại thư mục dự án chạy lệnh sau để kích hoạt môi trường ảo trên dự án: <br>
Scripts\activate.bat
<br><br>
Tại thư mục dự án chạy lệnh sau để cài các thư viện cần thiết:<br>
pip install -r requirements.txt
<br><br>
Tại thư mục dự án chạy lệnh sau để khởi động dự án bởi uvicorn:<br>
uvicorn app:app --reload --host 0.0.0.0 --port 8000
<br><br>

Bây giờ ta có thể gửi các request để kiểm thử, có dạng là POST, body như sau:<br>
<code>
{"user_input": "Content"}
</code>
