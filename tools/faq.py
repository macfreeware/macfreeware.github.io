"""FAQ and alternatives text, shared with the app READMEs (English and Turkish)."""

DATA = {
    "MacMonitor": {
        "en": {
            "lead": ("  A native <b>menu bar monitor</b> for macOS:", "  A free, open-source <b>menu bar monitor</b> for macOS:"),
            "alt": "A lightweight, free alternative to <b>iStat Menus</b>, <b>Stats</b> and <b>MenuMeters</b> when you only need CPU, memory, disk and battery at a glance.",
            "faq": """## FAQ

### Is MacMonitor free?

Yes. MacMonitor is free and open source under the GPL-3.0 license. There are no ads, no accounts and no in-app purchases, and it collects nothing; its only connection is the daily update check on GitLab, which you can turn off.

### How do I see CPU and RAM usage in the Mac menu bar?

Install MacMonitor: CPU and RAM percentages appear in the menu bar right away and refresh every 0.5 to 5 seconds. Click them for per-core load, the memory breakdown and the processes using the most CPU or memory.

### How do I check free disk space on my Mac?

Click MacMonitor in the menu bar and open the **Disk** tab. It shows free, used and total space for the startup disk and every external drive, calculated the same way as Finder.

### How do I check my Mac's battery health and charge history?

Open MacMonitor's **Battery** tab. It shows the charge, time remaining, power draw, battery health (the same "Maximum Capacity" as System Settings) and cycle count, and a chart of the charge level and system power over the last hour, 24 hours, 7 days, 30 days or everything recorded. macOS itself only shows the last 24 hours.

### Does MacMonitor keep a battery history when the panel is closed?

Yes. It records the battery once a minute while it runs and keeps 90 days, about 1 MB, in `~/Library/Application Support/MacMonitor` on your Mac. Nothing is sent anywhere. The Battery tab only appears on Macs with a battery.

### How do I see network speed in the Mac menu bar?

MacMonitor shows download and upload speed in two small lines next to CPU and RAM, in MB/s or Mbit/s. The **Network** tab adds usage for today, yesterday, this week, this month and last month, with charts by minute, hour, day or month, kept for 400 days.

### How do I see when my Mac was charging, and how long the screen was on?

Open **Details** in MacMonitor's **Battery** tab. The chart colors charging, plugged-in and on-battery time, with a strip for when the screen was on, and lists every charging session with its start, length and charge gained.

### Does MacMonitor update itself?

Yes, from version 1.3.0. Once a day it looks for a new release on GitLab and shows what's new. If you choose **Update Now**, it downloads the update, checks its SHA-256 and signature, replaces itself and restarts, and your battery history is kept. No password is needed. You can skip a version, or turn the check off in Settings.

### Will it slow down my Mac?

No. With the panel closed MacMonitor uses about 0.1% of total CPU and 40 MB of memory. It doesn't run shell commands such as `top` or `ps`, so it adds nothing to the system log.

### How is it different from iStat Menus or Stats?

MacMonitor does less on purpose: CPU, memory, network speed, disk space, the battery and the top processes. It has no sensor or GPU graphs. If those essentials are all you want, it stays small and quiet.

### Which Macs does it run on?

Apple Silicon and Intel Macs with macOS 13 Ventura or later.

### Why does macOS block it the first time?

MacMonitor is not notarized by Apple, which needs a paid developer account. Allow it once in **System Settings ▸ Privacy & Security ▸ Open Anyway**; see [First launch](#first-launch-allow-the-installer-once).

<sub>iStat Menus, Stats and MenuMeters are named only for comparison; MacMonitor is not affiliated with them.</sub>

""",
        },
        "tr": {
            "lead": ("  macOS için yerel bir <b>menü çubuğu izleyicisi</b>:", "  macOS için ücretsiz ve açık kaynak bir <b>menü çubuğu izleyicisi</b>:"),
            "alt": "Yalnızca CPU, bellek, disk ve pile bir bakışta göz atmak istiyorsanız <b>iStat Menus</b>, <b>Stats</b> ve <b>MenuMeters</b>'a hafif ve ücretsiz bir alternatif.",
            "faq": """## Sık sorulan sorular

### MacMonitor ücretsiz mi?

Evet. MacMonitor, GPL-3.0 lisansıyla ücretsiz ve açık kaynaktır. Reklam, hesap ya da uygulama içi satın alma yoktur, hiçbir veri toplamaz; tek bağlantısı GitLab'daki günlük güncelleme denetimidir ve kapatılabilir.

### Mac'te menü çubuğunda CPU ve RAM kullanımını nasıl görürüm?

MacMonitor'ı kurun: CPU ve RAM yüzdeleri hemen menü çubuğunda belirir ve 0,5 ile 5 saniye arasında yenilenir. Tıklayınca çekirdek yükleri, bellek dağılımı ve en çok CPU ya da bellek kullanan işlemler açılır.

### Mac'imde ne kadar boş disk alanı kaldığını nasıl görürüm?

Menü çubuğunda MacMonitor'a tıklayıp **Disk** sekmesini açın. Başlangıç diskinin ve bağlı her harici diskin boş, kullanılan ve toplam alanını Finder ile aynı hesapla gösterir.

### Mac'imin pil sağlığını ve şarj geçmişini nasıl görürüm?

MacMonitor'ın **Pil** sekmesini açın. Şarj yüzdesini, kalan süreyi, güç tüketimini, pil sağlığını (Sistem Ayarları'ndaki "Maksimum Kapasite" ile aynı) ve döngü sayısını; son 1 saat, 24 saat, 7 gün, 30 gün ya da kaydedilen tüm süre için şarj düzeyi ve sistem gücü grafiğini gösterir. macOS'un kendisi yalnızca son 24 saati gösterir.

### Panel kapalıyken de pil geçmişi kaydediliyor mu?

Evet. MacMonitor çalıştığı sürece pili dakikada bir kaydeder ve 90 günü (yaklaşık 1 MB) Mac'inizde, `~/Library/Application Support/MacMonitor` içinde tutar. Hiçbir yere gönderilmez. Pil sekmesi yalnızca pilli Mac'lerde görünür.

### Mac menü çubuğunda ağ hızını nasıl görürüm?

MacMonitor indirme ve yükleme hızını CPU ve RAM'in yanında iki küçük satırda, MB/s ya da Mbit/s olarak gösterir. **Ağ** sekmesi bugün, dün, bu hafta, bu ay ve geçen ayın kullanımını, dakika, saat, gün ya da ay bazında grafiklerle ekler ve 400 gün saklar.

### Mac'imin ne zaman şarj olduğunu ve ekranın ne kadar açık kaldığını nasıl görürüm?

MacMonitor'ın **Pil** sekmesinde **Ayrıntılar**'ı açın. Grafik şarj, prizde ve pilde geçen süreyi renklendirir, ekranın açık olduğu zamanları bir şeritte gösterir ve her şarj oturumunu başlangıcı, süresi ve kazanılan şarjla listeler.

### MacMonitor kendini günceller mi?

Evet, 1.3.0 sürümünden itibaren. Günde bir kez GitLab'da yeni sürüme bakar ve yenilikleri gösterir. **Şimdi Güncelle**'yi seçerseniz güncellemeyi indirir, SHA-256 değerini ve imzasını denetler, kendini değiştirip yeniden başlar; pil geçmişiniz korunur. Parola gerekmez. Bir sürümü atlayabilir ya da denetimi Ayarlar'dan kapatabilirsiniz.

### Mac'imi yavaşlatır mı?

Hayır. Panel kapalıyken toplam CPU'nun yaklaşık %0,1'ini ve 40 MB bellek kullanır. `top` ya da `ps` gibi kabuk komutları çalıştırmadığı için sistem loguna bir şey eklemez.

### iStat Menus ya da Stats'tan farkı ne?

MacMonitor bilerek daha az şey yapar: CPU, bellek, ağ hızı, disk alanı, pil ve en çok kaynak kullanan işlemler. Sensör ya da GPU grafikleri yoktur. Yalnızca bu temel bilgileri istiyorsanız küçük ve sessiz kalır.

### Hangi Mac'lerde çalışır?

macOS 13 Ventura veya üstü yüklü Apple Silicon ve Intel Mac'lerde.

### macOS neden ilk seferde engelliyor?

MacMonitor, ücretli geliştirici hesabı gerektiren Apple onayından (notarization) geçmemiştir. **Sistem Ayarları ▸ Gizlilik ve Güvenlik ▸ Yine de Aç** ile bir kez izin verin; ayrıntılar [İlk açılış](#i̇lk-açılış-kurulum-paketine-bir-kez-izin-verin) bölümünde.

<sub>iStat Menus, Stats ve MenuMeters yalnızca karşılaştırma için anılmıştır; MacMonitor'ın bunlarla bir bağı yoktur.</sub>

""",
        },
    },
    "MacCalendar": {
        "en": {
            "lead": ("  A native <b>menu bar calendar</b> for macOS", "  A free, open-source <b>menu bar calendar</b> for macOS"),
            "alt": "A free alternative to <b>Itsycal</b>, <b>Dato</b> and <b>Clocker</b>: a month calendar and a second time zone right in the menu bar.",
            "faq": """## FAQ

### Is MacCalendar free?

Yes. MacCalendar is free and open source under the GPL-3.0 license, with no ads, no accounts and no in-app purchases.

### How do I show a calendar in the Mac menu bar?

The macOS menu bar clock has no month view. Install MacCalendar and click the date in the menu bar: a month calendar opens with today highlighted, a **Today** button and quick notes for any day.

### How do I add a second time zone or world clock to the Mac menu bar?

Turn on the dual clock in MacCalendar's Settings and pick any of more than 400 cities. The menu bar then shows both times with country flags, for example `🇹🇷 20:04   🇯🇵 02:04`, and the calendar shows the time difference.

### Does it show my Apple Calendar events?

No. MacCalendar shows the month grid and its own quick notes for each day; it does not read events from the Calendar app.

### Which Macs does it run on?

Apple Silicon and Intel Macs with macOS 13 Ventura or later.

### Why does macOS block it the first time?

MacCalendar is not notarized by Apple, which needs a paid developer account. Allow it once in **System Settings ▸ Privacy & Security ▸ Open Anyway**; see [First launch](#first-launch-allow-the-installer-once).

<sub>Itsycal, Dato and Clocker are named only for comparison; MacCalendar is not affiliated with them.</sub>

""",
        },
        "tr": {
            "lead": (", yerel bir <b>menü çubuğu takvimi</b>.<br>", ", ücretsiz ve açık kaynak bir <b>menü çubuğu takvimi</b>.<br>"),
            "alt": "<b>Itsycal</b>, <b>Dato</b> ve <b>Clocker</b>'a ücretsiz bir alternatif: menü çubuğunda aylık takvim ve ikinci bir saat dilimi.",
            "faq": """## Sık sorulan sorular

### MacCalendar ücretsiz mi?

Evet. MacCalendar, GPL-3.0 lisansıyla ücretsiz ve açık kaynaktır; reklam, hesap ya da uygulama içi satın alma yoktur.

### Mac'te menü çubuğunda takvimi nasıl gösteririm?

macOS'un menü çubuğu saatinde aylık görünüm yoktur. MacCalendar'ı kurup menü çubuğundaki tarihe tıklayın: bugünün vurgulandığı aylık takvim, **Bugün** düğmesi ve her gün için hızlı notlar açılır.

### Mac menü çubuğuna ikinci bir saat dilimi ya da dünya saati nasıl eklenir?

MacCalendar'ın Ayarlar'ında çift saati açıp 400'den fazla şehirden birini seçin. Menü çubuğu iki saati ülke bayraklarıyla gösterir, örneğin `🇹🇷 20:04   🇯🇵 02:04`; takvim de saat farkını gösterir.

### Apple Takvim etkinliklerimi gösterir mi?

Hayır. MacCalendar aylık takvimi ve her gün için kendi hızlı notlarını gösterir; Takvim uygulamasındaki etkinlikleri okumaz.

### Hangi Mac'lerde çalışır?

macOS 13 Ventura veya üstü yüklü Apple Silicon ve Intel Mac'lerde.

### macOS neden ilk seferde engelliyor?

MacCalendar, ücretli geliştirici hesabı gerektiren Apple onayından (notarization) geçmemiştir. **Sistem Ayarları ▸ Gizlilik ve Güvenlik ▸ Yine de Aç** ile bir kez izin verin; ayrıntılar [İlk açılış](#i̇lk-açılış-kurulum-paketine-bir-kez-izin-verin) bölümünde.

<sub>Itsycal, Dato ve Clocker yalnızca karşılaştırma için anılmıştır; MacCalendar'ın bunlarla bir bağı yoktur.</sub>

""",
        },
    },
    "MacRAR": {
        "en": {
            "lead": ("  A WinRAR-style <b>archive manager</b> for macOS", "  A free, open-source, WinRAR-style <b>archive manager</b> for macOS"),
            "alt": "A free <b>WinRAR</b> alternative for the Mac, and an alternative to <b>Keka</b>, <b>BetterZip</b> and <b>The Unarchiver</b>.",
            "faq": """## FAQ

### Is MacRAR free?

Yes. MacRAR is free and open source under the GPL-3.0 license, and opening and extracting RAR files is free too: RARLAB's free `unrar` comes with the app. Only creating or editing **RAR** archives needs RARLAB's `rar` tool, which is free to try for 40 days and then needs a RARLAB license. Creating ZIP, 7Z and TAR archives never needs it.

### How do I open a RAR file on a Mac?

Install MacRAR and double-click the `.rar` file to look inside, or right-click it in the Finder and extract it without opening the main window. Password-protected archives ask for the password.

### Can I create RAR files on a Mac?

Yes. MacRAR's Setup Assistant downloads RARLAB's `rar` from rarlab.com with one click; then you can create RAR5 or RAR4 archives with a password, file name encryption, a recovery record or split volumes.

### Can I compress and extract from the Finder right-click menu?

Yes. Right-click files in the Finder to compress them to RAR or ZIP, or right-click an archive to extract or open it. The work runs with a small progress panel, without opening MacRAR's main window.

### Which Macs does it run on?

Apple Silicon and Intel Macs with macOS 15 Sequoia or later.

### Why does macOS block it the first time?

MacRAR is not notarized by Apple, which needs a paid developer account. Allow it once in **System Settings ▸ Privacy & Security ▸ Open Anyway**; see [Installation](#installation).

<sub>WinRAR, Keka, BetterZip and The Unarchiver are named only for comparison; MacRAR is not affiliated with them or with RARLAB.</sub>

""",
        },
        "tr": {
            "lead": ("  macOS için WinRAR tarzı bir <b>arşiv yöneticisi</b>", "  macOS için ücretsiz ve açık kaynak, WinRAR tarzı bir <b>arşiv yöneticisi</b>"),
            "alt": "Mac için ücretsiz bir <b>WinRAR</b> alternatifi; <b>Keka</b>, <b>BetterZip</b> ve <b>The Unarchiver</b>'a da alternatif.",
            "faq": """## Sık sorulan sorular

### MacRAR ücretsiz mi?

Evet. MacRAR, GPL-3.0 lisansıyla ücretsiz ve açık kaynaktır; RAR dosyalarını açmak ve çıkarmak da ücretsizdir, çünkü RARLAB'ın ücretsiz `unrar` aracı uygulamayla gelir. Yalnızca **RAR** arşivi oluşturmak ya da düzenlemek için RARLAB'ın `rar` aracı gerekir; 40 gün ücretsiz denenebilir, sonrasında RARLAB lisansı ister. ZIP, 7Z ve TAR oluşturmak için hiç gerekmez.

### Mac'te RAR dosyası nasıl açılır?

MacRAR'ı kurun ve içine bakmak için `.rar` dosyasına çift tıklayın ya da Finder'da sağ tıklayıp ana pencereyi açmadan çıkarın. Parolalı arşivler parolayı sorar.

### Mac'te RAR dosyası oluşturabilir miyim?

Evet. MacRAR'ın Kurulum Yardımcısı RARLAB'ın `rar` aracını rarlab.com'dan tek tıkla indirir; ardından parolalı, dosya adları şifreli, kurtarma kayıtlı ya da parçalara bölünmüş RAR5 veya RAR4 arşivleri oluşturabilirsiniz.

### Finder'ın sağ tık menüsünden sıkıştırıp çıkarabilir miyim?

Evet. Finder'da dosyalara sağ tıklayıp RAR ya da ZIP olarak sıkıştırabilir, bir arşive sağ tıklayıp çıkarabilir ya da açabilirsiniz. İşlem, MacRAR'ın ana penceresi açılmadan küçük bir ilerleme paneliyle yapılır.

### Hangi Mac'lerde çalışır?

macOS 15 Sequoia veya üstü yüklü Apple Silicon ve Intel Mac'lerde.

### macOS neden ilk seferde engelliyor?

MacRAR, ücretli geliştirici hesabı gerektiren Apple onayından (notarization) geçmemiştir. **Sistem Ayarları ▸ Gizlilik ve Güvenlik ▸ Yine de Aç** ile bir kez izin verin; ayrıntılar [Kurulum](#kurulum) bölümünde.

<sub>WinRAR, Keka, BetterZip ve The Unarchiver yalnızca karşılaştırma için anılmıştır; MacRAR'ın bunlarla ya da RARLAB ile bir bağı yoktur.</sub>

""",
        },
    },
    "MacZilla": {
        "en": {
            "lead": ("  A native (SwiftUI) <b>FTP, FTPS and SFTP</b> client for macOS", "  A free, open-source, native (SwiftUI) <b>FTP, FTPS and SFTP</b> client for macOS"),
            "alt": "A free, native alternative to <b>FileZilla</b>, <b>Cyberduck</b> and <b>Transmit</b> on the Mac.",
            "faq": """## FAQ

### Is MacZilla free?

Yes. MacZilla is free and open source under the GPL-3.0 license, with no ads, no accounts and no in-app purchases.

### Is there a native FileZilla for Mac?

FileZilla itself runs on the Mac, but it is not a native Mac app. MacZilla is written in Swift and SwiftUI with the same idea: two panes, tabs, a transfer queue and a Site Manager. It can import your FileZilla sites, folders, bookmarks and passwords.

### Can I connect with SFTP using my SSH key?

Yes. SFTP runs through macOS's own `ssh`, so your SSH keys, ssh-agent, `~/.ssh/config` and `known_hosts` work exactly as in Terminal.

### Does it support FTPS (FTP over TLS)?

Yes, both explicit (FTPES) and implicit (FTPS) TLS. A certificate macOS does not trust is shown with its SHA-256 fingerprint and connects only after you allow it.

### Where are my passwords stored?

In the macOS Keychain. The site list itself is a JSON file in `~/Library/Application Support/MacZilla`.

### Which Macs does it run on?

Apple Silicon and Intel Macs with macOS 14 Sonoma or later.

### Why does macOS block it the first time?

MacZilla is not notarized by Apple, which needs a paid developer account. Allow it once in **System Settings ▸ Privacy & Security ▸ Open Anyway**; see [First launch](#first-launch-allow-maczilla-once).

<sub>FileZilla, Cyberduck and Transmit are named only for comparison; MacZilla is not affiliated with them.</sub>

""",
        },
        "tr": {
            "lead": ("  macOS için FileZilla tarzı, yerel (SwiftUI) bir", "  macOS için ücretsiz ve açık kaynak, FileZilla tarzı, yerel (SwiftUI) bir"),
            "alt": "Mac'te <b>FileZilla</b>, <b>Cyberduck</b> ve <b>Transmit</b>'e ücretsiz ve yerel bir alternatif.",
            "faq": """## Sık sorulan sorular

### MacZilla ücretsiz mi?

Evet. MacZilla, GPL-3.0 lisansıyla ücretsiz ve açık kaynaktır; reklam, hesap ya da uygulama içi satın alma yoktur.

### Mac için yerel bir FileZilla var mı?

FileZilla Mac'te de çalışır, ama yerel bir Mac uygulaması değildir. MacZilla aynı fikirle Swift ve SwiftUI ile yazılmıştır: iki panel, sekmeler, aktarım kuyruğu ve Site Yöneticisi. FileZilla'daki sitelerinizi, klasörlerinizi, yer imlerinizi ve parolalarınızı içe aktarabilir.

### SSH anahtarımla SFTP bağlantısı kurabilir miyim?

Evet. SFTP, macOS'un kendi `ssh` aracıyla çalışır; SSH anahtarlarınız, ssh-agent, `~/.ssh/config` ve `known_hosts` Terminal'deki gibi aynen geçerlidir.

### FTPS (TLS üzerinden FTP) destekliyor mu?

Evet, hem açık (FTPES) hem örtük (FTPS) TLS. macOS'un güvenmediği bir sertifika SHA-256 parmak iziyle gösterilir ve ancak siz izin verince bağlanır.

### Parolalarım nerede saklanıyor?

macOS Anahtar Zinciri'nde. Site listesi ise `~/Library/Application Support/MacZilla` içinde bir JSON dosyasıdır.

### Hangi Mac'lerde çalışır?

macOS 14 Sonoma veya üstü yüklü Apple Silicon ve Intel Mac'lerde.

### macOS neden ilk seferde engelliyor?

MacZilla, ücretli geliştirici hesabı gerektiren Apple onayından (notarization) geçmemiştir. **Sistem Ayarları ▸ Gizlilik ve Güvenlik ▸ Yine de Aç** ile bir kez izin verin; ayrıntılar [İlk açılış](#maczillayı-ilk-açış-bir-kez-izin-verin) bölümünde.

<sub>FileZilla, Cyberduck ve Transmit yalnızca karşılaştırma için anılmıştır; MacZilla'nın bunlarla bir bağı yoktur.</sub>

""",
        },
    },
    "MacExplorer": {
        "en": {
            "lead": ("  A <b>Windows Explorer-style file manager</b> for macOS:", "  A free, open-source <b>Windows Explorer-style file manager</b> for macOS:"),
            "alt": "A free alternative to <b>Finder</b>, <b>Path Finder</b>, <b>ForkLift</b> and <b>Commander One</b> for people who miss Windows Explorer on the Mac.",
            "faq": """## FAQ

### Is MacExplorer free?

Yes. MacExplorer is free and open source under the GPL-3.0 license, with no ads, no accounts and no in-app purchases.

### Is there a Windows Explorer for Mac?

Microsoft does not make one. MacExplorer brings the same way of working to macOS: tabs, the address bar with steps, Windows menu names, Cut and Paste, and the Windows keyboard behaviour.

### Can I cut and paste files on a Mac?

Yes. In MacExplorer, Ctrl+X or ⌘X cuts files and Ctrl+V or ⌘V moves them. Cut items are dimmed until you paste.

### Does it replace Finder?

No, it runs next to Finder. macOS does not reliably allow another app to become the default file viewer, so folders opened from other apps still go to Finder.

### Can it connect to SFTP and FTP servers?

Yes. SFTP, FTP, FTPES and FTPS open in the pane, and SMB, WebDAV, AFP and NFS are mounted as disks. Connect with ⌘K.

### Where are my passwords stored?

Only in the macOS Keychain, and only if you choose to save them.

### Which Macs does it run on?

macOS 15 Sequoia or later, on Apple Silicon and Intel Macs.

### Why does macOS block it the first time?

MacExplorer is not notarized by Apple, which needs a paid developer account. Allow it once in **System Settings ▸ Privacy & Security ▸ Open Anyway**; see [Download and install](#download-and-install).

<sub>Finder, Path Finder, ForkLift, Commander One and Windows Explorer are named only for comparison; MacExplorer is not affiliated with them, with Apple or with Microsoft.</sub>

""",
        },
        "tr": {
            "lead": ("  macOS için <b>Windows Gezgini tarzı dosya yöneticisi</b>:", "  macOS için ücretsiz ve açık kaynak <b>Windows Gezgini tarzı dosya yöneticisi</b>:"),
            "alt": "Mac'te Windows Gezgini'ni arayanlar için <b>Finder</b>, <b>Path Finder</b>, <b>ForkLift</b> ve <b>Commander One</b>'a ücretsiz bir alternatif.",
            "faq": """## Sık sorulan sorular

### MacExplorer ücretsiz mi?

Evet. MacExplorer, GPL-3.0 lisansıyla ücretsiz ve açık kaynaktır; reklam, hesap ya da uygulama içi satın alma yoktur.

### Mac için Windows Gezgini var mı?

Microsoft yapmıyor. MacExplorer aynı çalışma biçimini macOS'a getirir: sekmeler, adımlı adres çubuğu, Windows menü adları, Kes ve Yapıştır, Windows klavye davranışı.

### Mac'te dosya kesip yapıştırabilir miyim?

Evet. MacExplorer'da Ctrl+X ya da ⌘X dosyaları keser, Ctrl+V ya da ⌘V taşır. Kesilen öğeler yapıştırılana kadar soluk görünür.

### Finder'ın yerini alıyor mu?

Hayır, Finder'ın yanında çalışır. macOS başka bir uygulamanın varsayılan dosya görüntüleyici olmasına güvenilir biçimde izin vermiyor; bu yüzden başka uygulamalardan açılan klasörler yine Finder'a gider.

### SFTP ve FTP sunucularına bağlanabilir mi?

Evet. SFTP, FTP, FTPES ve FTPS panelde açılır; SMB, WebDAV, AFP ve NFS disk olarak bağlanır. ⌘K ile bağlanın.

### Parolalarım nerede saklanıyor?

Yalnızca macOS Anahtar Zinciri'nde ve yalnızca kaydetmeyi seçerseniz.

### Hangi Mac'lerde çalışır?

macOS 15 Sequoia veya üstü yüklü Apple Silicon ve Intel Mac'lerde.

### macOS neden ilk seferde engelliyor?

MacExplorer, ücretli geliştirici hesabı gerektiren Apple onayından (notarization) geçmemiştir. **Sistem Ayarları ▸ Gizlilik ve Güvenlik ▸ Yine de Aç** ile bir kez izin verin; ayrıntılar [İndirme ve kurulum](#indirme-ve-kurulum) bölümünde.

<sub>Finder, Path Finder, ForkLift, Commander One ve Windows Gezgini yalnızca karşılaştırma için anılmıştır; MacExplorer'ın bunlarla, Apple ya da Microsoft ile bir bağı yoktur.</sub>

""",
        },
    },
    "MacNote++": {
        "en": {
            "lead": ("  A native <b>text, code and hex editor</b> for macOS:", "  A free, open-source <b>text, code and hex editor</b> for macOS:"),
            "alt": "A free alternative to <b>BBEdit</b>, <b>CotEditor</b> and <b>Sublime Text</b> for everyday text and code editing on the Mac.",
            "faq": """## FAQ

### Is MacNote++ free?

Yes. MacNote++ is free and open source under the GPL-3.0-or-later license, with no ads, no accounts and no in-app purchases.

### Does it send my files anywhere?

No. The only network request is the update check, which reads the latest release information from gitlab.com at most once a day. You can turn it off in Settings.

### Can it open very large files?

Yes. Files of 80 MB or more can open as a preview, and hex view reads even a 1 GB file from disk as you scroll.

### Can I edit several lines at once?

Yes. Add cursors with ⌥ + click or ⌥⇧↑ / ↓, or select a rectangle with ⌥ + drag, then type.

### Which Macs does it run on?

macOS 14 Sonoma or later, on Apple Silicon and Intel Macs.

### Why does macOS block it the first time?

MacNote++ is not notarized by Apple, which needs a paid developer account. Allow it once in **System Settings ▸ Privacy & Security ▸ Open Anyway**; see [Download and install](#download-and-install).

<sub>BBEdit, CotEditor and Sublime Text are named only for comparison; MacNote++ is not affiliated with them or with Apple.</sub>

""",
        },
        "tr": {
            "lead": ("  macOS için <b>metin, kod ve hex düzenleyici</b>:", "  macOS için ücretsiz ve açık kaynak <b>metin, kod ve hex düzenleyici</b>:"),
            "alt": "Mac'te günlük metin ve kod düzenleme için <b>BBEdit</b>, <b>CotEditor</b> ve <b>Sublime Text</b>'e ücretsiz bir alternatif.",
            "faq": """## Sık sorulan sorular

### MacNote++ ücretsiz mi?

Evet. MacNote++, GPL-3.0-or-later lisansıyla ücretsiz ve açık kaynaktır; reklam, hesap ya da uygulama içi satın alma yoktur.

### Dosyalarımı bir yere gönderiyor mu?

Hayır. Tek ağ isteği güncelleme denetimidir; günde en fazla bir kez gitlab.com'dan son sürüm bilgisini okur. Ayarlar'dan kapatabilirsiniz.

### Çok büyük dosyaları açabilir mi?

Evet. 80 MB ve üstü dosyalar önizlemeyle açılabilir; hex görünümü 1 GB'lık dosyayı bile siz kaydırdıkça diskten okur.

### Birden fazla satırı aynı anda düzenleyebilir miyim?

Evet. ⌥ + tık ya da ⌥⇧↑ / ↓ ile imleç ekleyin veya ⌥ + sürükleme ile dikdörtgen seçim yapıp yazın.

### Hangi Mac'lerde çalışır?

macOS 14 Sonoma veya üstü, Apple Silicon ve Intel Mac'ler.

### macOS neden ilk seferde engelliyor?

MacNote++ Apple tarafından onaylanmamıştır; bunun için ücretli geliştirici hesabı gerekir. **Sistem Ayarları ▸ Gizlilik ve Güvenlik ▸ Yine de Aç** ile bir kez izin verin; bkz. [İndirme ve kurulum](#indirme-ve-kurulum).

<sub>BBEdit, CotEditor ve Sublime Text yalnızca karşılaştırma için anılmıştır; MacNote++ bunlarla ya da Apple ile bağlantılı değildir.</sub>

""",
        },
    },
}
