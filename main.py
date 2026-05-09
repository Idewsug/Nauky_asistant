
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from jnius import autoclass
import android
PythonActivity = autoclass('org.kivy.android.PythonActivity')
Context = autoclass('android.content.Context')
Intent = autoclass('android.content.Intent')
Uri = autoclass('android.net.Uri')
TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
Locale = autoclass('java.util.Locale')
CameraManager = autoclass('android.hardware.camera2.CameraManager')
MediaStore = autoclass('android.provider.MediaStore')
class NaukyAssistant(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.label = Label(text='Nauky Siap... Bilang "Halo Nauky"', font_size='20sp')
        self.add_widget(self.label)
        self.tts = TextToSpeech(PythonActivity.mActivity, None)
        self.tts.setLanguage(Locale('id', 'ID'))
        self.tts.setPitch(1.15)
        self.tts.setSpeechRate(0.85)
        self.camera_manager = PythonActivity.mActivity.getSystemService(Context.CAMERA_SERVICE)
        self.camera_id = self.camera_manager.getCameraIdList()[0]
        self.torch_on = False
        Clock.schedule_once(lambda dt: self.speak("Halo kaka, aku Nauky siap bantu"), 2)
    def speak(self, text):
        self.label.text = f"Nauky: {text}"
        self.tts.speak(text, TextToSpeech.QUEUE_FLUSH, None, None)
    def on_command(self, text):
        text = text.lower()
        if "halo nauky" in text: self.speak("Halo kaka")
        elif "panggil mama" in text: self.speak("mama dipanggil"); self.wa_call("6282353035353")
        elif "panggil elisa" in text: self.speak("elisa dipanggil"); self.wa_call("6289612848532")
        elif "panggil optimus" in text: self.speak("optimus dipanggil"); self.wa_call("6285757099300")
        elif "nyalakan senter" in text: self.speak("senter dinyalakan"); self.toggle_torch(True)
        elif "matikan senter" in text: self.speak("senter dimatikan"); self.toggle_torch(False)
        elif "buka maps" in text: self.speak("maps dibuka"); self.open_app("com.google.android.apps.maps")
        elif "tutup maps" in text: self.speak("maps ditutup"); self.go_home()
        elif "buka youtube" in text: self.speak("youtube dibuka"); self.open_app("com.google.android.youtube")
        elif "buka kamera" in text: self.speak("kamera dibuka"); self.open_camera()
        elif "tutup kamera" in text: self.speak("kamera ditutup"); self.go_home()
        elif "rekam video" in text: self.speak("video merekam"); self.record_video()
        elif "stop merekam" in text: self.speak("merekam ditutup"); self.go_home()
        else: self.speak("maaf kaka, aku belum ngerti")
    def wa_call(self, nomor):
        uri = Uri.parse(f"https://wa.me/{nomor}")
        intent = Intent(Intent.ACTION_VIEW, uri)
        PythonActivity.mActivity.startActivity(intent)
    def open_app(self, package_name):
        intent = PythonActivity.mActivity.getPackageManager().getLaunchIntentForPackage(package_name)
        if intent: PythonActivity.mActivity.startActivity(intent)
        else: self.speak("aplikasinya gak ada kaka")
    def open_camera(self):
        intent = Intent(MediaStore.INTENT_ACTION_STILL_IMAGE_CAMERA)
        PythonActivity.mActivity.startActivity(intent)
    def record_video(self):
        intent = Intent(MediaStore.INTENT_ACTION_VIDEO_CAMERA)
        PythonActivity.mActivity.startActivity(intent)
    def toggle_torch(self, state):
        self.camera_manager.setTorchMode(self.camera_id, state)
        self.torch_on = state
    def go_home(self):
        intent = Intent(Intent.ACTION_MAIN)
        intent.addCategory(Intent.CATEGORY_HOME)
        PythonActivity.mActivity.startActivity(intent)
class NaukyApp(App):
    def build(self): return NaukyAssistant()
if __name__ == '__main__': NaukyApp().run()
