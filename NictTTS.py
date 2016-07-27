# encoding: shift_jis
import urllib2
import json
import base64
import sys
import winsound

usage = """NictTTS.py

●使い方
しゃべらせたい場合：
  NictTTS.py こんにちは
waveファイルで保存したい場合：
  NictTTS.py こんにちは test.wav
"""

def Text2Wave( message , filename ):
    url = u'http://rospeex.ucri.jgn-x.jp/nauth_json/jsServices/VoiceTraSS?method=speak&params=[ja,' + urllib2.quote(message.encode("utf_8")) + u',"*","audio/x-wav"]'

    req = urllib2.Request(url )
    print req.get_full_url()
    response = urllib2.urlopen(req)

    res = response.read()
    result = json.loads( res )
    wave = base64.b64decode( result["result"]["audio"] )

    f = open( filename , "wb" )
    f.write( wave )
    f.close()

def main():
    if len(sys.argv)==3:
        Text2Wave( sys.argv[1].decode("sjis") , sys.argv[2] )
    elif len(sys.argv)==2:
        Text2Wave( sys.argv[1].decode("sjis") , "tmp.wav" )
        winsound.PlaySound("tmp.wav", winsound.SND_FILENAME)
    else:
        print usage


if __name__ == '__main__':
    main()