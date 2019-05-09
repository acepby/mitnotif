from  praytimes import PrayTimes
from datetime import date,datetime,time,timedelta
import time as t
import notify2

ICON_PATH ="/home/acep/Oprek/python/mitprayertime/mit.png"
notify2.init("MITPrayer")
app = notify2.Notification(None,icon=ICON_PATH)
app.set_urgency(notify2.URGENCY_NORMAL)
app.set_timeout(10000)
prayTimes = PrayTimes()

def update():
	tgl =datetime.now()
	waktu = tgl.replace(second=0,microsecond=0)
	waktu = waktu.time()
	times = prayTimes.getTimes(date.today(), (-7.7500127,110.3606701), +7)
	imsakiyah=['Imsak','Fajr', 'Sunrise', 'Dhuhr', 'Asr', 'Maghrib', 'Isha'] 
	for i in imsakiyah: #['Imsak','Fajr', 'Sunrise', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
		if( datetime.strptime(times[i.lower()],'%H:%M').time()==waktu):
			app.update('Sudah masuk waktu '+ i,'Ayo Berangkat') 
			app.show()
			print('sudah '+ i+':'+ times[i.lower()])
		if(waktu < datetime.strptime(times[i.lower()],'%H:%M').time()):
			mynext =datetime.strptime(times[i.lower()],'%H:%M').time()
			mynext = datetime.combine(date.today(),mynext)
			mywaktu = datetime.combine(date.today(),waktu)
			durasi = mynext - mywaktu
			if(durasi.total_seconds() == 600):
				app.update('Ngasi Tau aja','bentar lagi '+i)
				app.show()
				print('bentar lagi '+i) 
			break
if __name__ == "__main__":
	print("MITPrayerTimes - Alarm Imsakiyah")
	while True:
		update()
		t.sleep(60)
