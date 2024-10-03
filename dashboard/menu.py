import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
sns.set(style='dark')
def question1(df):
    # Pertanyaan 1: Dari negara mana saja pelanggan berasal ?
    st.subheader('Negara Asal Pelanggan')
    state_df = df.groupby(by="customer_state").customer_id.nunique().reset_index()
    state_df.rename(columns={
        "customer_id": "customer_count"
    }, inplace=True)    
    state_df
    fig = plt.figure(figsize=(10, 10))
    sns.barplot(
        x="customer_count", 
        y="customer_state",
        data=state_df.sort_values(by="customer_count", ascending=False),
    )
    plt.title("Number of Customer by States", loc="center", fontsize=15)
    plt.ylabel(None)
    plt.xlabel(None)
    plt.tick_params(axis='y', labelsize=12)
    plt.show()
    st.pyplot(fig)


    fig = plt.figure(figsize=(10, 10))
    plt.pie(state_df['customer_count'], labels=state_df['customer_state'], autopct='%1.1f%%', startangle=90)
    plt.title("Percentage of Customers by States")
    plt.axis('equal') 
    plt.show()
    st.pyplot(fig)



def question2(df):
    # Pertanyaan 2: Apa metode pembayaran yang paling populer digunakan pelanggan ?
    st.subheader('Metode Pembayaran Populer')
    pt = df.groupby(['payment_type']).size().sort_values(ascending=False).reset_index(name='count')
    fig = plt.figure(figsize=(10, 6))
    sns.barplot(
        x='payment_type', 
        y='count', 
        data=pt
    )

    plt.title("Payment Type Distribution", fontsize=15)
    plt.xlabel("Payment Type")
    plt.ylabel("Count of Payments")

    plt.xticks(rotation=30, ha="right") 
    plt.tight_layout()
    plt.show()
    st.pyplot(fig)


    fig = plt.figure(figsize=(10, 6))
    sns.countplot(
        y='payment_type', 
        data=df, 
        order=df['payment_type'].value_counts().index
    )

    plt.title("Payment Type Distribution", fontsize=15)
    plt.xlabel("Count of Payments")
    plt.ylabel("Payment Type")
    plt.show()
    st.pyplot(fig)

def question3(df, pd):
    # Pertanyaan 3: Bagaimana perbandingan jumlah transaksi antara pembayaran menggunakan kartu kredit dengan cicilan (> 1) dengan tanpa cicilan (==1)?
    st.subheader('Perbandingan Jumlah Transaksi Antara Pembayaran Menggunakan Kartu Kredit Dengan Cicilan Dengan Tanpa Cicilan')


    count_with_installments = df[(df['payment_type'] == 'credit_card') & (df['payment_installments'] > 1)].shape[0]
    count_without_installments = df[(df['payment_type'] == 'credit_card') & (df['payment_installments'] == 1)].shape[0]
    data = {'Payment Installments': ['More than 1', 'Equal to 1'],
        'Transaction Count': [count_with_installments, count_without_installments]}
    df_count = pd.DataFrame(data)

    # Visualisasi bar plot
    fig = plt.figure(figsize=(10, 15))
    sns.barplot(x='Payment Installments', y='Transaction Count', data=df_count)
    plt.title("Perbandingan Jumlah Transaksi Kartu Kredit: Cicilan > 1 vs Cicilan = 1")
    plt.xlabel("Payment Installments")
    plt.ylabel("Transaction Count")
    plt.show()
    st.pyplot(fig)

def question4(df, pd):
    # Bagaimana perbandingan antara metode pembayaran yang digunakan pelanggan dengan rentang nilai pembayaran yang mereka keluarkan?
    st.subheader('Perbandingan Antara Metode Pembayaran yang Digunakan Pelanggan Dengan Rentang Nilai Pembayaran')


    q1_pv = df['payment_value'].quantile(0.25)
    q2_pv = df['payment_value'].quantile(0.50)
    q3_pv = df['payment_value'].quantile(0.75)
    bins = [0, q1_pv, q2_pv, q3_pv, np.inf]
    labels = ['Low (0 - {})'.format(q1_pv), 'Medium ({} - {})'.format(q1_pv, q2_pv), 'High ({} - {})'.format(q2_pv, q3_pv), 'Very High ({}+)'.format(q3_pv)]
    df['payment_value_bin'] = pd.cut(df['payment_value'], bins=bins, labels=labels)
    distribution_per_bin = df.groupby(['payment_value_bin', 'payment_type']).size().unstack().fillna(0)
    distribution_per_bin['Total'] = distribution_per_bin.sum(axis=1)

    fig = plt.figure(figsize=(10,6))
    sns.barplot(x=distribution_per_bin.index, y=distribution_per_bin.sum(axis=1))
    plt.title('Distribusi Metode Pembayaran Berdasarkan Nilai Transaksi')
    plt.xlabel('Kelompok Nilai Transaksi')
    plt.ylabel('Jumlah Transaksi')
    plt.show()
    st.pyplot(fig)