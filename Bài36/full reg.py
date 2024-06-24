info = info_acc(geo='vn', type_email = [""])
# simcode = TowNdLine("6865cd8dcddaa5b5a003ea7145cbe031","373")
# simcode = Api_hcotp_com("VWNpQjEySTcxSEpwbHBEY29UcCtJTWVEWEFBRGhWcCtGcGRoVzlGZUExQT0","26")
# simcode = Api_mmotp_com("mZT38UYlE4h40s7JtafJltMrSxlKCwe4iISy","663dcacc597f8bd5f212c610")
simcode = Api_sim24_cc("8n2nuq8dolh69t5f9cshvxlgp5ntvy8v","Payoneer")


def get_mail_po(type_get = "link", index = 0, search = "Mã xác minh của bạn từ Payoneer", email = "", passwd = ""):
	if type_get != "code":
		type_get = "link"
	# URL của API
	url = f"http://127.0.0.1:10002/{type_get}"

	# Tham số truy vấn
	params = {
		"count": 10,
		"index": index,
		"search": search,
		"username": email,
		"password": passwd
	}

	response = requests.get(url, params=params)
	json_data = response.json()
	if json_data["stt"]:
		return json_data["data"]
	else:
		return False
		




def tool_atfc_pro(phone):
	url = "https://tool.atfc.pro/api-internal/api/v1/helper/sms/get-otp2"
	params = {
		"phoneNumber": f"84{phone}",
		"munite": 5,
		"appBrand": "Payoneer"
	}

	# Make the GET request
	response = requests.get(url, params=params)

	# Check if the request was successful
	if response.status_code == 200:
		# Parse the JSON response
		data = response.json()
		if data.get("statusCode") == 200:
			if len(data.get("data")) > 4:
				return data.get("data")
			else:
				return False
		else:
			return False
	else:
		return False





class GOGL:
	def __init__(self):
		self.telegram_bot_token = "6062669164:AAHsr9hmjkpr4qLvFIuW0wO0K5IflbIA2kw"
		self.telegram_chat_id = "-4230582430"
		
		
		self.folderBackupCloud = "Payonner"
		
		# --------DB 100k Sim Reg--------#
		self.Sim_Reg = "pov8@gmail.com/Payoneer-V2/Data/100K-Sim"
        self.API_Sim_Reg = Api_database(token, self.Sim_Reg, "")
		
		# --------DB Acc Reg Thành Công--------#
		self.Acc_Reg_Thanh_Cong = "pov8@gmail.com/Payoneer-V2/Acc-Thanh-Cong"
		self.API_Acc_Reg_Thanh_Cong = Api_database(token, self.Acc_Reg_Thanh_Cong, "")
		
		# --------DB Bank--------#
		self.Bank_Reg = "pov8@gmail.com/Payoneer-V2/Data/Bank/Bank-Hai"
		# self.Bank_Reg = "pov8@gmail.com/Payoneer-V2/Data/Bank/Bank-Tuan"
		# self.Bank_Reg = "pov8@gmail.com/Payoneer-V2/Data/Bank/Bank-Y"
		
                        # --------API--------#
		self.API_Bank_Reg = Api_database(token, self.Bank_Reg, "")
		
		
		# --------DB Proxy Reg--------#
		self.Proxy_Reg = "pov8@gmail.com/Payoneer-V2/Data/Proxy/US-GB-CA-MX-DE-IT"
# 		self.Proxy_Reg = "pov8@gmail.com/Payoneer-V2/Data/Proxy/US-GB-CA"
# 		self.Proxy_Reg = "pov8@gmail.com/Payoneer-V2/Data/Proxy/US"

                        # --------API--------#
        self.API_Proxy_Reg = Api_database(token, self.Proxy_Reg, "")
		
		# --------DB Mail Reg--------#
		self.Mail_Reg = "pov8@gmail.com/Payoneer-V2/Mail-Reg-DV"
		self.Mail_Reg_Pending = "pov8@gmail.com/Payoneer-V2/Pending-Mail-Reg"
		self.Mail_Reg_Lap = "pov8@gmail.com/Payoneer-V2/Mail-Lap"
		
                        # --------API--------#
		self.API_Mail = Api_database(token, self.Mail_Reg, "")
		self.API_Mail_Reg_Pending = Api_database(token, self.Mail_Reg_Pending, "")
		self.API_Mail_Reg_Lap = Api_database(token, self.Mail_Reg_Lap, "")
		
		# --------DB Xác Nhận Link--------#
		self.Db_Xac_Nhan_Link_Thanh_Cong = "pov8@gmail.com/Payoneer-V2/DB-Xac-Nhan-Link/Xac-Nhan-Thanh-Cong"
# 		self.Db_Xac_Nhan_Link_Thanh_Cong = "pov8@gmail.com/Payoneer-V2/DB-Xac-Nhan-Link/Xac-Nhan-Thanh-Cong-2"

                        # --------API--------#
		self.API_Db_Xac_Nhan_Link_Thanh_Cong = Api_database(token, self.Db_Xac_Nhan_Link_Thanh_Cong, "")
	


		# --------DB Ver Code Mail--------#
		self.Db_One_Or_More_Details_Is_Incorrect = "pov8@gmail.com/Payoneer-V2/DB-Ver-Code-Mail/Acc-Bi-One-Or-More-Details-Is-Incorrect"
		self.Db_Mail_Chua_Dang_Ky_Thanh_Cong = "pov8@gmail.com/Payoneer-V2/DB-Ver-Code-Mail/Mail-Chua-Dang-Ky-Thang-Cong"
		self.Db_Tai_Khoan_Ver_Code_Bi_Khoa = "pov8@gmail.com/Payoneer-V2/DB-Ver-Code-Mail/Tai-Khoan-Ver-Code-Bi-Khoa"
		self.Db_Mail_Ver_Khong_Co_Code = "pov8@gmail.com/Payoneer-V2/DB-Ver-Code-Mail/Mail-Ver-Khong-Co-Code"
		self.Db_Acc_Ver_Khonggggg_Co_Tick_Xanh = "pov8@gmail.com/Payoneer-V2/DB-Ver-Code-Mail/Acc-Ver-Khonggggg-Co-Tick-Xanh"
		self.Db_Acc_Ver_Done_Co_Tick_Xanh = "pov8@gmail.com/Payoneer-V2/DB-Ver-Code-Mail/Acc-Ver-Done-Co-Tick-Xanh"
		
                        # --------API--------#
        self.API_Db_One_Or_More_Details_Is_Incorrect = Api_database(token, self.Db_One_Or_More_Details_Is_Incorrect, "")
		self.API_Db_Mail_Chua_Dang_Ky_Thanh_Cong = Api_database(token, self.Db_Mail_Chua_Dang_Ky_Thanh_Cong, "")
		self.API_Db_Tai_Khoan_Ver_Code_Bi_Khoa = Api_database(token, self.Db_Tai_Khoan_Ver_Code_Bi_Khoa, "")
        self.API_Db_Mail_Ver_Khong_Co_Code = Api_database(token, self.Db_Mail_Ver_Khong_Co_Code, "")
		self.API_Db_Acc_Ver_Khonggggg_Co_Tick_Xanh = Api_database(token, self.Db_Acc_Ver_Khonggggg_Co_Tick_Xanh, "")
		self.API_Db_Acc_Ver_Done_Co_Tick_Xanh = Api_database(token, self.Db_Acc_Ver_Done_Co_Tick_Xanh, "")

		
		
		
		
		
		
		# hàm get địa chỉ
# 		self.InputAddress = Api_database(token, self.pathFile_InputAddress, "").findOne(wheres = {}, key_search = "text_full", search = "", delete = True, hide = True, reset_hide = True).datas["text_full"]
# 		if self.InputAddress == None or len(self.InputAddress) < 5:
# 			printe("Hết địa chỉ.")
# 			main.exit()
		self.dia_chis = [
			"Pho Hang Dao",
			"Pho Hang Dau",
			"Pho Hang Dieu",
			"Pho Hang Dong",
			"Pho Hang Duong",
			"Pho Hang Ga"
		]
		self.dia_chi_full = str(random.randint(1,9999))+" "+unidecode(info.first_name)+" "+unidecode(info.middle_name)
		self.dia_chi = random.choice(self.dia_chis)
		
		# hàm get thành phố
		self.InputCitys = Api_database(token, "pov8@gmail.com/Payoneer-V2/Data/City", "").findOne(wheres = {}, key_search = "text_full", search = "", delete = False, hide = True, reset_hide = True).datas
		if len(self.InputCitys) == 0:
			printe("Hết thành phố.")
			main.exit()
		# hàm get zipcode
		self.InputZipcodes = Api_database(token, "pov8@gmail.com/Payoneer-V2/Data/Zipcode", "").findOne(wheres = {}, key_search = "text_full", search = "", delete = False, hide = True, reset_hide = True).datas
		if len(self.InputZipcodes) == 0:
			printe("Hết zipcode.")
			main.exit()
		
		# hàm get proxy
		self.proxys = Api_database(token, self.Proxy_Reg, "").findOne(wheres = {}, key_search = "text_full", search = "", delete = False, hide = True, reset_hide = True).datas
		if len(self.proxys) == 0:
			printe("Hết proxy reg account rồi nhé bro :))")
			main.exit()
		
		
		self.firstname = unidecode(info.first_name)
		self.middlename = unidecode(info.middle_name)
		self.lastname = unidecode(info.last_name)
		self.password = info.password +str(random.randint(1,99))
		self.sn_month = random.choice(["Tháng 1","Tháng 2","Tháng 3","Tháng 4","Tháng 5","Tháng 6","Tháng 7","Tháng 8","Tháng 9","Tháng 10","Tháng 11","Tháng 12"])
		self.sn_day = str(random.randint(1,26))
		self.sn_year = str(random.randint(1990,1995))
		
		
		self.full_acc = ""
		self.email_kp = ""
		self.phone = ""
		
		
		self.bank = ""
		self.banks = ""
		self.bank_name = ""
		self.bank_number = ""
		self.bank_swift = ""
		self.bank_ho_va_ten = ""
		self.mails = None
		self.mail_user = None
		self.mail_pass = None
		self.text_acc = ""
		self.cmnd = str(random.randint(100,999))+str(random.randint(100,999))+str(random.randint(100,999))
		self.cau_hoi_bao_mat_reg_value = str(random.randint(100000,700000))
		
		
		
		self.Browser = Sofin_browser(main=main, folder_backup = self.folderBackupCloud)
		# Hàm khởi tạo profile mới
		if self.Browser.create() == False:
			printe("Không tạo được profile")
			main.exit()
		self.proxy = self.proxys["text_full"]
		if self.Browser.proxy(self.proxys["text_full"]) == False:
			printe("KHÔNG KẾT NỐI ĐƯỢC PROXY")
			main.exit()
			
		# hàm mở trình duyệt
		self.flags = [
			"--blink-settings=imagesEnabled=false", "--incognito","--enable-quic", "--enable-features=ParallelDownloading", "--disable-background-networking", "--enable-http2","--enable-brotli","--enable-experimental-canvas-features","--enable-fast-unload","--enable-lazy-image-loading","--enable-lazy-frame-loading","--enable-smooth-scrolling","--enable-simple-cache-backend","--enable-tcp-fast-open"
		]
		if self.Browser.open(flags = self.flags, win_scale = scale, win_pos = position) == False:
			printe("Không mở được trình duyệt.")
			main.exit()
		# connect playwright
		self.driver = Soplaywright(self.Browser)
		self.main_tool()
	
	
	
	
	
	
	def bot_telegrams(self, id_chat = "-4230582430", text = ""):
		try:
			bot_token = self.bot_token
			chat_id = id_chat
			message = 'xxxxxxxxx'
			url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
			params = {
				"chat_id": chat_id,
				"text": text
			}
			response = requests.post(url, params=params)
		except:
			pass
			
	
	
	def get_phone_db(self):

		TDev.get(dbToken = self.Sim_Reg)
		self.phone = TDev.text
		if self.phone == None:
			 printe("Hết Sđt")
			 main.exit()		
			
	
	def main_tool(self):
		self.driver.Goto("https://payouts.payoneer.com/partners/or.aspx?pid=YOYIZC74IO2s4KZQp7tgsw%3D%3D&BusinessLine=7&Volume=below-2000&web_interaction=webpage_accounts&from=login&langid=21&locale=vi&_gl=1*rryavz*_ga*NjA4OTQ0OTMxLjE3MTc0MjAzODA.*_ga_G4G3RX5S55*MTcxNzQyMDM3OS4xLjEuMTcxNzQyMDM5NC4wLjAuMzI5OTM4NTM4")
# 		self.driver.Goto("https://payouts.payoneer.com/partners/or.aspx?pid=YOYIZC74IO2s4KZQp7tgsw%3d%3d&BusinessLine=7&Volume=below-2000&web_interaction=webpage_accounts|website_traffic&langid=21&locale=vi")
		###### nhạp info
		if self.driver.Set_xpath("//input[contains(@name,'txtFirstName')]", 20).isElement:
			isAction = False
			for _ in range(5):
				if self.driver.Get_xpath(0).Click().is_click:
					self.driver.Press(self.middlename+" "+self.firstname)
				# 	self.driver.Press(self.firstname)
					isAction =  True
					break
		else:
			isAction =  False
		if isAction == False:
			printe("Click `Tên` thất bại")
			main.exit()
		
		
		
		if self.driver.Set_xpath("//input[@id='txtLastName']", 20).isElement:
			isAction = False
			for _ in range(5):
				if self.driver.Get_xpath(0).Click().is_click:
					self.driver.Press(self.lastname)
					isAction =  True
					break
		else:
			isAction =  False
		if isAction == False:
			printe("Click `Họ` thất bại")
			main.exit()
		
		
		
		
		# hàm get mail
		
		self.InputMails = self.API_Mail.findOne(wheres = {}, key_search = "text_full", search = "", delete = True, hide = True, reset_hide = True).datas
		if len(self.InputMails) == 0:
			self.InputMails = self.API_Mail.findOne(wheres = {}, key_search = "text_full", search = "", delete = True, hide = True, reset_hide = True).datas
			if len(self.InputMails) == 0:
				printe("Hết mail")
				main.exit()
		self.mail = self.InputMails["text_full"]
		self.mails = self.InputMails["text_full"].split("|")
		self.mail_user = self.mails[0]
		self.mail_pass = self.mails[1]
		# lưu vào db pending
		self.Mail_Reg_Pending.create_database(self.InputMails["text_full"], live = 0)
		
		
		
		if self.driver.Set_xpath("//input[@id='txtEmail']", 20).isElement:
			isAction = False
			for _ in range(5):
				if self.driver.Get_xpath(0).Click().is_click:
					self.driver.Press(self.mail_user)
					isAction =  True
					break
		else:
			isAction =  False
		if isAction == False:
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			printe("Click `Email` thất bại")
			main.exit()
			
			
			
		if self.driver.Set_xpath("//input[@id='txtRetypeEmail']", 20).isElement:
			isAction = False
			for _ in range(5):
				if self.driver.Get_xpath(0).Click().is_click:
					self.driver.Press(self.mail_user).Sleep(0.5).TAB().Sleep(0.5)
					isAction =  True
					break
		else:
			isAction =  False
		if isAction == False:
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			printe("Click `Nhập lại email` thất bại")
			main.exit()
		
		
		

		if self.driver.Set_xpath("//select[@data-handler='selectYear']", 20).isElement:
			self.driver.Get_xpath(0).Selected(self.sn_year).Sleep(1)
			isAction =  True
		else:
			isAction =  False
		if isAction == False:
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			printe("Nhập `Năm sinh` thất bại")
			main.exit()
		

		if self.driver.Set_xpath("//select[@data-handler='selectMonth']", 20).isElement:
			self.driver.Get_xpath(0).Selected(self.sn_month).Sleep(1)
			isAction =  True
		else:
			isAction =  False
		if isAction == False:
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			printe("Nhập `Tháng sinh` thất bại")
			main.exit()
		





		if self.driver.Set_xpath(f"//tr/td/a[contains(.,'{self.sn_day}')]", 20).isElement:
			isAction = False
			for _ in range(5):
				if self.driver.Get_xpath(0).Click().is_click:
					isAction =  True
					break
		else:
			isAction =  False
		if isAction == False:
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			printe("Click `Ngày sinh` thất bại")
			main.exit()

		time.sleep(5)

		if self.driver.Set_xpath(f"//input[@id='txtRetypeEmail']", 20).isElement:
			isAction = False
			for _ in range(5):
				if self.driver.Get_xpath(0).Click().is_click:
					self.driver.ENTER()
					isAction =  True
					break
		else:
			isAction =  False
		if isAction == False:
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			printe("Click `Tiếp Tục` thất bại")
			main.exit()	
			
		
	

		
		
		
		if self.driver.Set_xpath("(//div[contains(.,'Chúng tôi chỉ cho phép một tài khoản mỗi người. Vui lòng liên hệ với chúng tôi để được trợ giúp với tài khoản hiện có của bạn.')])[14]", 10).isElement:
			printe("Mail Lặppppp Lạiiiiiiiii!!!!!!")
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail_Reg_Lap.create_database(self.mail, live = 0)
			
			main.exit()
		else:
			printx("Mail Mới Hihihihihihihihi Timmmmmmmmmmmmmmmmm")
		
		

		printx("XONG BƯỚC 1")
		time.sleep(10)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		if self.driver.Set_xpath("//select[@id='ddlResidencyCountries']", 20).isElement:
			isAction = False
			for _ in range(5):
				if self.driver.Get_xpath(0).Click().is_click:
					self.driver.Sleep(1).Press("Vie").Sleep(1).ENTER().Sleep(5)
					isAction =  True
					break
		else:
			isAction =  False
		if isAction == False:
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			printe("Click `Quốc gia` thất bại")
			main.exit()

		
		
		if self.driver.Set_xpath("//input[@id='inputAddress']", 20).isElement:
			isAction = False
			for _ in range(3):
				if self.driver.Get_xpath(0).Click().is_click:
					self.driver.Press(self.dia_chi)
					isAction =  True
					break
		else:
			isAction =  False
		if isAction == False:
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			printe("Click `Địa chỉ1` thất bại")
			main.exit()
		
		
		
		
		time.sleep(2)
		if self.driver.Set_xpath("//div[contains(@class,'OtherAddressOption')]", 20).isElement:
			self.driver.Get_xpath(0).Click()
		else:
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			printe("Click `OtherAddressOption` thất bại")
			main.exit()
		
		
		
		
		time.sleep(1)
		if self.driver.Set_xpath("//input[@id='txtAddress1']", 20).isElement:
			isAction = False
			for _ in range(3):
				if self.driver.Get_xpath(0).Click().is_click:
					for _ in range(30):
						self.driver.RIGHT()
						time.sleep(0.1)
					for _ in range(30):
						self.driver.BACKSPACE()
						time.sleep(0.1)
					self.driver.Press(self.dia_chi_full)
					isAction =  True
					break
		else:
			isAction =  False
		if isAction == False:
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			printe("Click `Địa chỉ2` thất bại")
			main.exit()
		
		
		
		
		
		
		time.sleep(2)
		
		if self.driver.Set_xpath("//input[@id='txtCity']", 20).isElement:
			isAction = False
			for _ in range(5):
				if self.driver.Get_xpath(0).Click().is_click:
					self.thanh_pho = self.InputCitys["text_full"]
					self.driver.Press(self.thanh_pho)
					isAction =  True
					break
		else:
			isAction =  False
		if isAction == False:
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			printe("Click `Thành Phố` thất bại")
			main.exit()
		
		
		
		if self.driver.Set_xpath("//input[@id='txtZip']", 20).isElement:
			isAction = False
			for _ in range(5):
				if self.driver.Get_xpath(0).Click().is_click:
					self.zipcode = self.InputZipcodes["text_full"]
					self.driver.Press(self.zipcode)
					isAction =  True
					break
		else:
			isAction =  False
		if isAction == False:
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			printe("Click `zipcode` thất bại")
			main.exit()
			
		time.sleep(3)




		if self.driver.Set_xpath("//input[@id='AccountPhoneNumber_num']", 20).isElement:
			isAction = False
			for _ in range(5):
				if self.driver.Get_xpath(0).Click().is_click:
					self.get_phone_db()
					if self.phone != False:
						for _ in range(15):
							self.driver.RIGHT()
							time.sleep(0.1)
						for _ in range(15):
							self.driver.BACKSPACE()
							time.sleep(0.1)
						self.driver.Press(self.phone)
						isAction =  True
						break
		else:
			isAction =  False
		if self.phone == False:
			printe("Hết số điện thoại từ API.")
		if isAction == False:
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			printe("Click `Phone` thất bại")
			main.exit()
		
		

		
				
				
				
				
		###############################################
		############-PHONE------#######################
		###############################################
		###############################################
		if self.driver.Set_xpath("//a[contains(.,'Gửi mã')]", 20).isElement:
			isAction = False
			for _ in range(5):
				if self.driver.Get_xpath(0).Click().is_click:
					isAction =  True
					break
		else:
			isAction =  False
		if isAction == False:
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			printe("Click `Gửi code` thất bại")
			main.exit()
		

		code = False
		for _ in range(30):
			time.sleep(5)
			code = tool_atfc_pro(self.phone)
			if code != False:
				break
		if code == False:
			printe("Không lấy được code sđt")
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			main.exit()
		code = str(code)
		printx("code SĐT: " +code)
		if self.driver.Set_xpath("//input[@id='txtVerificationCode']", 20).isElement:
			isAction = False
			for _ in range(5):
				if self.driver.Get_xpath(0).Click().is_click:
					self.driver.Press(code)
					isAction =  True
					break
		else:
			isAction =  False
		if isAction == False:
			TDev.delete()
			TDev.set(dbToken = self.mail_reg, value = self.mail)
			printe("Click `Nhập code` thất bại")
			main.exit()
		###############################################
		############-PHONE------#######################
		###############################################
		###############################################
		
		if self.driver.Set_xpath("//input[@id='ContactDetailsButton']", 20).isElement:
			isAction = False
			for _ in range(5):
				if self.driver.Get_xpath(0).Click().is_click:
					isAction =  True
					break
		else:
			isAction =  False
		if isAction == False:
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			printe("Click `Tiếp tục` thất bại")
			main.exit()
			
		
		
		printx("XONG BƯỚC 2")
		time.sleep(20)
		
		
		
		
		
		
		
		
		
		
		
		
		
		# page 3 
		if self.driver.Set_xpath("//input[@id='tbPassword']", 20).isElement:
			isAction = False
			for _ in range(5):
				if self.driver.Get_xpath(0).Click().is_click:
					self.driver.Press(self.password)
					isAction =  True
					break
		else:
			isAction =  False
		if isAction == False:
			TDev.deleteId()
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			main.exit()
			
			
		if self.driver.Set_xpath("//input[@id='tbRetypePassword']", 20).isElement:
			isAction = False
			for _ in range(5):
				if self.driver.Get_xpath(0).Click().is_click:
					self.driver.Press(self.password)
					isAction =  True
					break
		else:
			isAction =  False
		if isAction == False:
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			printe("Click `mật khẩu` thất bại")
			main.exit()
		
		
		
		
		if self.driver.Set_xpath("//select[@id='ddlSecurityQuestions']", 20).isElement:
			isAction = False
			for _ in range(5):
				if self.driver.Get_xpath(0).Click().is_click:
					self.driver.Sleep(1).DOWN().Sleep(1).DOWN().Sleep(1).ENTER().Sleep(1)
					isAction =  True
					break
		else:
			isAction =  False
		if isAction == False:
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			printe("Click `Chọn câu hỏi bảo` thất bại")
			main.exit()
			
			
		if self.driver.Set_xpath("//input[@id='tbSecurityAnswer']", 20).isElement:
			isAction = False
			for _ in range(5):
				if self.driver.Get_xpath(0).Click().is_click:
					self.driver.Sleep(0.3).Click().Sleep(0.3).Press(self.cau_hoi_bao_mat_reg_value).Sleep(1)
					isAction =  True
					break
		else:
			isAction =  False
		if isAction == False:
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			printe("Click `nhập câu trả lời` thất bại")
			main.exit()

			
		if self.driver.Set_xpath("//input[@id='txtCollectForeignId']", 20).isElement:
			isAction = False
			for _ in range(5):
				if self.driver.Get_xpath(0).Scroll().Scroll_up(300).Click().is_click:
					self.driver.Press(self.cmnd)
					isAction =  True
					break
		else:
			isAction =  False
		if isAction == False:
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			printe("Click `nhập cmnd` thất bại")
			main.exit()
		
		
		
		
		
		
		if self.driver.Set_xpath("//input[@id='AccountDetailsButton']", 20).isElement:
			isAction = False
			for _ in range(5):
				if self.driver.Get_xpath(0).Scroll().Scroll_up(300).Click().is_click:
					isAction =  True
					break
		else:
			isAction =  False
		if isAction == False:
			self.Mail_Reg_Pending.deleteId()
			self.API_Mail.create_database(self.mail, live = 0)
			printe("Click `tiếp theo` thất bại")
			main.exit()
		

		
		
		
	
		
		printx("XONG BƯỚC 3")
		time.sleep(20)
		
		
		
		
		print("Bank")
		

		
		try:
			# hàm get bank
			self.InputBank = Api_database(token, self.Bank_Reg, "").findOne(wheres = {}, key_search = "text_full", search = "", delete = True, hide = True, reset_hide = True).datas
			if len(self.InputBank) == 0:
				self.InputBank = Api_database(token, self.Bank_Reg, "").findOne(wheres = {}, key_search = "text_full", search = "", delete = True, hide = True, reset_hide = True).datas
				if len(self.InputBank) == 0:
					self.Mail_Reg_Pending.deleteId()
					self.API_Mail.create_database(self.mail, live = 0)
					printe("Hết bank")
					main.exit()
			self.bank = self.InputBank["text_full"]
			self.banks = self.bank.split("\t")
			self.bank_name = self.banks[0]
			self.bank_number = self.banks[1]
			self.bank_swift = self.banks[2]
			random_sw = str(random.randint(100,999))
			self.bank_swift = self.bank_swift+random_sw
			
			self.bank_ho_va_ten = self.banks[3]
			
			
			iframes = self.driver.page.query_selector_all('//iframe[starts-with(@id, "iframMR")]')
			iframe = iframes[0]
			frame = iframe.content_frame()
			
			
			
			# nhập tên ngân hàng
			element = frame.locator("//span[contains(@role,'combobox')]")
			element.click()
			time.sleep(3)
			inputtext = frame.locator("//input[@type='search']")
			inputtext.type("Khác")
			time.sleep(3)
			inputtext.press('Enter')
			
			
			
			inputtext = frame.locator("//input[@id='iachfield1']")
			inputtext.click()
			time.sleep(3)
			inputtext.type(self.bank_name)
			time.sleep(3)
			
			# nhập chi nhanh
			inputtext = frame.locator("//input[contains(@id,'iachfield44')]")
			inputtext.type(self.thanh_pho)
			time.sleep(3)
			# nhập ten nguoi nhan
			inputtext = frame.locator("//input[@id='iachfield2']")
# 			inputtext.type(self.lastname+" "+self.middlename+" "+self.firstname)
			inputtext.type(self.lastname+" "+self.firstname)
			
			# nhập số tK
			time.sleep(3)
			inputtext = frame.locator("//input[@id='iachfield3']")
			inputtext.type(self.bank_number)
			
			time.sleep(10)
			
			
			# click vào đồng ý điều khoản
			elm = frame.locator("(//label[@class='radio'])[3]")
			elm.click()
			time.sleep(3)

			frame.locator("//label[contains(.,'Tôi đồng ý với Giá và Phí')]").press('Space')
			time.sleep(3)
			
			# time.sleep(50)

			# click tiếp theo 
			frame.locator("//input[@id='btnNextPhantomOnly']").click()
			time.sleep(6)
			
			
			elm = frame.locator("//input[@id='iachfield4']")
			elm.click()
			time.sleep(5)
			inputtext.type(self.bank_swift)
			time.sleep(3)
			
			
			elm = frame.locator("//input[@id='btnConfirmPhantomOnly']")
			elm.click()
		except:
			pass
# 			main.exit()
		
		
		time.sleep(5)
		if self.driver.Set_xpath_text("Đang trong quá trình xem xét", 20).isElement:
# 			self.text_acc = f"{self.Browser.path_file_cloud_backup}\t{self.mail_user}\t{self.password}\t{self.mail_pass}\t{self.cau_hoi_bao_mat_reg_value}\t{self.phone}\t{self.bank_ho_va_ten}\t{self.bank}\t"+self.lastname+" "+self.middlename+" "+self.firstname+f"\t{self.sn_day}-{self.sn_month}-{self.sn_year}"
			self.text_acc = f"{self.Browser.path_file_cloud_backup}\t{self.mail_user}\t{self.password}\t{self.mail_pass}\t{self.cau_hoi_bao_mat_reg_value}\t{self.bank_ho_va_ten}\t{self.bank_number}\t{self.bank_name}\t"+self.lastname+" "+self.middlename+" "+self.firstname+f"\t{self.sn_day}-{self.sn_month}-{self.sn_year}\t{self.phone}\t{self.proxy}"
			if self.Browser.backup_v2():
				printx("\tMở Backup!!!")
			# lưu vào db tài khoản thành công
			Api_database(token, self.Acc_Reg_Thanh_Cong, "").create_database(self.text_acc, live = 1)
			
# 			TDev.set(dbToken = self.Acc_Reg_Thanh_Cong, value = self.text_acc)
# 			self.bot_telegrams(text = f"""Tạo tài khoản thành công :
# BANK NAME : {self.bank_ho_va_ten}
# BANK NUMBER : {self.bank_number}
# """)
			printx("TẠO TK THÀNH CÔNG")
		
		else:
# 			self.bot_telegram(f"Đã lấy code sms mà đăng ký thất bại")
			printe("Click `tiếp theo` thất bại")
			# thoát tool 
			main.exit()
		
		
		
		
		
		
		
		
		# ---------------------Xác Nhận Link----------------------#
		
		
		
		
		
		time.sleep(200)
		
		
		search = "Vui lòng xác minh email của bạn"
		url_docmail = f"http://127.0.0.1:10000/api/hotmail?username=admin&password=123456&mail_username={self.mail_user}&mail_password={self.mail_pass}&type_find=title&result=body&search={search}"
# 		url_docmail = f"http://localhost:10001/findMail_v2?server=imap-mail.outlook.com&folder=inbox&unread=0&user={self.mail_user}&passwd={self.mail_pass}&email=&title={search}"
		
		
		
		is_mail = False
		for _ in range(5):
			time.sleep(10)
			self.driver.Goto(url_docmail)
			if self.driver.Set_xpath_attr("div","id","sofin_body", 6).isElement:
				printe("Chưa Có Xác Nhận Mail!!!")
				pass
			else:
				is_mail = True
				break
			
		if is_mail != True:
			printe("Không Có Xác Nhận Mail Của Tôi")
# 			main.exit()
		time.sleep(5)
		isAction = False
		if self.driver.Set_xpath("//span[@class='btn-inner']", 20).isElement:
			for _ in range(5):
				if self.driver.Get_xpath(0).Click().is_click:
					isAction =  True
					break
		if isAction == False:
			printe("Chưa Có Mail Xác Nhận!")
# 			TDev.delete()
# 			TDev.set(dbToken = self.db_xac_nhan_chua_co_mail_xac_nhan, value = self.text_acc)
# 			main.exit()
		
		time.sleep(5)
		if self.driver.Set_xpath("//span[@class='btn-inner']", 20).isElement:
			self.driver.Get_xpath(0).element.click()
			printe("Chưa Click Link, Click Lại!")
		else:
			printx("Đã Click Link")
			pass
		
		time.sleep(5)
		if self.driver.Set_xpath_text("You successfully verified your email", 120).isElement:
			printx("Ver Acc Thành Công")
			self.Acc_Reg_Thanh_Cong.delete()
			self.Db_Xac_Nhan_Link_Thanh_Cong.create_database(self.text_acc, live = 1)
		else:
			printe("Acc Ver Thành Công Nhưng Die Proxy")
			self.Acc_Reg_Thanh_Cong.delete()
			self.Db_Xac_Nhan_Link_Thanh_Cong.create_database(self.text_acc, live = 1)
			# thoát tool 
# 			main.exit()
		
# 		main.exit()
		
		
		
		
		
		time.sleep(10)
		
		
		# ---------------------Ver Code--------------------#
		
		self.driver.Goto("https://login.payoneer.com")
		time.sleep(10)
# 		self.Sofin_playwright.Goto("https://login.payoneer.com")
# 		time.sleep(10)
		isAction = False
		if self.driver.Set_xpath("//input[@id='username']", 20).isElement:
			for _ in range(5):
				if self.driver.Get_xpath(0).Click().is_click:
					self.driver.Press(self.mail_user).Sleep(1).TAB().Sleep(1).Press(self.password).Sleep(1).ENTER()
					isAction =  True
					break
		if isAction == False:
			printe("Click `Đăng nhập thất bại` thất bại")
			self.Acc_Reg_Thanh_Cong.delete()
			self.Db_Xac_Nhan_Link_Thanh_Cong.create_database(self.text_acc, live = 1)
			main.exit()
		
		time.sleep(10)
		
		if self.driver.Set_xpath("//span[contains(.,'One or more details is incorrect')]", 2).isElement:
			printe("Acc Một hoặc nhiều chi tiết không chính xác")
			self.Db_Xac_Nhan_Link_Thanh_Cong.delete()
			self.Db_One_Or_More_Details_Is_Incorrect.create_database(self.text_acc, live = 1)
			main.exit()
		
		
		elif self.driver.Set_xpath("//span[contains(.,'It looks like you didn’t finish signing up. Go to the signup page and reenter your details.')]", 2).isElement:
			printe("Mail Chưa Đăng Ký")
			self.Db_Xac_Nhan_Link_Thanh_Cong.delete()
			self.Db_Mail_Chua_Dang_Ky_Thanh_Cong.create_database(self.text_acc, live = 1)
			main.exit()
		
		
		
		elif self.driver.Set_xpath("//span[contains(.,'Account blocked. Contact us.')]", 2).isElement:
			printe("Acc Bị Khoá")
			self.Db_Xac_Nhan_Link_Thanh_Cong.delete()
			self.Db_Tai_Khoan_Ver_Code_Bi_Khoa.create_database(self.text_acc, live = 1)
			main.exit()
		
		
		elif self.driver.Set_xpath("//span[contains(.,'Account locked. To unlock it, reset your password.')]", 2).isElement:
			printe("Acc Bị Khoá")
			self.Db_Xac_Nhan_Link_Thanh_Cong.delete()
			self.Db_Tai_Khoan_Ver_Code_Bi_Khoa.create_database(self.text_acc, live = 1)
			main.exit()
		
		
		
		elif self.driver.Set_xpath("//span[contains(.,'Account locked. Try again in 30 minutes or reset your password.')]", 2).isElement:
			printe("Acc Bị Khoá")
			self.Db_Xac_Nhan_Link_Thanh_Cong.delete()
			self.Db_Tai_Khoan_Ver_Code_Bi_Khoa.create_database(self.text_acc, live = 1)
			main.exit()
		
		
		elif self.driver.Set_xpath("//span[contains(.,'Your account was closed as some of your activity has gone against our Terms and Conditions. Learn more')]", 2).isElement:
			printe("Acc Bị Khoá")
			self.Db_Xac_Nhan_Link_Thanh_Cong.delete()
			self.Db_Tai_Khoan_Ver_Code_Bi_Khoa.create_database(self.text_acc, live = 1)
			main.exit()
		

		
		else:
			printx("Acc Cần Ver")
		
		
		
		
		try:
			iframes = self.driver.page.query_selector_all('//iframe[starts-with(@src, "https://login.payoneer.com/auth")]')
			iframe = iframes[0]
			frame = iframe.content_frame()
	
			try:
				elm = frame.locator("//input[@id='answer1']")
				elm.click()
				elm.type(self.cau_hoi_bao_mat_reg_value)
				time.sleep(1)
			except:
				pass
			
			try:
				elm = frame.locator("//input[@id='answer2']")
				elm.click()
				elm.type(self.cau_hoi_bao_mat_reg_value)
				time.sleep(1)
			except:
				pass
				
			try:
				elm = frame.locator("//input[@id='answer3']")
				elm.click()
				elm.type(self.cau_hoi_bao_mat_reg_value)
				time.sleep(1)
			except:
				pass
			
			elm = frame.locator("//button[@id='send-code-button']")
			elm.click()
# 			elm.press('Enter')
			
			
			
			

		except:
			printe("Lỗi nhập câu hỏi bảo mật khi login")
# 			TDev.delete()
# 			TDev.set(dbToken = self.db_acc_ver, value = self.text_acc)
# 			main.exit()
		
		
		time.sleep(20)
		try:
			printx("Tab Bỏ Qua")
			iframes = self.driver.page.query_selector_all('//iframe[starts-with(@src, "https://login.payoneer.com/auth")]')
			iframe = iframes[0]
			frame = iframe.content_frame()
	
			elm = frame.locator("//button[contains(.,'Not now')]")
			elm.click()
		except:
			printx("Không Có Case Tab Bỏ Qua")
			pass

		

		
		
		
		
		
		
		
		
		
		
		
		
		time.sleep(30)
		isAction = False
		if self.driver.Set_xpath_text("CẬP NHẬT NGAY", 60).isElement:
			for _ in range(5):
				if self.driver.Get_xpath(0).Click().is_click:
					isAction =  True
					break
		if isAction == False:
			printe("Click `CẬP NHẬT NGAY` thất bại")
			self.Db_Xac_Nhan_Link_Thanh_Cong.delete()
			self.Db_Xac_Nhan_Link_Thanh_Cong.create_database(self.text_acc, live = 1)
			main.exit()
		
		

			
			
		# NHẬP CÂU HỎI BAO MẬT
		isAction = False
		if self.driver.Set_xpath("//input[@name='Question1.SecurityAnswer']", 20).isElement:
			for _ in range(5):
				if self.driver.Get_xpath(0).Scroll().Scroll_up(300).Click().is_click:
				# 	self.driver.Press(self.cau_hoi).Sleep(1).TAB().Sleep(0.5).TAB().Sleep(0.5).TAB()
					self.driver.Press(self.cau_hoi_bao_mat_reg_value).Sleep(1)
					isAction =  True
					break
		if isAction == False:
			printe("Click `Nhập Câu Hỏi 1` thất bại")
			self.Db_Xac_Nhan_Link_Thanh_Cong.delete()
			self.Db_Xac_Nhan_Link_Thanh_Cong.create_database(self.text_acc, live = 1)
			main.exit()
		
		
		isAction = False
		if self.driver.Set_xpath("//input[@name='Question2.SecurityAnswer']", 20).isElement:
			for _ in range(5):
				if self.driver.Get_xpath(0).Scroll().Scroll_up(300).Click().is_click:
				# 	self.Sofin_playwright.Press(self.cau_hoi).Sleep(1).TAB().Sleep(0.5).TAB().Sleep(0.5).TAB()
					self.driver.Press(self.cau_hoi_bao_mat_reg_value).Sleep(1)
					isAction =  True
					break
		if isAction == False:
			printe("Click `Nhập Câu Hỏi 2` thất bại")
			self.Db_Xac_Nhan_Link_Thanh_Cong.delete()
			self.Db_Xac_Nhan_Link_Thanh_Cong.create_database(self.text_acc, live = 1)
			main.exit()
			
			
		isAction = False
		if self.driver.Set_xpath("//input[@name='Question3.SecurityAnswer']", 20).isElement:
			for _ in range(5):
				if self.driver.Get_xpath(0).Scroll().Scroll_up(300).Click().is_click:
					self.driver.Press(self.cau_hoi_bao_mat_reg_value).Sleep(1).ENTER()
					isAction =  True
					break
		if isAction == False:
			printe("Click `Nhập Câu Hỏi 3` thất bại")
			self.Db_Xac_Nhan_Link_Thanh_Cong.delete()
			self.Db_Xac_Nhan_Link_Thanh_Cong.create_database(self.text_acc, live = 1)
			main.exit()

		
# 		if m2proxy_com(self.proxy_api):
# 			printc("ĐỔI PROPXY RỒI NHÉ")
# 		time.sleep(10)
		

			

		time.sleep(220)
		
		
		


		
		code = False
		# link = False
		for _ in range(10):
			# link = get_mail_po(type_get = "link",search = "Vui lòng xác minh email của bạn", email = self.mail_user, passwd = self.mail_pass))
			code = get_mail_po(type_get = "code",search = "Mã xác minh của bạn từ Payoneer", email = self.mail_user, passwd = self.mail_pass)
			if code != False:
				break
			time.sleep(10)
		if code == False:
			printw("Mail Không Có Code!!!!!")
			self.Db_Xac_Nhan_Link_Thanh_Cong.delete()
			self.Db_Mail_Ver_Khong_Co_Code.create_database(self.text_acc, live = 1)
			main.exit()
		
		
		printx("code nèeeeeeee <3333: " +code)
# 		print(code)
		
		
		
		self.driver.Sleep(1).Press(code).Sleep(1).ENTER().Sleep(3).ENTER().Sleep(30)
		
		
		
		

		
		
		
		
		
		
		
		
		if self.driver.Set_xpath_text("Tài khoản bị khóa", 10).isElement:
			printe("Acc Bị Khoá")
			self.Db_Xac_Nhan_Link_Thanh_Cong.delete()
			self.Db_Tai_Khoan_Ver_Code_Bi_Khoa.create_database(self.text_acc, live = 1)
			main.exit()
		else:
			printx("Acc Live")
			pass
		
		
		
		
		
		
		
		
		
		for _ in range(2):
			isAction = False
			if self.driver.Set_xpath("//button[@type='button']", 20).isElement:
				for _ in range(3):
					if self.driver.Get_xpath(0).Scroll().Scroll_up(300).Click().is_click:
						isAction =  True
						break
			time.sleep(15)
			if isAction == False:
				printe("Click `Done` thất bại")
		        self.Db_Xac_Nhan_Link_Thanh_Cong.delete()
		        self.Db_Xac_Nhan_Link_Thanh_Cong.create_database(self.text_acc, live = 1)
				main.exit()
		
		
		
			
		
		
		
		printe("Xác minh bước 3 thành công")

		time.sleep(5)
		
		
		
		
		is_live = False
		for _ in range(10):
			try:
				self.driver.Goto("https://myaccount.payoneer.com/ma/")
				time.sleep(3)
				if self.driver.Set_xpath("//span[contains(.,'Tài khoản của bạn đã được duyệt')]", 5).isElement:
					is_live = True
					break
			except:
				pass
		if is_live:
			self.Db_Xac_Nhan_Link_Thanh_Cong.delete()
			self.Db_Acc_Ver_Done_Co_Tick_Xanh.create_database(self.text_acc, live = 1)
			printx("Lưu Acc Có Tick Xanh Thành Công <333333")
# 			text_bot_tele = f"""Account OK, Chờ Xác Minh.\nName:  {self.ho_va_ten}\nBANK NUMBER : {self.bank_number}"""
# 			self.bot_telegram(f"""Acc Có Tick Xanh Chờ Làm Tay :
# BANK NAME : {self.bank_ho_va_ten}
# BANK NUMBER : {self.bank_number}
# """)
		else:
			self.Db_Xac_Nhan_Link_Thanh_Cong.delete()
			self.Db_Acc_Ver_Khonggggg_Co_Tick_Xanh.create_database(self.text_acc, live = 1)
			printe("Lưu Acc Không Có Tick Xanh Thành Công!!!!")
# 			text_bot_tele = f"""KHÔNG CÓ TÍCH XANH NHÉ : {self.ho_va_ten}\nBANK NUMBER : {self.bank_number}"""
		
# 		self.bot_telegram(text_bot_tele)
		main.exit()

		
		
		
			
		
# 		time.sleep(2)
		
		main.exit()
GOGL()