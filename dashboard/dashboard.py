import pandas as pd
import streamlit as st
from datetime import datetime
from menu import question1, question2, question3, question4
from pathlib import Path



csv_file_path1 = Path(__file__).parents[0] / 'olist_customers_dataset.csv'
csv_file_path2 = Path(__file__).parents[0] / 'olist_order_payments_dataset.csv'
# gambar = Path(__file__).parents[0] / 'foto.jpg'

df_customer = pd.read_csv(csv_file_path1)
df_payment = pd.read_csv(csv_file_path2)

with st.sidebar:
    st.subheader('Ferdiyansyah')
    # st.image(gambar)
    today = datetime.today().strftime('%d-%m-%Y')
    st.caption(f'Tanggal hari ini: {today}')
    menu = st.sidebar.selectbox(
        'Pilih Menu:',
        ['Negara Asal Pelanggan', 'Metode Pembayaran Populer', 'Perbandingan Jumlah Transaksi Antara Pembayaran Menggunakan Kartu Kredit Dengan Cicilan Dengan Tanpa Cicilan', 'Perbandingan Antara Metode Pembayaran yang Digunakan Pelanggan Dengan Rentang Nilai Pembayaran']
    )


st.header('Brazilian E-Commerse - Analysis by Ferdiyansyah')


if menu == 'Negara Asal Pelanggan':
    question1(df_customer)
    st.markdown(
        """
        # Kesimpulan
        Berdasarkan hasil analisa, negara bagian SP memiliki jumlah pelanggan tertinggi, sedangkan RR memiliki jumlah pelanggan terendah. Dalam hal ini dapat dilakukan prmosi yang lebih mendalam terhdap negara bagian yang masih dibawah nilai Q1, agar persebaran produk lebih luas dan produk akan lebih dikenal oleh masyarakat
        """
    )
elif menu == 'Metode Pembayaran Populer':
    question2(df_payment)
    st.markdown(
        """
        # Kesimpulan
        Berdasarkan hasil analisa, metode pembayaran yang paling populer adalah dengan menggunakan akrtu kredit. Dari hasil tersebut dapat digunakan untuk strategi marketing untuk membuat promosi yang menguntungkan pengguna kartu kredit dan melakukan mitra dengan penyedia kartu kredit untuk mendapatkan keuntungan yang lebih baik
        """
    )
elif menu == 'Perbandingan Jumlah Transaksi Antara Pembayaran Menggunakan Kartu Kredit Dengan Cicilan Dengan Tanpa Cicilan':
    question3(df_payment, pd)
    st.markdown(
        """
        # Kesimpulan
        Berdasarkan hasil analisa, di dapat sebuah informasi bahwa sebagian besar pengguna yang mengunakan akrtu kredit akan mengangsur pembayarannya. Hal ini dapat digunakan untuk strategi bisnis dengan memberikan beberapa keuntungan atau promosi kepada pengguna yang menggunakan kartu kredit dan mengangsur pembayarannya seperti misalnya diberi bonus tertentu atau meningkatkan branding dalam hal itu
        """
    )
else:
    question4(df_payment, pd)
    st.markdown(
        """
        # Kesimpulan
        Berdasarkan ahsil analisa, persebaran nilai transaksi dengan jumlah taransaksi terlihat cukup merata dari berbagai rentang kelompok transaksi
        """
    )








