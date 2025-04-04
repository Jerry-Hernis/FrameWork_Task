from flask import Flask, render_template

app = Flask(__name__)

app_sesuatu = "Website Pada Pukul Satu Siang & Juga Kelaparan (Variabel Global)"

# 1. App Route Hello World
@app.route("/")
def halo_cantik():
    return "<p>Hello Jerry!</p>"

# 2. App Route Aplikasi Ke Halaman Yang Lebih Spesifik
@app.route('/tambahan/')
def tambahan():
    return "<p>Hello Jerry, ini adalah halaman Baru !</p>"

# 3. App Route Ke Halaman HTML Yang Keren (Menggunakan Fungsi yang In line/ Mendesain Web secara langsung didalam HTML)
@app.route("/bisayuk/")
def bisayuk():
    return render_template('bisayuk.html')

# 4. App Route Ke Halaman Yang Tambah Keren (Menggunakan Fungsi yang dapat terhubung ke CSS/Mendesain Web secara Terpisah)
@app.route("/bisayuk/tambahkren/")
def tambahkren():
    return render_template('tambahkren.html')

# 5. App Route Dinamis (Kita dapat memasukkan string kedalam URL yang juga akan muncul didalam Website)
@app.route('/bisayuk/<string:nama>')
def apamau_mu(nama):
    return "Hai, Terimakasih Telah Mengakses Web Kami, Biar Ku Tebak Anda Adalah {}".format(nama)

# 6. App Route Variabel Global 
@app.route('/globalnih/')
def global_globe ():
    return f'Saya Mengerjakan {app_sesuatu}'

# 7. App Route Variabel Lokal
@app.route('/lokalnih/')
def loklok():
    data = {"name": "Jinwo", "age": 25, "city": "Korea"}
    return render_template('loklok.html', data=data)

# 8. App Route Menampilkan List Nama dalam HTML
@app.route('/huft')
def orang():
    list_orang = ["Jinwo", "Chae", "ByungGu", "Antares"]
    return render_template('orang.html', orang=list_orang)

# 9. App Route Menampilkan Pesan jika Tidak ada data
@app.route('/huft2')
def orang2():
    list_orang = ["Jinwo", "Chae", "ByungGu", "Antares"]
    return render_template('orang2.html', orang=list_orang)

#10. AR. Menandai Admin dalam Daftar User
@app.route('/huft3')
def miming():
    mimin_list = [
        {"name": "Jinwo", "role": "admin"},
        {"name": "Chae", "role": "user"},
        {"name": "Antares", "role": "admin"},
        {"name": "ByungGu", "role": "user"},
    ]
    return render_template('mimin.html', miming=mimin_list)

# 11. AR. Menampilkan Nomor Urut
@app.route('/huft4')
def orang3():
    list_orang = ["Jinwo", "Chae", "ByungGu", "Antares"]
    return render_template('orang3.html', orang3=list_orang)

# 12. AR. Menampilkan Pesan Berdasarkan Skor
@app.route('/huft5/<int:score>')
def skoruts(score):
    return render_template('scoruts.html', score=score)

# 13. AR Menampilkan Status 
@app.route('/huft6')
def mahas3wa():
    demo_ikut2an = [
        {"nama": "Mina", "nilai": 92},
        {"nama": "Antum", "nilai": 80},
        {"nama": "Imah", "nilai": 65},
        {"nama": "Pati", "nilai": 55},
    ]
    return render_template('mahas3wa.html', mahas3wa=demo_ikut2an)

if __name__ == "__main__":
    app.run(debug=True)
