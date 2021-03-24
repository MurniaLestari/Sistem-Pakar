# Sistem-Pakar
# Nama : Murnia Lestari
# NPM : 1184006
# Kelas : D4 TI 3C
##% BFS dan DFS
# Persoalan yang akan kita selesaikan dengan metode BFS dan DFS yaitu
# Bagaimanakah Aisya akan menuju ke rumah Raisya dengan rute tercepat. Maka disini kita akan
# mencoba metode BFS dan DFS untuk mengantarkan Aisya menuju rumah Raisya


# Berikut merupakan root node dari rumah Aisya (A) sampai ke rumah Raisya (K).
graf =  {'A':set(['B','C','E']),
         'B':set(['E','D']),
         'C':set(['A','B','D']),
         'D':set(['B','F','K','I']),
         'E':set(['A','B']),
         'F':set(['D','G']),
         'G':set(['H','F','I']),
         'H':set(['G']),
         'I':set(['G','J']),
         'J':set(['I']),
         'K':set(['D','J'])}

##%  BFS
# Maka dengan metode BFS Aisya akan memulai perjalanan menuju rumah Raisya (L) dari root node A ke  note L
# seperti yang kita ketahui apabila menggunakan metode BFS (Breadth First Search) 
# metode ini akan mencarikan solusi atau rute tercepat dengan cara mengecek satu persatu cabang sesuai dengan level pada root node/maps
def bfs(graf, mulai, tujuan):
# mendefinisikan fungsi bfs beserta parameter yaitu graf/node,mulai dan juga tujuan
    queue = [[mulai]]
   # kumpulan antrian  dari graf /peta yang ada untuk memulai mencari rute ke rumah Raisya
    visited = set()
    # Akan mengambil / mengeset data dari peta yang dikunjungi

    while queue:    
        # melakukan perulangan pada antrian paling depan ke variable jalur yang ada pada grap/peta
        jalur = queue.pop(0)
        #memasukkan antrian paling depan ke variabel jalur
        state = jalur[-1]
        #menyimpan graf atau peta yang dipilih ke variabel state,
        if state == tujuan:
            # melakukan pengecekan apakah sama dengan tujuan,jika Ya maka akan mengembalikan pada jalur
            return jalur
        elif state not in visited:
            # jika tidak ada pada state maka
            for cabang in graf.get(state, []): 
                #lakukan perulangan pada cabang di graf dan pengecekan semua cabang pada state
                jalur_baru = list(jalur) 
		#memasukkan isi dari variabel jalur ke variabel jalur ke variabel jalur_baru
                jalur_baru.append(cabang)  
		# mengupdate/menmabah isi jalur_baru dengan cabang
                queue.append(jalur_baru) 
		# mengupdate/menambah queue dengan jalur baru

            visited.add(state)
#menandai state yang sudah dikunjugi
# mengecek isi queue
        isi = len(queue)
        if isi == 0:
            print("Tidak ditemukan")
# maka ketika dijalankan kode program ini rute tercepat dengan metode BFS dari rumah Aisya untuk sampai ke rumah Aisya yaitu A,B,D,K


#%% DFS
# Masih sama dengan  metode BFS maka DFS pun juga  akan mencari atau menemukan solusi untuk  Aisya yang akan menuju  rumah Raisya 
# dimulai dari  root node A untuk menuju rumah Aisya  yaitu node terakhir yaitu L
# seperti yang kita ketahui apabila menggunakan metode DFS (Depth First Search) 
# maka dalam metode ini akan dicarikan solusi atau rute tercepat dengan cara mengecek satu persatu dengan menurun ke bawah
# untuk memeriksa terlebih dahulu semua anak atau turunan dari cabang sebelum beralih ke cabang lain.
def dfs(graf, mulai,tujuan):
    # mendefinisikan fungsi dfs beserta parameter yaitu graf/node,mulai dan juga tujuan
    stack = [[mulai]]
# tumpukan antrian  dari graf /peta yang ada untuk memulai mencari rute ke rumah Raisya
    visited = set()
 # Akan mengambil / mengeset data dari peta yang dikunjungi

    while stack: 
         # melakukan perulangan pada tumpukan paling depan ke variable jalur yang ada pada grap/node
        jalur = stack.pop(-1)
          #memasukkan tumpukan antrian paling depan ke variabel jalur
        state = jalur[-1]
         #menyimpan graf atau node yang dipilih ke variabel state,
        if state == tujuan:
            # melakukan pengecekan apakah sama dengan tujuan,jika Ya maka akan mengembalikan pada jalur
            return jalur
        elif state not in visited:
              # jika tidak ada pada state maka
            for cabang in graf.get(state, []): 
                 #lakukan perulangan pada cabang di graf dan pengecekan semua cabang pada state
                jalur_baru = list(jalur) 
                 #memasukkan isi dari variabel jalur ke variabel jalur ke variabel jalur_baru
                jalur_baru.append(cabang) 
engupdate/menambah isi dengan jalur baru dengan cabang
                stack.append(jalur_baru) 
# mengupdate/menambah stack dengan jalur baru

            visited.add(state)
#menandai state yang sudah dikunjugi
# mengecek isi stack
        isi = len(stack)
        if isi == 0:
            print("Tidak ditemukan")
# maka ketika dijalankan kode program ini akan menunjukan rute tercepat dengan metode DFS dari rumah Aisya untuk sampai ke rumah Raisya yaitu A,B,D,F,G,J,K
