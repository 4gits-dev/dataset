import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("curah_hujan_kota_bandung.csv")
    return df

df = load_data()

st.title("🌧️ Dashboard Curah Hujan Kota Bandung")

st.write("""
Dashboard ini menampilkan data **curah hujan bulanan** berdasarkan dataset resmi Kota Bandung.
Gunakan filter di bawah untuk memilih **tahun** dan **bulan** yang ingin dianalisis.
""")

# -----------------------------
# Konversi nama bulan ke urutan benar
# -----------------------------
bulan_order = [
    "JANUARI", "FEBRUARI", "MARET", "APRIL", "MEI", "JUNI",
    "JULI", "AGUSTUS", "SEPTEMBER", "OKTOBER", "NOVEMBER", "DESEMBER"
]

df["bulan"] = pd.Categorical(df["bulan"], categories=bulan_order, ordered=True)
df = df.sort_values(["tahun", "bulan"])

# -----------------------------
# Filter Tahun
# -----------------------------
tahun_list = sorted(df["tahun"].unique())
selected_year = st.selectbox("Pilih Tahun:", tahun_list)

df_year = df[df["tahun"] == selected_year]

# -----------------------------
# Filter Bulan
# -----------------------------
selected_months = st.multiselect(
    "Pilih Bulan:",
    bulan_order,
    default=bulan_order
)

filtered_df = df_year[df_year["bulan"].isin(selected_months)]

# -----------------------------
# Statistik Ringkas
# -----------------------------
st.subheader("📊 Statistik Curah Hujan")

col1, col2, col3 = st.columns(3)
col1.metric("Jumlah Bulan", len(filtered_df))
col2.metric("Total Curah Hujan (mm)", round(filtered_df["jumlah_curah_hujan"].sum(), 2))
col3.metric("Rata-rata Bulanan (mm)", round(filtered_df["jumlah_curah_hujan"].mean(), 2))

# -----------------------------
# Grafik Curah Hujan Bulanan
# -----------------------------
st.subheader(f"📈 Grafik Curah Hujan Tahun {selected_year}")

fig, ax = plt.subplots()
ax.plot(filtered_df["bulan"], filtered_df["jumlah_curah_hujan"], marker='o')
ax.set_xlabel("Bulan")
ax.set_ylabel("Curah Hujan (mm)")
ax.set_title(f"Curah Hujan Bulanan Kota Bandung - {selected_year}")
plt.xticks(rotation=45)

st.pyplot(fig)

# -----------------------------
# Tampilkan Data Mentah
# -----------------------------
st.subheader("📄 Data Mentah")
st.dataframe(filtered_df)
