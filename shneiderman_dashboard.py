import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📈 Dasbor Analisis dengan Shneiderman's Mantra")

# Simulasi Data
df = pd.DataFrame({
    'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun'],
    'Wilayah_A': [100, 150, 130, 180, 200, 250],
    'Wilayah_B': [120, 110, 160, 140, 190, 210]
})

# 1. OVERVIEW FIRST (Ringkasan metrik secara makro)
st.subheader("1. Overview First")
col1, col2 = st.columns(2)
col1.metric("Total Penjualan Wilayah A", f"{df['Wilayah_A'].sum()} Unit")
col2.metric("Total Penjualan Wilayah B", f"{df['Wilayah_B'].sum()} Unit")

# 2. ZOOM AND FILTER (Kontrol pengguna untuk menyaring informasi)
st.subheader("2. Zoom and Filter")
pilihan_wilayah = st.selectbox("Pilih Wilayah untuk Dianalisis:", ["Semua", "Wilayah_A", "Wilayah_B"])

if pilihan_wilayah == "Semua":
    grafik_data = df.melt(id_vars='Bulan', value_vars=['Wilayah_A', 'Wilayah_B'])
else:
    grafik_data = df[['Bulan', pilihan_wilayah]].rename(columns={pilihan_wilayah: 'value'})
    grafik_data['variable'] = pilihan_wilayah

# 3. DETAILS-ON-DEMAND (Menampilkan detail spesifik hanya saat pengguna melakukan hover)
st.subheader("3. Details-on-Demand (Hover grafik di bawah)")
fig = px.bar(grafik_data, x='Bulan', y='value', color='variable', barmode='group')
fig.update_traces(hovertemplate='Bulan: %{x}<br>Jumlah: %{y} Unit') # Detail on demand
st.plotly_chart(fig, use_container_width=True)