[app]

title = Asisten Nauky
package.name = nauky
package.domain = org.idewsug

source.dir =.
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy,pyjnius

android.permissions = CAMERA,INTERNET,RECORD_AUDIO,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,CALL_PHONE,WAKE_LOCK,FLASHLIGHT

android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk_path =

[buildozer]
log_level = 2
warn_on_root = 1
