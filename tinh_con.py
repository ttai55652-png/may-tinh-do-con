import streamlit as st
import math

st.set_page_config(page_title="Máy Tính Độ Côn", layout="centered")

st.title("🛠 Công Cụ Tính Độ Côn")
st.write("Nhập các thông số để tính độ côn và góc nghiêng.")

# Nhập liệu
D = st.number_input("Đường kính trục lớn (D)", value=50.0)
d = st.number_input("Đường kính trục nhỏ (d)", value=40.0)
L = st.number_input("Chiều dài đoạn côn (L)", value=100.0)

if st.button("Tính toán"):
    if L > 0:
        # Tính độ côn C
        C = (D - d) / L
        # Tính góc nghiêng (alpha/2)
        tan_half_alpha = (D - d) / (2 * L)
        angle_rad = math.atan(tan_half_alpha)
        angle_deg = math.degrees(angle_rad)
        
        # Hiển thị kết quả
        st.success(f"**Kết quả:**")
        st.write(f"- Độ côn (C): **1:{1/C:.2f}** (hoặc {C:.4f})")
        st.write(f"- Góc nghiêng bàn trượt (α/2): **{angle_deg:.3f}°**")
        
        # Chuyển đổi sang độ - phút
        degrees = int(angle_deg)
        minutes = int((angle_deg - degrees) * 60)
        st.info(f"👉 Xoay bàn trượt: **{degrees}° {minutes}'**")
    else:
        st.error("Chiều dài L phải lớn hơn 0")