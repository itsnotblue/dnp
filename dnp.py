import streamlit as st

data = [
    {'Nama': 'es cekek', 'Harga': 3000, 'Jenis': 'Minuman', 'Tetangga1': 'roti bakar', 'Tetangga2': 'cireng'},
    {'Nama': 'cireng', 'Harga': 5000, 'Jenis': 'Makanan', 'Tetangga1': 'es cekek', 'Tetangga2': 'kentang'},
    {'Nama': 'es teh', 'Harga': 5000, 'Jenis': 'Minuman', 'Tetangga1': 'dimsum', 'Tetangga2': 'batagor'},
    {'Nama': 'roti bakar', 'Harga': 6000, 'Jenis': 'Makanan', 'Tetangga1': 'dimsum', 'Tetangga2': 'es cekek'},
    {'Nama': 'kentang', 'Harga': 8000, 'Jenis': 'Makanan', 'Tetangga1': 'es cekek', 'Tetangga2': 'cireng'},
    {'Nama': 'batagor', 'Harga': 10000, 'Jenis': 'Makanan', 'Tetangga1': 'es teh', 'Tetangga2': 'es cekek'},
    {'Nama': 'dimsum', 'Harga': 12000, 'Jenis': 'Makanan', 'Tetangga1': 'es teh', 'Tetangga2': 'roti bakar'},
]


def knapsack_dp(data, w):
    n = len(data)
    dp = [[0 for j in range(w + 1)] for i in range(n + 1)]

    # Initialize first row
    for j in range(w + 1):
        if data[0]['Harga'] <= j:
            dp[0][j] = data[0]['Harga']

    # Fill the DP table
    for i in range(1, n):
        for j in range(w + 1):
            if data[i]['Harga'] <= j:
                dp[i][j] = max(dp[i - 1][j], data[i]['Harga'] + dp[i - 1][j - data[i]['Harga']])
            else:
                dp[i][j] = dp[i - 1][j]

    # Traceback to find the items in the knapsack
    x = []
    total_harga = dp[n - 1][w]
    i = n - 1
    j = w

    while i >= 0 and j >= 0:
        if dp[i - 1][j] == dp[i][j]:
            i -= 1
        else:
            x.append(data[i])
            j -= data[i]['Harga']
            i -= 1

    x.reverse()
    return x, total_harga


st.title("Mencari Takjil Greedy vs Brute Force")

edited_df = st.data_editor(data, num_rows="dynamic")

w = st.number_input("Tentukan Batas Harga!", placeholder="nilai awal ialah 25000", value=25000)
nama_options = [item['Nama'] for item in edited_df]
n = st.selectbox("Tentukan 1 Item Yang Wajib Dibeli!", nama_options)

hasil, total = knapsack_dp(edited_df, w)
st.write('ini hasil :', hasil)
st.write('total harga :', total)
