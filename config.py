import os
from instaloader import Instaloader
class Config:
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    USER = os.environ.get("INSTAGRAM_USERNAME", "")
    OWNER = os.environ.get("OWNER_ID", "")
    INSTA_SESSIONFILE_ID = os.environ.get("INSTA_SESSIONFILE_ID", None)
    S = "0"
    STATUS = set(int(x) for x in (S).split())
    L=Instaloader()
    HELP="""
Sən istənilən post'u istənilən Instagram hesabından endirə bilərsən.

<b>Biz nələri edə bilərik?:</b>

1. İstənilən profilin bütün postları  (İctimai olan hesabların postlarını və hesabına giriş etməklə şəxsi postları.)
2. Sənin bütün postlarını. 
3. İstənilən profilin story'ni (İctimai olan hesabların postlarını və hesabına giriş etməklə şəxsi postları.)
4. Profil detallarını.
5. İstənilən hesabın izləyici və izlədikləri hesablar.
6. Səni geri izləyən izlədiyin hesablar.
7. Səni geri izləyən izlədiyin hesablar.
8. Sənin izlədiyin hesabların story'ləri.
9. İstənilən profilin tag edilmiş postları .
10. Sənin yaddaşa vurduğun postlar.
11. IGTV videoları.
12. İstənilən profil'in highlight'larını endirmək.
13. Link vasitəsilə istənilən postu endirmək.


<b>Necə endirmək olar:</b>

Bu çox asandır!
Sənv/login yazmaqla hesabına giriş etməlisən. ⚠️ Diqqət ⚠️ məlumatlar 3-cü şəxs tərəfindən oxunmur.

Sənin iki seçimin var:

1. İstifadəçi adı daxil etməklə:

İstənilən istifadəçi adını göndər.

For Example:
<code>husnumustafayev75</code>


2. Link vasitəsilə:

Siz həmçinin post və ya videonu yükləmək üçün bağlantını göndərə bilərsiniz.

Məsələn:
<code>https://www.instagram.com/p/CbAMPg6KbPJ/?utm_medium=copy_link</code


<b>Əlçatan xüsusiyyətlər və istifadə qaydaları </b>

/start - Botun işlək olduğunu test edin.
/restart - Botu yenidən başlat (Nəysə səhv getdikdə /restart əmrindən istifadə et..)
/help - Hazırki menyunu göstərər.
/login - Hesabına giriş etmək üçün əmr.
/logout - Hesabından çıxış etmək üçün əmr .
/account - Daxil olunmuş hesab barəsində detalları əldə et.

/posts <username> - İstənilən istifadəçinin postlarını endir. Öz postunu və ya <code> /posts <username> </code> digərlərinin postlarını endirmək üçün istifadə et..
Example : <code>/posts husnumustafayev75</code>

/igtv <username> - Verilmiş istifadəçi adından İGTV - videolarını endirin. Əgər istifadəçi adı verilməzsə sənin İGTV videolarını endirər.

/feed <number of posts to download> - Hesabınızdan postları endirir.Əgər nömrə göstərilməyibsə hesabınızdakı bütün postları endirəcək.
Nümunə: <code>/feed 10</code> hesabda ən son 10 postu yükləmək üçün .

/saved <number of posts to download> - Yadda saxlanılan postları endirir. Əgər nömrə göstərilməyibsə hesabınızdakı bütün saxlanılan postları endirəcək.
Nümunə: <code>/saved 10</code> saxlanmış ən son 10 postu yükləmək üçün .

/followers <username> - Verilmiş istifadəçi adının bütün izləyicilərinin siyahısını əldə edin. Heç bir istifadəçi adı verilməyibsə siyahınız bərpa olunacaq.
Example: <code>/followers husnumustafayev75</code>

/followees <username> - Verilmiş istifadəçi adının bütün izlədiklərinin siyahısını əldə edin.Heç bir istifadəçi adı verilməyibsə siyahınız bərpa olunacaq

/fans <username> - Verilmiş istifadəçi adının geri izləyən izləyicilərin siyahını əldə edin.Heç bir istifadəçi adı verilməyibsə siyahınız bərpa olunacaq

/notfollowing <username> - Verilmiş istifadəçi adını geri izləməyən izləyicilərin siyahısını əldə edin.

/tagged <username> - İstifadəçi adının tağ edildiyi bütün postları yükləyər. Heç bir əmr verilmədikdə tağ edilmiş postlarınız endiriləcək.

/story <username> - Verilmiş istifadəçi adından bütün hekayələri yükləyir. Heç bir şey verilməzsə hekayələriniz endiriləcək.

/stories - Bütün izlədiklərinizin bütün hekayələrini yükləyin.

/highlights <username> - Verilmiş istifadəçi adından highlight'ları endirir. Əgər heç bir əmr verilməzsə sizin highlight'larınız endiriləcək.


"""
    HOME_TEXT = """
<b>Salam, [{}](tg://user?id={})


Use /help to know What I can Do?</b>
"""
    HOME_TEXT_OWNER = """
<b>Salam, [{}](tg://user?id={})
Sənin hesabını idarə etmək üçün nəzərdə tutulmuş köməkçinizəm.

Sizin üçün nə edə biləcəyimi bilmək üçün /help əmrindən istifadə edin.</b>
"""

