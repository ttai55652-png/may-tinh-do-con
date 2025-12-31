import streamlit as st
import math

# Giao diện đơn giản
st.title("Máy Tính Độ Côn")

# 3 Input
D = st.number_input("Đường kính lớn (D)", value=50.0)
d = st.number_input("Đường kính nhỏ (d)", value=40.0)
L = st.number_input("Chiều dài (L)", value=100.0)

# 1 Output
if st.button("TÍNH TOÁN"):
    if L > 0:
        # Công thức: tan(alpha/2) = (D - d) / (2L)
        tan_half_alpha = (D - d) / (2 * L)
        angle_rad = math.atan(tan_half_alpha)
        angle_deg = math.degrees(angle_rad)
        
        # Hiển thị đúng định dạng x.xxx độ
        st.success(f"Kết quả: {angle_deg:.3f} độ")
    else:
        st.error("L phải lớn hơn 0")
