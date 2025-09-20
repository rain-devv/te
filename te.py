#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
أداة متقدمة للإبلاغ عن المحتوى غير الملائم على Telegram
تم تطويرها بواسطة ماجد المهندس - حقوق ToHelx / HelxOne محفوظة
"""

import requests
import random
import re
import time
import sys
from typing import Tuple, List, Optional
from datetime import datetime

class AdvancedAntiPornReporter:
    def __init__(self):
        # تنسيق الألوان للواجهة
        self.COLORS = {
            'RED': '\033[1;31m',
            'GREEN': '\033[1;32m',
            'YELLOW': '\033[1;33m',
            'BLUE': '\033[1;34m',
            'PURPLE': '\033[1;35m',
            'CYAN': '\033[1;36m',
            'WHITE': '\033[1;37m',
            'END': '\033[0m'
        }
        
        # قائمة وكيل مستخدم متنوعة
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1"
        ]
        
        self.session = requests.Session()
        self.success_count = 0
        self.failure_count = 0
        self.start_time = None
        
    def print_banner(self):
        """عرض شعار البرنامج"""
        banner = f"""
{self.COLORS['PURPLE']}╔══════════════════════════════════════════════════════════════╗
{self.COLORS['PURPLE']}║{self.COLORS['CYAN']}         أداة مكافحة المحتوى غير الملائم على Telegram         {self.COLORS['PURPLE']}║
{self.COLORS['PURPLE']}║{self.COLORS['CYAN']}               الإصدار المتقدم - عالي الدقة               {self.COLORS['PURPLE']}║
{self.COLORS['PURPLE']}║{self.COLORS['YELLOW']}         تم التطوير بواسطة ماجد المهندس - ToHelx         {self.COLORS['PURPLE']}║
{self.COLORS['PURPLE']}╚══════════════════════════════════════════════════════════════╝
        {self.COLORS['END']}"""
        print(banner)
    
    def color_print(self, text: str, color: str) -> None:
        """طباعة نص ملون"""
        color_code = self.COLORS.get(color, self.COLORS['WHITE'])
        print(f"{color_code}{text}{self.COLORS['END']}")
    
    def generate_realistic_email(self) -> str:
        """إناء بريد إلكتروني واقعي أكثر"""
        domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com"]
        prefixes = [
            "john.doe", "jane_smith", "mike1987", "sara.ali", "ahmed90", 
            "loyal_user", "telegram_supporter", "community_guardian", "online_safety"
        ]
        
        username = random.choice(prefixes)
        if random.random() > 0.5:
            username += str(random.randint(10, 99))
        
        return f"{username}@{random.choice(domains)}"

    def generate_credible_phone(self) -> str:
        """إنشاء رقم هاتف أكثر مصداقية"""
        country_codes = {
            "US": ["+1", 10],
            "UK": ["+44", 10],
            "FR": ["+33", 9],
            "DE": ["+49", 10],
            "AE": ["+971", 9]
        }
        
        country = random.choice(list(country_codes.keys()))
        code, digits = country_codes[country]
        
        # إنشاء رقم واقعي
        number = ''.join([str(random.randint(0, 9)) for _ in range(digits)])
        return code + number

    def get_country_language_code(self) -> Tuple[str, str]:
        """الحصول على رمز بلد ولغة متطابقين"""
        country_languages = {
            "en": ["US", "GB", "AU", "CA"],
            "es": ["ES", "MX", "AR"],
            "fr": ["FR", "CA", "BE"],
            "de": ["DE", "AT", "CH"],
            "ar": ["SA", "AE", "EG"]
        }
        
        lang = random.choice(list(country_languages.keys()))
        country = random.choice(country_languages[lang])
        return country, lang

    def get_authentic_headers(self) -> dict:
        """إنشاء رؤوس طلب تبدو حقيقية"""
        base_headers = {
            'authority': 'telegram.org',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://telegram.org',
            'referer': 'https://telegram.org/support',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
        }
        
        # إضافة وكيل مستخدم عشوائي
        base_headers['user-agent'] = random.choice(self.user_agents)
        
        return base_headers

    def create_persuasive_message(self, message_link: str, channel_link: str) -> str:
        """إنشاء رسالة إبلاغ مقنعة وواقعية"""
        templates = [
            f"""
Dear Telegram Support Team,

I am writing to report inappropriate content that violates Telegram's Terms of Service.

I came across a channel that is distributing explicit adult content without proper age verification. This is particularly concerning as it's easily accessible to minors.

The offending message can be found here: {message_link}
The channel in question is: {channel_link}

I believe this content violates section 3 of your Terms of Service regarding prohibited content. I would appreciate it if you could review this matter and take appropriate action.

Thank you for your attention to this important issue.

Sincerely,
A concerned user
            """,
            f"""
Hello Telegram Team,

I wanted to bring to your attention a channel that appears to be sharing pornographic material in violation of your community guidelines.

Message link: {message_link}
Channel: {channel_link}

As a parent and long-time Telegram user, I'm concerned about the ease with which such content can be accessed by underage users. I hope you will investigate and remove this content if it indeed violates your policies.

Best regards,
            """,
            f"""
To the Telegram Safety Department,

I am reporting a channel that is distributing explicit sexual content without proper safeguards. This seems to be a clear violation of your platform's rules against adult content.

Specific offending content: {message_link}
Channel source: {channel_link}

I've been a Telegram user for years and value the platform's commitment to user safety. I trust you'll handle this report with appropriate urgency.

Respectfully,
            """
        ]
        
        return random.choice(templates).strip()

    def send_intelligent_report(self, message_link: str, channel_link: str) -> Tuple[bool, str]:
        """إرسال بلاغ ذكي مع محاولات متعددة إذا لزم الأمر"""
        max_attempts = 2
        for attempt in range(max_attempts):
            try:
                # إنشاء بيانات الطلب
                email = self.generate_realistic_email()
                phone = self.generate_credible_phone()
                country, lang = self.get_country_language_code()
                
                message = self.create_persuasive_message(message_link, channel_link)
                
                data = {
                    'message': message,
                    'email': email,
                    'phone': phone,
                    'setln': lang,
                }
                
                # إرسال الطلب مع تأخير عشوائي
                delay = random.uniform(3, 8)
                time.sleep(delay)
                
                response = self.session.post(
                    'https://telegram.org/support',
                    headers=self.get_authentic_headers(),
                    data=data,
                    timeout=25,
                    allow_redirects=True
                )
                
                # تحليل الاستجابة بدقة
                if response.status_code == 200:
                    if "thank you" in response.text.lower() or "شكرًا" in response.text.lower():
                        return True, "تم إرسال البلاغ بنجاح ✅"
                    elif "success" in response.text.lower():
                        return True, "تم الإبلاغ بنجاح ✅"
                    else:
                        # محاولة أخرى إذا لم تكن هناك إشارة واضحة للنجاح
                        continue
                else:
                    return False, f"استجابة غير متوقعة: {response.status_code}"
                    
            except requests.exceptions.ConnectionError:
                return False, "فشل في الاتصال بالخادم 🌐"
            except requests.exceptions.Timeout:
                return False, "انتهت مهلة الاتصال ⏰"
            except Exception as e:
                return False, f"خطأ غير متوقع: {str(e)}"
        
        return False, "فشل بعد محاولات متعددة 🔄"

    def run_continuous_reporting(self, message_link: str, channel_link: str, report_count: int):
        """تشغيل عملية الإبلاغ المستمرة"""
        self.start_time = datetime.now()
        
        for i in range(report_count):
            current_time = datetime.now().strftime("%H:%M:%S")
            self.color_print(f"[{current_time}] إرسال البلاغ رقم {i+1}...", "YELLOW")
            
            success, message = self.send_intelligent_report(message_link, channel_link)
            
            if success:
                self.color_print(f"✓ {message}", "GREEN")
                self.success_count += 1
            else:
                self.color_print(f"✗ {message}", "RED")
                self.failure_count += 1
            
            # تأخير متغير بين المحاولات
            delay = random.uniform(5, 15)
            time.sleep(delay)
            
            # عرض إحصاءات دورية
            if (i + 1) % 5 == 0:
                self.show_progress()

    def show_progress(self):
        """عرض تقدم العملية"""
        elapsed = datetime.now() - self.start_time
        elapsed_str = str(elapsed).split('.')[0]
        
        print()
        self.color_print("📊 إحصاءات التقدم:", "CYAN")
        self.color_print(f"   النجاحات: {self.success_count}", "GREEN")
        self.color_print(f"   الإخفاقات: {self.failure_count}", "RED")
        self.color_print(f"   الوقت المنقضي: {elapsed_str}", "CYAN")
        print()

    def show_summary(self):
        """عرض ملخص النتائج"""
        total = self.success_count + self.failure_count
        success_rate = (self.success_count / total) * 100 if total > 0 else 0
        
        print()
        self.color_print("=" * 50, "PURPLE")
        self.color_print("ملخص النتائج النهائية", "CYAN")
        self.color_print("=" * 50, "PURPLE")
        
        self.color_print(f"إجمالي البلاغات المرسلة: {total}", "WHITE")
        self.color_print(f"البلاغات الناجحة: {self.success_count}", "GREEN")
        self.color_print(f"البلاغات الفاشلة: {self.failure_count}", "RED")
        self.color_print(f"معدل النجاح: {success_rate:.2f}%", "YELLOW")
        
        elapsed = datetime.now() - self.start_time
        self.color_print(f"الوقت الإجمالي: {str(elapsed).split('.')[0]}", "WHITE")
        
        self.color_print("=" * 50, "PURPLE")

    def run(self):
        """الدالة الرئيسية لتشغيل البرنامج"""
        self.print_banner()
        
        try:
            # الحصول على المدخلات من المستخدم
            self.color_print("📝 يرجى إدخال معلومات البلاغ:", "CYAN")
            message_link = input(f"{self.COLORS['WHITE']}• رابط الرسالة المخالفة: {self.COLORS['END']}")
            channel_link = input(f"{self.COLORS['WHITE']}• رابط القناة المخالفة: {self.COLORS['END']}")
            
            report_count = input(f"{self.COLORS['WHITE']}• عدد البلاغات المراد إرسالها (افتراضي: 10): {self.COLORS['END']}")
            if not report_count:
                report_count = 10
            else:
                report_count = int(report_count)
                
            # تأكيد البدء
            print()
            self.color_print(f"سيتم إرسال {report_count} بلاغ للمحتوى غير الملائم", "YELLOW")
            confirm = input(f"{self.COLORS['WHITE']}هل تريد البدء؟ (y/n): {self.COLORS['END']}")
            
            if confirm.lower() != 'y':
                self.color_print("تم إلغاء العملية.", "RED")
                return
                
            # بدء عملية الإبلاغ
            print()
            self.color_print("بدء عملية الإبلاغ...", "GREEN")
            self.run_continuous_reporting(message_link, channel_link, report_count)
            
            # عرض النتائج
            self.show_summary()
            
        except (KeyboardInterrupt, EOFError):
            self.color_print("\nتم إيقاف البرنامج بواسطة المستخدم", "YELLOW")
            if self.start_time:
                self.show_summary()
        except ValueError:
            self.color_print("خطأ: يجب إدخال رقم صحيح لعدد البلاغات", "RED")
        except Exception as e:
            self.color_print(f"حدث خطأ غير متوقع: {str(e)}", "RED")

if __name__ == "__main__":
    try:
        reporter = AdvancedAntiPornReporter()
        reporter.run()
    except Exception as e:
        print(f"فشل تشغيل البرنامج: {str(e)}")
